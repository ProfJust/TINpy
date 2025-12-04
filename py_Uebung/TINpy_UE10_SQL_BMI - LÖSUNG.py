import sys
import os
import mysql.connector
from mysql.connector import Error

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTableWidget, QTableWidgetItem, QPushButton, QLabel, QLineEdit, QMessageBox
)
from PyQt6.QtCore import Qt


DB_NAME = "db_tinpy"
TABLE_NAME = "swz_table"


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "youbot"),
        database=DB_NAME,
    )


class QSqlTableModel_Example(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("PyQt + MariaDB Beispiel")

        self.cnx = None
        self.cur = None

        self._init_db_table()
        self._init_ui()
        self._load_table_data()

    # ---------------- DB-Setup ----------------
    def _init_db_table(self):
        """Datenbank-Verbindung aufbauen und Tabelle anlegen, falls nicht vorhanden."""
        try:
            self.cnx = get_connection()
            self.cur = self.cnx.cursor()

            create_sql = f"""
                CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                    ids INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                    weight FLOAT,
                    size FLOAT
                )
            """
            
            self.cur.execute(create_sql)
            self.cnx.commit()
        except Error as e:
            QMessageBox.critical(self, "DB-Fehler", f"Fehler beim DB-Setup:\n{e}")
            sys.exit(1)

    # ---------------- UI-Setup ----------------
    def _init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout()
        central.setLayout(main_layout)

        # Tabelle
        self.table = QTableWidget()
        #self.table.setColumnCount(3)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["id", "weight", "size", "BMI", "Status"])
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        main_layout.addWidget(self.table)

        # Eingabe-Felder
        form_layout = QHBoxLayout()
        self.input_weight = QLineEdit()
        self.input_weight.setPlaceholderText("Gewicht [kg]")
        self.input_size = QLineEdit()
        self.input_size.setPlaceholderText("Größe [m]")

        form_layout.addWidget(self.input_weight)
        form_layout.addWidget(self.input_size)

        main_layout.addLayout(form_layout)

        # Buttons
        btn_layout = QHBoxLayout()

        self.btn_add_row = QPushButton("Zeile hinzufügen")
        self.btn_delete_row = QPushButton("Ausgewählte Zeile löschen")
        self.btn_get_avg_weight = QPushButton("Durchschnittsgewicht")
        self.btn_get_overweight = QPushButton("Übergewichtige anzeigen (BMI > 25)")

        btn_layout.addWidget(self.btn_add_row)
        btn_layout.addWidget(self.btn_delete_row)
        btn_layout.addWidget(self.btn_get_avg_weight)
        btn_layout.addWidget(self.btn_get_overweight)

        main_layout.addLayout(btn_layout)

        # Label für Durchschnitt
        self.lbl_avg_weight = QLabel("Durchschnittsgewicht: -")
        main_layout.addWidget(self.lbl_avg_weight)

        # Signale
        self.btn_add_row.clicked.connect(self.add_row)
        self.btn_delete_row.clicked.connect(self.delete_row)
        self.btn_get_avg_weight.clicked.connect(self.calc_avg_weight)
        self.btn_get_overweight.clicked.connect(self.show_overweight)

    # ---------------- DB-Hilfsfunktionen ----------------
    def _load_table_data(self):
        """Daten aus der DB in die TableWidget laden."""
        try:
            
            sql = f"SELECT ids, weight, size, bmi, bmi_text FROM {TABLE_NAME}"

            self.cur.execute(sql)
            rows = self.cur.fetchall()

            self.table.setRowCount(len(rows))
            for r, (id_, weight, size, bmi, bmi_text) in enumerate(rows):
                self.table.setItem(r, 0, QTableWidgetItem(str(id_)))
                self.table.setItem(r, 1, QTableWidgetItem(str(weight)))
                self.table.setItem(r, 2, QTableWidgetItem(str(size)))
                self.table.setItem(r, 3, QTableWidgetItem(str(bmi)))
                self.table.setItem(r, 4, QTableWidgetItem(str(bmi_text)))

        except Error as e:
            QMessageBox.critical(self, "DB-Fehler", f"Fehler beim Laden der Daten:\n{e}")

    # ---------------- Slots / Aktionen ----------------
    def add_row(self):
        """Neue Zeile mit weight und size einfügen."""
        try:
            weight_str = self.input_weight.text().strip()
            size_str = self.input_size.text().strip()

            if not weight_str or not size_str:
                QMessageBox.warning(self, "Eingabe fehlt", "Bitte Gewicht und Größe eingeben.")
                return

            weight = float(weight_str)
            size = float(size_str)

            sql = f"INSERT INTO {TABLE_NAME} (weight, size) VALUES (%s, %s)"
            self.cur.execute(sql, (weight, size))
            self.cnx.commit()

            self.input_weight.clear()
            self.input_size.clear()
            self._load_table_data()

        except ValueError:
            QMessageBox.warning(self, "Eingabefehler", "Gewicht und Größe müssen Zahlen sein.")
        except Error as e:
            QMessageBox.critical(self, "DB-Fehler", f"Fehler beim Einfügen:\n{e}")

    def delete_row(self):
        """Ausgewählte Zeile aus DB löschen."""
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.information(self, "Keine Auswahl", "Bitte eine Zeile in der Tabelle auswählen.")
            return

        id_item = self.table.item(row, 0)
        if id_item is None:
            return

        id_ = int(id_item.text())   # ID der ausgewählten Zeile

        try:
            sql = f"DELETE FROM {TABLE_NAME} WHERE ids = %s"
            self.cur.execute(sql, (id_,))
            self.cnx.commit()
            self._load_table_data()
        except Error as e:
            QMessageBox.critical(self, "DB-Fehler", f"Fehler beim Löschen:\n{e}")

    def calc_avg_weight(self):
        """Durchschnittsgewicht berechnen und im Label anzeigen."""
        try:
            sql = f"SELECT AVG(weight) FROM {TABLE_NAME}"
            self.cur.execute(sql)
            (avg_weight,) = self.cur.fetchone()
            if avg_weight is None:
                self.lbl_avg_weight.setText("Durchschnittsgewicht: -")
            else:
                self.lbl_avg_weight.setText(f"Durchschnittsgewicht: {avg_weight:.2f} kg")
        except Error as e:
            QMessageBox.critical(self, "DB-Fehler", f"Fehler beim Berechnen des Durchschnitts:\n{e}")

    def show_overweight(self):
        """Nur Personen mit BMI > 25 anzeigen."""
        # # SELECT * FROM swz_table WHERE bmi > 25.0;
        # sql = f"SELECT * FROM swz_table WHERE bmi > 25.0" 
        # self.cur.execute(sql, (id,))
        # print(f"{self.cur.rowcount} Übergewichtige:")

        select_sql = "SELECT * FROM swz_table WHERE bmi > 25.0"
        self.cur.execute(select_sql)
        rows = self.cur.fetchall()   # wichtig: alles lesen, sonst "Unread result found"[web:52][web:55]

        print(f"{len(rows)} Uebergewichtige:")
        for row in rows:
            ids, weight, size, bmi, bmi_text = row
            print(f"  ID={ids}, weight={weight} size={size} bmi={bmi}")

    # ---------------- Aufräumen ----------------
    def closeEvent(self, event):
        try:
            if self.cur is not None:
                self.cur.close()
            if self.cnx is not None and self.cnx.is_connected():
                self.cnx.close()
        except Error:
            pass
        super().closeEvent(event)


def main():
    app = QApplication(sys.argv)
    w = QSqlTableModel_Example()
    w.resize(700, 400)
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

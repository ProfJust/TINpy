import os
import mysql.connector
from mysql.connector import Error


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "youbot"),
        database="db_tinpy",
    )


def main():
    cnx = None
    cur = None

    try:
        cnx = get_connection()
        print("Verbindung zur Datenbank aufgebaut.")
        cur = cnx.cursor()

        # 1) EINTRAG HINZUFÜGEN
        insert_sql = "INSERT INTO tbl_temp (temp_value) VALUES (%s)"
        temp = 42.9  # Python-float; passt direkt zum FLOAT-Feld[web:72][web:58]

        cur.execute(insert_sql, (temp,))
        cnx.commit()

        print("1 Datensatz hinzugefügt, ID:", cur.lastrowid)

        # 2) ALLE DATEN LESEN (Resultset komplett abholen!)
        select_sql = "SELECT temp_id, temp_value FROM tbl_temp"
        cur.execute(select_sql)
        rows = cur.fetchall()   # wichtig: alles lesen, sonst "Unread result found"[web:52][web:55]

        print(f"{len(rows)} Datensätze in der Tabelle tbl_temp:")
        for row in rows:
            temp_id, temp_value = row
            print(f"  ID={temp_id}, temp_value={temp_value}")

    except Error as e:
        print("Fehler beim Zugriff auf die Datenbank:", e)

    finally:
        if cur is not None:
            cur.close()
        if cnx is not None and cnx.is_connected():
            cnx.close()
            print("Verbindung zur Datenbank geschlossen.")


if __name__ == "__main__":
    main()

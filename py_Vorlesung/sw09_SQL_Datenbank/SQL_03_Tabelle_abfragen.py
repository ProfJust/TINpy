# SQL_02_Tabellen_erstellen.py
import os
import mysql.connector  # ggf. pip install mysql-connector-python
from mysql.connector import Error


def get_connection():
    """Erstellt eine neue DB-Verbindung.
        LOCALHOST für lokalen Server hat die IP 127.0.0.1
        Standardport für MySQL ist 3306
        Benutzername und Passwort anpassen
        Hier: root mit Passwort youbot
        ACHTUNG: unsicher, nur für Testzwecke!
        Bei produktiven Systemen: sichere Methoden verwenden!
        z.B. Umgebungsvariablen, Konfigurationsdateien, etc.
        Keine sensiblen Zugangsdaten im Quellcode speichern!
    """
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "youbot"),
        database='db_tinpy'        
    )

def main():
    try:
        cnx = get_connection() # Verbindung aufbauen
        print("Verbindung zur Datenbank aufgebaut.")

        with cnx.cursor() as cur: # Create a cursor object
            query="SHOW TABLES" #query to show all the tables in the database
            print("Query:", query ) 
            cur.execute(query) #executing the query   
            for table in cur: # printing all the tables
                print(table)

    except Error as e: # Fehlerbehandlung
        print("Fehler beim Zugriff auf die Datenbank:", e)

    finally: 
        # Verbindung sauber schließen, falls aufgebaut
        if 'cnx' in locals() and cnx.is_connected():
            cnx.close()
            print("Verbindung zur Datenbank geschlossen.")


if __name__ == "__main__":
    main()



import mysql.connector  # ggf. pip install mysql-connector-python

# Connect to server (ohne Angabe einer Datenbank)
# LOCALHOST für lokalen Server hat die IP 127.0.0.1
# Standardport für MySQL ist 3306
# Benutzername und Passwort anpassen
# Hier: root mit Passwort youbot
# ACHTUNG: unsicher, nur für Testzwecke!
# Bei produktiven Systemen: sichere Methoden verwenden!
# z.B. Umgebungsvariablen, Konfigurationsdateien, etc.
# Keine sensiblen Daten im Quellcode speichern!

# Verbindung aufbauen
cnx = mysql.connector.connect(
    host="127.0.0.1",  
    port=3306,
    user="root",
    password="youbot")

# Get a cursor
#----------------------------
cur = cnx.cursor() # Create a cursor object
# A cursor allows you to execute SQL queries
# and fetch results
# Cursors are used to interact with the database
# They provide methods to execute queries   
# and retrieve data

# Execute a query
#----------------------------
# Example query: Get current date from the database server
cur.execute("SELECT CURDATE()")


# Fetch one result
#----------------------------
row = cur.fetchone() # Fetch one row from the result set    
#   fetchone() retrieves the next row of a query result set
#   It returns a single sequence, or None when no more data is available        
print("Current date from database server:", row[0])  # Print the first column of the row 

print()  # Blank line for better readability
print("---- Done ----")

# Close connections
#----------------------------
cur.close() # Close the cursor  
cnx.close() # Close the connection to the database server

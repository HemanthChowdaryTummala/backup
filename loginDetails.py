import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('TreatmentTeamSample.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create the "login" table
cursor.execute('''
    CREATE TABLE login (
        username TEXT,
        password TEXT
    )
''')

# List of usernames
usernames = ["PT1001", "PT1002", "PT1003", "PT1004", "PT1005", "PT1006", "PT1007", "PT1008", "PT1009", "PT1010"]

# Insert rows with matching username and password
for username in usernames:
    cursor.execute('INSERT INTO login (username, password) VALUES (?, ?)', (username, username))

# Commit the changes and close the database connection
conn.commit()
conn.close()

print("Table 'login' created and populated with data.")

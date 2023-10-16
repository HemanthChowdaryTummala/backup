import sqlite3

# Connect to the database (creates a new database if it doesn't exist)
conn = sqlite3.connect('TreatmentTeamSample.db')
cursor = conn.cursor()

# Create the Pharmacist table
cursor.execute('''CREATE TABLE IF NOT EXISTS Pharmacist (
                    ID TEXT PRIMARY KEY,
                    Name TEXT,
                    DateOfBirth TEXT,
                    Title TEXT,
                    Company TEXT,
                    Phone TEXT,
                    Email TEXT
                )''')

# Data to insert into the Pharmacist table
data_to_insert = [
    ('PHR1001', 'Justin', 'DOB12121984', 'Pharmacist', 'EverGreen Pharmacy', '+12564014540', 'justin@evergreen.phar'),
    ('PHR1002', 'Madison', 'DOB15071977', 'Pharm Technician', 'BlueSky Pharmacy', '+15134414566', 'madison@bluesky.drug')
]

# Insert the data into the Pharmacist table
cursor.executemany('INSERT INTO Pharmacist VALUES (?, ?, ?, ?, ?, ?, ?)', data_to_insert)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data inserted successfully.")

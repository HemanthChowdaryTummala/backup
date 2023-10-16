import sqlite3

# Connect to the database (creates a new database if it doesn't exist)
conn = sqlite3.connect('TreatmentTeamSample.db')
cursor = conn.cursor()

# Create the InsuranceAgent table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS InsuranceAgent (
                    ID TEXT PRIMARY KEY,
                    Name TEXT,
                    DateOfBirth TEXT,
                    Title TEXT,
                    Company TEXT,
                    Phone TEXT,
                    Email TEXT
                )''')

# Data to insert into the InsuranceAgent table
data_to_insert = [
    ('ICA1001', 'Jasper', 'DOB21091955', 'Senior Agent', 'Anthem Health Plan', '+13524606592', 'jasper@antheplan.org'),
    ('ICA1002', 'Hanan', 'DOB17021985', 'Agent', 'Care Health Insurance', '+18189025033', 'hanan@care.care')
]

# Insert the data into the InsuranceAgent table
cursor.executemany('INSERT INTO InsuranceAgent VALUES (?, ?, ?, ?, ?, ?, ?)', data_to_insert)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data inserted into InsuranceAgent table successfully.")

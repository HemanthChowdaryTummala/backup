import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("TreatmentTeamSample.db")

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create the Health_Records table with columns (Record ID, Record Name, Record Description)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Health_Records (
        RecordID TEXT PRIMARY KEY,
        RecordName TEXT,
        RecordDescription TEXT
    )
''')

# Sample data to insert (including the first three columns)
records_data = [
    ("HR1001", "Demographic Info", "Patient’s information"),
    ("HR1002", "Previous Medical History", "Old medical records from another hospital"),
    ("HR1003", "Immunizations", "Immunization records that are administered over time"),
    ("HR1004", "Allergies", "Various allergies sources, triggering condition, remediation"),
    ("HR1005", "Visit Notes", "Contains physiological data, disease description, advice, follow-up, visit details"),
    ("HR1006", "Medications and Prescription", "Prescribed medications including name, dosage, etc."),
    ("HR1007", "Pathology Lab Works", "Blood work"),
    ("HR1008", "Radiology Lab Works", "Imaging and Radiology Lab results"),
    ("HR1009", "Billing and Insurance", "Bank account and insurance policy Information"),
    ("HR1010", "Payer Transactions", "Bills of doctor visit, lab works, and medications")
]

# Insert the first three columns (Record ID, Record Name, and Record Description) into the table
cursor.executemany('INSERT INTO Health_Records (RecordID, RecordName, RecordDescription) VALUES (?, ?, ?)', records_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

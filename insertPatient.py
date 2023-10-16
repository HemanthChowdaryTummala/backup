import sqlite3

# Connect to the database (this will create the database if it doesn't exist)
conn = sqlite3.connect('TreatmentTeamSample.db')
cursor = conn.cursor()

# Define a SQL command to create the table if it doesn't exist
create_table_query = '''
CREATE TABLE IF NOT EXISTS patients (
    patient_id TEXT PRIMARY KEY,
    first_name TEXT,
    date_of_birth TEXT,
    gender TEXT,
    phone TEXT,
    email TEXT
);
'''

# Execute the SQL command to create the table
cursor.execute(create_table_query)

# Define the data to insert
patient_data = [
    ("PT1001", "Jordan", "DOB11251980", "Male", "+15306524342", "jordam@compliance.com"),
    ("PT1002", "Simon", "DOB10151982", "Male", "+15737524481", "simon@compliance.com"),
    ("PT1003", "Tatum", "DOB11051984", "Male", "+14324386527", "tatum@compliance.com"),
    ("PT1004", "Thomas", "DOB12201986", "Male", "+16609079598", "thomas@compliance.com"),
    ("PT1005", "David", "DOB05091975", "Male", "+15702917315", "david@compliance.com"),
    ("PT1006", "Alexander", "DOB01271978", "Male", "+16578059479", "alexander@compliance.com"),
    ("PT1007", "Sarah", "DOB09281970", "Female", "+12058912490", "sarah@compliance.com"),
    ("PT1008", "Ronald", "DOB03151979", "Male", "+13238648870", "ronald@compliance.com"),
    ("PT1009", "Rebecca", "DOB12251985", "Female", "+14426746222", "rebecca@compliance.com"),
    ("PT1010", "Emma", "DOB10151995", "Female", "+16098632161", "emma@compliance.com"),
]

# Define the SQL command to insert data into the patients table
insert_query = '''
INSERT INTO patients (patient_id, first_name, date_of_birth, gender, phone, email)
VALUES (?, ?, ?, ?, ?, ?);
'''

# Execute the SQL command for each set of data
for patient in patient_data:
    cursor.execute(insert_query, patient)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database 'TreatmentTeamSample.db' and table 'patients' created, and data inserted successfully.")

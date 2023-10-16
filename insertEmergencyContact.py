import sqlite3

# Connect to the database (this will create the database if it doesn't exist)
conn = sqlite3.connect('TreatmentTeamSample.db')
cursor = conn.cursor()

# Define a SQL command to create the "emergencyContact" table if it doesn't exist
create_emergency_contact_table_query = '''
CREATE TABLE IF NOT EXISTS emergencyContact (
    contact_id TEXT PRIMARY KEY,
    name TEXT,
    date_of_birth TEXT,
    phone TEXT,
    email TEXT,
    patient_id TEXT,
    relationship TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients (patient_id)
);
'''

# Execute the SQL command to create the "emergencyContact" table
cursor.execute(create_emergency_contact_table_query)

# Define the data to insert into the "emergencyContact" table
emergency_contact_data = [
    ("EC1001", "Olivia", "DOB11041992", "+15135030830", "olivia@service.info", "PT1001", "Sister"),
    ("EC1002", "Isabella", "DOB12281972", "+12246579011", "isabella@service.info", "PT1002", "Aunt"),
    ("EC1003", "Amelia", "DOB07011999", "+15166694568", "amelia@service.info", "PT1003", "Mother"),
    ("EC1004", "Alice", "DOB12251998", "+12164898791", "alice@service.info", "PT1004", "Spouse"),
    ("EC1005", "Eleanor", "DOB09111990", "+14305361691", "eleanor@service.info", "PT1005", "Spouse"),
    ("EC1006", "Benjamin", "DOB10071980", "+15772628573", "benjamin@service.info", "PT1006", "Friend"),
    ("EC1007", "Theodore", "DOB06281992", "+15646892293", "theodore@service.info", "PT1007", "Son"),
    ("EC1008", "Henry", "DOB08061982", "+15416532424", "henry@service.info", "PT1008", "Brother"),
    ("EC1009", "Arthur", "DOB12101994", "+16025371089", "arthur@service.info", "PT1009", "Brother"),
    ("EC1010", "Liam", "DOB02101987", "+13217057450", "liam@service.info", "PT1010", "Cousin"),
]

# Define the SQL command to insert data into the "emergencyContact" table
insert_emergency_contact_query = '''
INSERT INTO emergencyContact (contact_id, name, date_of_birth, phone, email, patient_id, relationship)
VALUES (?, ?, ?, ?, ?, ?, ?);
'''

# Execute the SQL command for each set of emergency contact data
for contact in emergency_contact_data:
    cursor.execute(insert_emergency_contact_query, contact)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Table 'emergencyContact' created, and data inserted successfully.")

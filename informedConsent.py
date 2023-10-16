import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('TreatmentTeamSample.db')
cursor = conn.cursor()

# Create the Informed Consent table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS InformedConsent (
        Subject TEXT,
        Action TEXT,
        ObjectId TEXT,
        Object TEXT
    )
''')

cursor.execute(f"PRAGMA table_info(TreatmentTeam)")
columns_info = cursor.fetchall()
column_names = [column[1] for column in columns_info]
# Retrieve data from the TreatmentTeam table
cursor.execute('SELECT * FROM TreatmentTeam')
treatment_team_data = cursor.fetchall()

# Define the health_records dictionary (as in the previous response)
health_records = {
    "HR1001": {
        # "Record Name": "Demographic Info",
        "Read": ["Patient", "Doctor", "Support_Staff"],
        "Write": ["Patient", "Support_Staff"],
        "Update": ["Patient", "Support_Staff"]
    },
    "HR1002": {
        # "Record Name": "Previous Medical History",
        "Read": ["Doctor", "Patient"],
        "Write": ["Patient", "Doctor"],
        "Update": ["Patient", "Doctor"]
    },
    "HR1003": {
        # "Record Name": "Immunizations",
        "Read": ["Doctor", "Patient", "Pathology_Lab_Technician"],
        "Write": ["Pathology_Lab_Technician"],
        "Update": ["Pathology_Lab_Technician"]
    },
    "HR1004": {
        # "Record Name": "Allergies",
        "Read": ["Doctor", "Patient", "Nurse"],
        "Write": ["Patient", "Pathology_Lab_Technician"],
        "Update": ["Patient", "Pathology_Lab_Technician"]
    },
    "HR1005": {
        # "Record Name": "Visit Notes",
        "Read": ["Doctor", "Nurse", "Patient"],
        "Write": ["Doctor"],
        "Update": ["Doctor"]
    },
    "HR1006": {
        # "Record Name": "Medications and Prescription",
        "Read": ["Doctor", "Patient", "Nurse", "Pharmacist", "Insurance_Agent"],
        "Write": ["Doctor"],
        "Update": ["Doctor"]
    },
    "HR1007": {
        # "Record Name": "Pathology Lab Works",
        "Read": ["Pathology_Lab_Technician", "Doctor", "Patient"],
        "Write": ["Pathology_Lab_Technician"],
        "Update": ["Pathology_Lab_Technician"]
    },
    "HR1008": {
        # "Record Name": "Radiology Lab Works",
        "Read": ["Radiology_Lab_Technician", "Doctor", "Patient"],
        "Write": ["Radiology_Lab_Technician"],
        "Update": ["Radiology_Lab_Technician"]
    },
    "HR1009": {
        # "Record Name": "Billing and Insurance",
        "Read": ["Patient", "Billing_Office", "Insurance_Agent"],
        "Write": ["Billing_Office", "Patient"],
        "Update": ["Billing_Office", "Patient"]
    },
    "HR1010": {
        # "Record Name": "Payer Transactions",
        "Read": ["Patient", "Billing_Office", "Insurance_Agent"],
        "Write": ["Billing_Office", "Insurance_Agent"],
        "Update": ["Billing_Office", "Insurance_Agent"]
    }
}

# Iterate through the TreatmentTeam data and insert records into InformedConsent
for row in treatment_team_data:
    for i in range(1,10):
        for record_id,access in health_records.items():
            for action,allowed in access.items():
                for user in allowed:
                    if(column_names[i] == user):
                        # print(row[i], action, row[0], record_id)
                        cursor.execute('INSERT INTO InformedConsent (Subject, Action, ObjectId, Object) VALUES (?, ?, ?, ?)',
                               (row[i], action, row[0], record_id))

           

# Commit the changes and close the database connection
conn.commit()
conn.close()

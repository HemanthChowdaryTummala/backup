import sqlite3
import random

# Connect to the database
conn = sqlite3.connect('TreatmentTeamsample.db')
cursor = conn.cursor()

# Delete the existing TreatmentTeam table if it exists
cursor.execute('DROP TABLE IF EXISTS TreatmentTeam')

# Create the TreatmentTeam table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS TreatmentTeam (
        Patient TEXT,
        Doctor TEXT,
        Nurse TEXT,
        Support_Staff TEXT,
        Billing_Office TEXT,
        Radiology_Lab_Technician TEXT,
        Pathology_Lab_Technician TEXT,
        Emergency_Contact TEXT,
        Pharmacist TEXT,
        Insurance_Agent TEXT
    )
''')

# Select all providers for each role
cursor.execute('''
    SELECT provider_id FROM Provider WHERE title = 'Doctor'
''')
doctors = cursor.fetchall()

cursor.execute('''
    SELECT provider_id FROM Provider WHERE title = 'Nurse'
''')
nurses = cursor.fetchall()

cursor.execute('''
    SELECT provider_id FROM Provider WHERE title = 'Support Staff'
''')
support_staff = cursor.fetchall()

cursor.execute('''
    SELECT provider_id FROM Provider WHERE title = 'Billing Officer'
''')
billing_officers = cursor.fetchall()

cursor.execute('''
    SELECT provider_id FROM Provider WHERE title = 'Radiology Tech'
''')
radiology_techs = cursor.fetchall()

cursor.execute('''
    SELECT provider_id FROM Provider WHERE title = 'Pathology Tech'
''')
pathology_techs = cursor.fetchall()

cursor.execute('SELECT patient_id, contact_id FROM Patients JOIN emergencyContact USING (patient_id)')
patients_with_contacts = cursor.fetchall()

cursor.execute('''
    SELECT ID FROM Pharmacist
''')
pharmacists = cursor.fetchall()

cursor.execute('''
    SELECT ID FROM InsuranceAgent
''')
insurance_agents = cursor.fetchall()

# Create teams and assign providers and emergency contacts randomly
for patient_id, contact_id in patients_with_contacts:
    team = (
        patient_id,
        random.choice(doctors)[0],
        random.choice(nurses)[0],
        random.choice(support_staff)[0],
        random.choice(billing_officers)[0],
        random.choice(radiology_techs)[0],
        random.choice(pathology_techs)[0],
        contact_id,
        random.choice(pharmacists)[0],
        random.choice(insurance_agents)[0]
    )
    cursor.execute('''
        INSERT INTO TreatmentTeam (
            Patient, Doctor, Nurse, Support_Staff, Billing_Office,
            Radiology_Lab_Technician, Pathology_Lab_Technician, Emergency_Contact, Pharmacist, Insurance_Agent
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', team)

# Commit changes and close the connection
conn.commit()
conn.close()

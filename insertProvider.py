import sqlite3

# Connect to the database (this will create the database if it doesn't exist)
conn = sqlite3.connect('TreatmentTeamSample.db')
cursor = conn.cursor()

# Define a SQL command to create the "provider" table if it doesn't exist
create_provider_table_query = '''
CREATE TABLE IF NOT EXISTS provider (
    provider_id TEXT PRIMARY KEY,
    name TEXT,
    date_of_birth TEXT,
    title TEXT,
    phone TEXT,
    email TEXT
);
'''

# Execute the SQL command to create the "provider" table
cursor.execute(create_provider_table_query)

# Define the data to insert into the "provider" table
provider_data = [
    ("PR1001", "Andrew", "DOB11041992", "Doctor", "+14016296781", "andrew@hospital.com"),
    ("PR1002", "Sophia", "DOB12281972", "Doctor", "+16805970987", "sophia@hospital.com"),
    ("PR1003", "Linda", "DOB07011999", "Doctor", "+12522173068", "linda@hospital.com"),
    ("PR1004", "Oscar", "DOB12251998", "Nurse", "+12488860746", "oscar@hospital.com"),
    ("PR1005", "William", "DOB09111990", "Nurse", "+18026758468", "william@hospital.com"),
    ("PR1006", "Damien", "DOB10071980", "Support Staff", "+13194615516", "damien@hospital.com"),
    ("PR1007", "Douglas", "DOB06281992", "Support Staff", "+18597638767", "douglas@hospital.com"),
    ("PR1008", "Robert", "DOB08061982", "Radiology Tech", "+18502557057", "robert@hospital.com"),
    ("PR1009", "Victoria", "DOB12101994", "Pathology Tech", "+12837975034", "victoria@hospital.com"),
    ("PR1010", "James", "DOB02101987", "Billing Officer", "+17712104375", "james@hospital.com"),
]

# Define the SQL command to insert data into the "provider" table
insert_provider_query = '''
INSERT INTO provider (provider_id, name, date_of_birth, title, phone, email)
VALUES (?, ?, ?, ?, ?, ?);
'''

# Execute the SQL command for each set of provider data
for provider in provider_data:
    cursor.execute(insert_provider_query, provider)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Table 'provider' created, and data inserted successfully.")

import sqlite3
import random

# Connect to the database
conn = sqlite3.connect('TreatmentTeamsample.db')
cursor = conn.cursor()

# Delete the existing TreatmentTeam table if it exists
cursor.execute('DROP TABLE IF EXISTS Image')

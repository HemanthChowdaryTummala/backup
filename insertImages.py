import sqlite3
import os

# Connect to the "TreatmentTeamSample" database (or create it if it doesn't exist)
db_connection = sqlite3.connect("TreatmentTeamSample.db")
cursor = db_connection.cursor()

# Create the "Image" table with ID (image name) as text and image data as BLOB
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Image (
        id TEXT PRIMARY KEY,
        image_data BLOB
    )
''')
db_connection.commit()

# Directory containing image files
image_directory = "images"

# Check if the directory exists
if os.path.exists(image_directory):
    for filename in os.listdir(image_directory):
        if filename.endswith((".jpg", ".png")):  # Add more file extensions if needed
            image_file_path = os.path.join(image_directory, filename)
            
            # Check if the image file exists
            if os.path.exists(image_file_path):
                # Read the image file as binary data
                with open(image_file_path, "rb") as image_file:
                    image_data = image_file.read()
                
                # Remove the file extension from the image name
                image_name = os.path.splitext(filename)[0]
                    
                # Insert the image name and image data into the "Image" table
                cursor.execute("INSERT INTO Image (id, image_data) VALUES (?, ?)", (image_name, image_data))
                db_connection.commit()
                
                print(f"Image '{image_name}' inserted into the database.")
            else:
                print(f"Image file '{filename}' does not exist.")
else:
    print("Image directory does not exist.")

# Close the database connection
db_connection.close()

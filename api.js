const express = require('express');
const sqlite3 = require('sqlite3');
const cors = require('cors');
const app = express();
const port = 3000;

// Connect to the SQLite database
const db = new sqlite3.Database('TreatmentTeamSample.db');
app.use(cors());

// Define an endpoint to retrieve patient data by ID
app.get('/patients/:id', (req, res) => {
  const patientId = req.params.id;

  // Query the database to get patient data by ID
  db.get('SELECT * FROM patients WHERE patient_id = ?', [patientId], (err, row) => {
    if (err) {
      console.error(err);
      res.status(500).json({ error: 'Internal server error' });
    } else if (row) {
      res.json(row);
    } else {
      res.status(404).json({ error: 'Patient not found' });
    }
  });
});

app.get('/treatment-team/:id', (req, res) => {
    const teamId = req.params.id;
  
    // Query the database to get treatment team data by ID
    db.get('SELECT * FROM TreatmentTeam WHERE Patient = ?', [teamId], (err, row) => {
      if (err) {
        console.error(err);
        res.status(500).json({ error: 'Internal server error' });
      } else if (row) {
        res.json(row);
      } else {
        res.status(404).json({ error: 'Treatment team not found' });
      }
    });
  });

app.get('/health-records', (req, res) => {
    // Query the database to get all health records
    db.all('SELECT * FROM Health_Records', (err, rows) => {
      if (err) {
        console.error(err);
        res.status(500).json({ error: 'Internal server error' });
      } else {
        res.json(rows);
      }
    });
});
app.get('/informed-consent/:patient', (req, res) => {
    const patient = req.params.patient;
    // Query the database to get all health records
    db.all('SELECT * FROM InformedConsent where ObjectId = ?', [patient] ,(err, rows) => {
      if (err) {
        console.error(err);
        res.status(500).json({ error: 'Internal server error' });
      } else {
        res.json(rows);
      }
    });
});
app.get('/image/:imageId', (req, res) => {
    const imageId = req.params.imageId;
  
    db.get('SELECT image_data FROM Image WHERE id = ?', [imageId], (err, row) => {
      if (err) {
        console.error(err);
        return res.status(500).send('Internal Server Error');
      }
  
      if (row) {
        // Send the image data as a response with the appropriate content type
        res.setHeader('Content-Type', 'image/jpeg'); // Adjust the content type as needed
        res.end(row.image_data, 'binary');
      } else {
        res.status(404).send('Image not found');
      }
    });
});
app.post('/check-login', (req, res) => {
    const { username, password } = req.body;

    if (!username || !password) {
        return res.status(400).json({ error: 'Both username and password are required.' });
    }

    const query = 'SELECT * FROM login WHERE username = ? AND password = ?';

    db.get(query, [username, password], (err, row) => {
        if (err) {
            console.error(err);
            return res.status(500).json({ error: 'Database error' });
        }

        if (row) {
            res.status(200).json({ message: 'Login successful' });
        } else {
            res.status(401).json({ error: 'Invalid username or password' });
        }
    });
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

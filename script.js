
let patientId;

let apiUrl1 ;
let apiUrl2 ;
let apiUrl3 = 'http://localhost:3000/health-records';
let apiUrl4 ;
let apiUrl5 ;
let subject =[];
let object = ["HR1001","HR1002","HR1003","HR1004","HR1005","HR1006","HR1007","HR1008","HR1009","HR1010",];
let patients = ["PT1001","PT1002","PT1003","PT1004","PT1005","PT1006","PT1007","PT1008","PT1009","PT1010",]
let action = ["Read", "Write", "Update"];
let consents = []; 
const tableBody = document.querySelector('#api-data-table tbody');
function fetchAndDisplayPatientData() {
    fetch(apiUrl1)
        .then(response => response.json())
        .then(data => {
            const patientDetailsContainer = document.getElementById('patient-details-container');
            patientDetailsContainer.innerHTML = `
                    <table class="table table-striped table-bordered mt-3">
                    <tr>
                        <th class="bg-info text-white text-center">Information</th>
                        <th class="bg-info text-white text-center">Value</th>
                    </tr>
                    <tr>
                        <th>ID</th>
                        <td>${data.patient_id}</td>
                    </tr>
                    <tr>
                        <th>Name</th>
                        <td>${data.first_name}</td>
                    </tr>
                    <tr>
                        <th>Date of Birth</th>
                        <td>${data.date_of_birth}</td>
                    </tr>
                    <tr>
                        <th>Gender</th>
                        <td>${data.gender}</td>
                    </tr>
                    <tr>
                        <th>Phone</th>
                        <td>${data.phone}</td>
                    </tr>
                    <tr>
                        <th>Email</th>
                        <td>${data.email}</td>
                    </tr>
                </table>
            `;
        })
        .catch(error => {
            console.error('Error fetching patient data:', error);
        });
}
function fetchAndDisplayTreatmentTeamData() {
    fetch(apiUrl2)
        .then(response => response.json())
        .then(data => {
            subject = Object.values(data);
            subject.shift();
            const patientDetailsContainer = document.getElementById('treatment-team-details-container');
            patientDetailsContainer.innerHTML = `
                <table class="table table-striped table-bordered mt-3">
                <tr>
                    <th class="bg-info text-white text-center">Title</th>
                    <th class="bg-info text-white text-center">ID</th>
                </tr>
                    <tr>
                        <th class = "text-center" >Doctor</th>
                        <td class = "text-center">${data.Doctor}</td>
                    </tr>
                    <tr>
                        <th class = "text-center">Nurse</th>
                        <td class = "text-center">${data.Nurse}</td>
                    </tr>
                    <tr>
                        <th class = "text-center">Support Staff</th>
                        <td class = "text-center">${data.Support_Staff}</td>
                    </tr>
                    <tr>
                        <th class = "text-center">Billing Officer</th>
                        <td class = "text-center">${data.Billing_Office}</td>
                    </tr>
                    <tr>
                        <th class = "text-center">Radiology Lab Technician</th>
                        <td class = "text-center">${data.Radiology_Lab_Technician}</td>
                    </tr>
                    <tr>
                        <th class = "text-center">Pathology Lab Technician</th>
                        <td class = "text-center">${data.Pathology_Lab_Technician}</td>
                    </tr>
                    <tr>
                        <th class = "text-center">Emergency Contact</th>
                        <td class = "text-center">${data.Emergency_Contact}</td>
                    </tr>
                    <tr>
                        <th class = "text-center">Pharmacist</th>
                        <td class = "text-center">${data.Pharmacist}</td>
                    </tr>
                    <tr>
                        <th class = "text-center">Insurance Agent</th>
                        <td class = "text-center">${data.Insurance_Agent}</td>
                    </tr>
                </table>
            `;
            populateDropdowns();
        })
        .catch(error => {
            console.error('Error fetching patient data:', error);
        });
}
function fetchAndDisplayHealthRecords() {

    const tbody = document.querySelector("#health-records-table tbody");

    // Function to fetch data and populate the table
    function fetchDataAndPopulateTable() {
        fetch(apiUrl3)
            .then(response => response.json())
            .then(data => {
                // Clear any existing rows in the table
                tbody.innerHTML = "";

                // Loop through the data and create table rows
                data.forEach(record => {
                    const row = document.createElement("tr");
                    row.innerHTML = `
                        <td>${record.RecordID}</td>
                        <td>${record.RecordName}</td>
                        <td>${record.RecordDescription}</td>
                    `;
                    tbody.appendChild(row);
                });
            })
            .catch(error => {
                console.error("Error fetching data from the API:", error);
            });
    }

    // Call the function to fetch data and populate the table
    fetchDataAndPopulateTable();
}
function showLoginForm() {
    document.getElementById("login-form").style.display = "block";
}
document.getElementById("login-button").addEventListener("click", function () {
    // Get patient ID and password from the form
    const enteredPatientId = document.getElementById("patient-id").value;
    const enteredPassword = document.getElementById("password").value;
    
    if ( patients.includes(enteredPatientId) && enteredPatientId == enteredPassword) {
        // Authentication successful
        patientId = enteredPatientId;
        // Hide the login form
        document.getElementById("login-form").style.display = "none";
        patientId = enteredPatientId;
        apiUrl1 = `http://localhost:3000/patients/${patientId}`;
        apiUrl2 = `http://localhost:3000/treatment-team/${patientId}`;
        apiUrl4 = `http://localhost:3000/informed-consent/${patientId}`;
        apiUrl5 = `http://localhost:3000/image/${patientId}`;
        loadContent();
        document.getElementById("photo").style.display = "block";
        document.getElementById("main-body").style.display = "block";
        document.getElementById("login-form").style.display = "none";
    } else {
        const loginAlert = document.getElementById("login-alert");
        loginAlert.style.display = "block";
    }
});
function updateRowIndices() {
    const rows = tableBody.rows;
    for (let index = 0; index < rows.length; index++) {
        const deleteButton = rows[index].querySelector('.delete-button');
        deleteButton.dataset.index = index;
    }
}
function newRow(item,index){
    const newRow = tableBody.insertRow(index);

    // Add cells for Subject, Action, Object, and Delete button
    const subjectCell = newRow.insertCell(0);
    const actionCell = newRow.insertCell(1);
    const objectCell = newRow.insertCell(2);
    const deleteCell = newRow.insertCell(3);

    // Populate the cells with data
    subjectCell.textContent = item.Subject;
    actionCell.textContent = item.Object;
    objectCell.textContent = item.Action;

    // Create a Delete button
    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'Delete';
    deleteButton.className = 'btn btn-danger delete-button';
    deleteButton.addEventListener('click', function () {
        const rowIndex = parseInt(deleteButton.dataset.index, 10);
        // Remove the row when the Delete button is clicked
        tableBody.deleteRow(rowIndex);
        consents.splice(rowIndex, 1);
        // Update row indices
        updateRowIndices();
        setConsentCount();
        console.log(consents)
        // You can also make an API call to delete the item from your server
    });

    deleteCell.appendChild(deleteButton);
}
function fetchAndDisplayConsent() {

    fetch(apiUrl4)
        .then((response) => response.json())
        .then((data) => {
            // Get a reference to the table body

            // Loop through the data and create rows
            data.forEach((item, index) => {
                let uniqueConsent = {
                    Subject: item.Subject,
                    Action: item.Action,
                    Object: item.Object
                }
                consents.push(uniqueConsent);
                newRow(item,index);
            });
            setConsentCount();
        })
        .catch((error) => {
            console.error('Error fetching data:', error);
        });
}
function displayAdd(){
    document.getElementById('add-id').style.display = "block";
}
function removeAdd(){
    document.getElementById('add-id').style.display = "none";   
}
function addDataToTable() {

    const subjectDropdown = document.getElementById('subject-dropdown');
    const actionDropdown = document.getElementById('action-dropdown');
    const objectDropdown = document.getElementById('object-dropdown');
    const tableBody = document.querySelector('#api-data-table tbody');

    // Get selected values from the dropdowns
    const subjectValue = subjectDropdown.value;
    const actionValue = actionDropdown.value;
    const objectValue = objectDropdown.value;

   

    let newConsent = {
        Subject: subjectDropdown.value,
        Action: actionDropdown.value,
        Object: objectDropdown.value
    };
    consents.push(newConsent);
    newRow(newConsent,consents.length-1);
    subjectDropdown.selectedIndex = 0;
    actionDropdown.selectedIndex = 0;
    objectDropdown.selectedIndex = 0;
    console.log(consents);
    removeAdd();
    setConsentCount();
}
function populateDropdowns() {
    const subjectDropdown = document.getElementById('subject-dropdown');
    const actionDropdown = document.getElementById('action-dropdown');
    const objectDropdown = document.getElementById('object-dropdown');

    // Replace these arrays with your actual data
    const subjectOptions = subject;
    const actionOptions = action;
    const objectOptions = object;

    // Populate Subject dropdown
    subjectOptions.forEach((option) => {
        const optionElement = document.createElement('option');
        optionElement.value = option;
        optionElement.textContent = option;
        subjectDropdown.appendChild(optionElement);
    });

    // Populate Action dropdown
    actionOptions.forEach((option) => {
        const optionElement = document.createElement('option');
        optionElement.value = option;
        optionElement.textContent = option;
        actionDropdown.appendChild(optionElement);
    });

    // Populate Object dropdown
    objectOptions.forEach((option) => {
        const optionElement = document.createElement('option');
        optionElement.value = option;
        optionElement.textContent = option;
        objectDropdown.appendChild(optionElement);
    });
}
function fetchAndLoadImage(){
    const img = document.getElementById('image'); // Make sure you have an HTML element with the id "image"
    fetch(apiUrl5)
    .then((response) => {
        if (!response.ok) {
        throw new Error('Network response was not ok');
        }
        return response.blob(); // Get the response body as a Blob
    })
    .then((imageBlob) => {
        // Create an object URL from the Blob
        const imageUrl = URL.createObjectURL(imageBlob);

        // Set the src attribute of the img tag to display the image
        img.src = imageUrl;
    })
    .catch((error) => {
        console.error('Error:', error);
    });

}
function populateConsentModal() {
    // TODO: Replace this with your code to fetch consent data from your data source
    const consentData = consents;

    const consentList = document.getElementById("consentList");

    // Clear any existing consent rows
    consentList.innerHTML = "";

    // Populate the modal with consent data
    consentData.forEach((consent) => {
        const tr = document.createElement("tr");
        const td1 = document.createElement("td");
        const td2 = document.createElement("td");
        const td3 = document.createElement("td");
        td1.textContent = consent['Subject'];
        td2.textContent = consent['Object'];
        td3.textContent = consent['Action'];
        tr.appendChild(td1);
        tr.appendChild(td2);
        tr.appendChild(td3);
        consentList.appendChild(tr);
    });
}
function setConsentCount(){
    document.getElementById("consents-count").innerText = `Number of consents : ${consents.length}`;
}
document.getElementById("accept-consent-button").addEventListener("click", function () {
    populateConsentModal(); // Populate the modal with consent data
    $('#consentModal').modal('show'); // Show the modal
});
function loadContent() {
    fetchAndLoadImage();
    fetchAndDisplayPatientData();
    fetchAndDisplayTreatmentTeamData();
    fetchAndDisplayHealthRecords();
    fetchAndDisplayConsent();
}


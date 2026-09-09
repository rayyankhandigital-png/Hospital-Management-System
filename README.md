# 🏥 Hospital Management System

A simple **Hospital Management System** built with Python using **Tkinter** for the graphical user interface and **JSON** for storing patient records.

This project allows users to easily **add, view, search, update, and delete patient information** through a simple desktop application.

## ✨ Features

* ➕ Add new patients
* 👀 View all patient records
* 🔍 Search patients using Patient ID
* ✏️ Update patient information
* 🗑️ Delete patient records
* 🧹 Clear input fields
* 💾 Automatically save patient data
* 📂 Store records in a JSON file
* ⚠️ Display warning and error messages using message boxes
* 🖥️ Simple and user-friendly Tkinter interface

## 🛠️ Technologies Used

* **Python**
* **Tkinter** – Used to create the graphical user interface
* **MessageBox** – Used to display alerts, warnings, errors, and success messages
* **JSON** – Used to store patient records
* **OS** – Used to check whether the patient data file exists

## 📋 Patient Information

The system stores the following information:

* Patient ID
* Patient Name
* Age
* Gender
* Phone Number
* Disease
* Doctor

## 📁 Project Structure

```text
Hospital-Management-System/
│
├── hospital_management.py
├── patients.json
└── README.md
```

> `patients.json` is automatically created by the program if it does not already exist.

## 🚀 How to Run

### 1. Install Python

Make sure Python is installed on your computer.

You can check by running:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/rayyankhandigital-png/Hospital-Management-System/edit/main/README.md
```

### 3. Open the Project Folder

```bash
cd Hospital-Management-System
```

### 4. Run the Program

```bash
python hospital_management.py
```

The Hospital Management System window will open.

## 🖥️ How It Works

### Add Patient

Enter the patient's information and click **Add Patient**.

The system checks whether the required information is entered and whether the Patient ID already exists. The patient record is then saved to `patients.json`.

### View Patients

Click **View Patients** to display all saved patient records in the application.

### Search Patient

Enter a Patient ID and click **Search Patient**.

If the patient exists, their information will automatically appear in the input fields.

### Update Patient

Enter the Patient ID, edit the required information, and click **Update Patient**.

The updated information will be saved to the JSON file.

### Delete Patient

Enter the Patient ID and click **Delete Patient**.

The system asks for confirmation before deleting the record.

### Clear

The **Clear** button removes all information from the input fields.

## 💾 Data Storage

Patient records are stored locally in a file called:

```text
patients.json
```

The data is stored in JSON format, making it simple to read and manage.

Example:

```json
[
    {
        "id": "P001",
        "name": "Ali",
        "age": "25",
        "gender": "Male",
        "phone": "03001234567",
        "disease": "Flu",
        "doctor": "Dr. Ahmed"
    }
]
```

## 🎯 Project Purpose

The main purpose of this project is to demonstrate how Python can be used to create a simple **GUI-based management system** with data storage.

It is also useful for learning:

* Python functions
* Tkinter GUI development
* JSON file handling
* CRUD operations
* Input validation
* Error handling
* File handling

## 🔄 CRUD Operations

The system supports the basic CRUD operations:

| Operation  | Function            |
| ---------- | ------------------- |
| **Create** | Add Patient         |
| **Read**   | View/Search Patient |
| **Update** | Update Patient      |
| **Delete** | Delete Patient      |

## 👨‍💻 Developer

**Muhammad Rayyan Khan**

## 📄 License

This project is created for **educational and learning purposes**.

## ⭐ Conclusion

This Hospital Management System is a simple Python project that demonstrates how **Tkinter, MessageBox, JSON, and OS** can be combined to create a useful desktop application. I hope you find this project useful and helpful for learning Python GUI development.

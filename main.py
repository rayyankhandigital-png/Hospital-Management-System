import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "patients.json"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as file:
        json.dump([], file)


def load_patients():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


def save_patients(patients):
    with open(FILE_NAME, "w") as file:
        json.dump(patients, file, indent=4)


def clear_fields():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_gender.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_disease.delete(0, tk.END)
    entry_doctor.delete(0, tk.END)


def add_patient():
    patient_id = entry_id.get()
    name = entry_name.get()
    age = entry_age.get()
    gender = entry_gender.get()
    phone = entry_phone.get()
    disease = entry_disease.get()
    doctor = entry_doctor.get()

    if not patient_id or not name or not age or not gender:
        messagebox.showwarning(
            "Missing Information",
            "Please enter Patient ID, Name, Age and Gender."
        )
        return

    patients = load_patients()

    for patient in patients:
        if patient["id"] == patient_id:
            messagebox.showerror(
                "Error",
                "Patient ID already exists."
            )
            return

    patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "gender": gender,
        "phone": phone,
        "disease": disease,
        "doctor": doctor
    }

    patients.append(patient)
    save_patients(patients)

    messagebox.showinfo(
        "Success",
        "Patient added successfully!"
    )

    clear_fields()
    view_patients()


def view_patients():
    patients = load_patients()

    patient_list.delete(0, tk.END)

    for patient in patients:
        data = (
            f'ID: {patient["id"]} | '
            f'Name: {patient["name"]} | '
            f'Age: {patient["age"]} | '
            f'Gender: {patient["gender"]} | '
            f'Phone: {patient["phone"]} | '
            f'Disease: {patient["disease"]} | '
            f'Doctor: {patient["doctor"]}'
        )

        patient_list.insert(tk.END, data)


def search_patient():
    search_id = entry_id.get()

    if not search_id:
        messagebox.showwarning(
            "Search",
            "Enter Patient ID to search."
        )
        return

    patients = load_patients()

    for patient in patients:
        if patient["id"] == search_id:

            clear_fields()

            entry_id.insert(0, patient["id"])
            entry_name.insert(0, patient["name"])
            entry_age.insert(0, patient["age"])
            entry_gender.insert(0, patient["gender"])
            entry_phone.insert(0, patient["phone"])
            entry_disease.insert(0, patient["disease"])
            entry_doctor.insert(0, patient["doctor"])

            messagebox.showinfo(
                "Found",
                "Patient found successfully!"
            )
            return

    messagebox.showerror(
        "Not Found",
        "Patient not found."
    )


def update_patient():
    patient_id = entry_id.get()

    if not patient_id:
        messagebox.showwarning(
            "Update",
            "Enter Patient ID."
        )
        return

    patients = load_patients()

    for patient in patients:
        if patient["id"] == patient_id:

            patient["name"] = entry_name.get()
            patient["age"] = entry_age.get()
            patient["gender"] = entry_gender.get()
            patient["phone"] = entry_phone.get()
            patient["disease"] = entry_disease.get()
            patient["doctor"] = entry_doctor.get()

            save_patients(patients)

            messagebox.showinfo(
                "Success",
                "Patient information updated!"
            )

            view_patients()
            return

    messagebox.showerror(
        "Error",
        "Patient not found."
    )


def delete_patient():
    patient_id = entry_id.get()

    if not patient_id:
        messagebox.showwarning(
            "Delete",
            "Enter Patient ID."
        )
        return

    patients = load_patients()

    for patient in patients:
        if patient["id"] == patient_id:

            confirm = messagebox.askyesno(
                "Confirm Delete",
                "Are you sure you want to delete this patient?"
            )

            if confirm:
                patients.remove(patient)
                save_patients(patients)

                messagebox.showinfo(
                    "Deleted",
                    "Patient deleted successfully!"
                )

                clear_fields()
                view_patients()

            return

    messagebox.showerror(
        "Error",
        "Patient not found."
    )


root = tk.Tk()
root.title("Hospital Management System")
root.geometry("1000x650")
root.resizable(False, False)

title = tk.Label(
    root,
    text="HOSPITAL MANAGEMENT SYSTEM",
    font=("Arial", 24, "bold")
)

title.pack(pady=15)


input_frame = tk.Frame(root)
input_frame.pack(pady=10)


# Patient ID
tk.Label(
    input_frame,
    text="Patient ID:",
    font=("Arial", 12)
).grid(row=0, column=0, padx=10, pady=8)

entry_id = tk.Entry(
    input_frame,
    width=25
)
entry_id.grid(row=0, column=1, padx=10)


# Name
tk.Label(
    input_frame,
    text="Name:",
    font=("Arial", 12)
).grid(row=0, column=2, padx=10)

entry_name = tk.Entry(
    input_frame,
    width=25
)
entry_name.grid(row=0, column=3, padx=10)


# Age
tk.Label(
    input_frame,
    text="Age:",
    font=("Arial", 12)
).grid(row=1, column=0, padx=10, pady=8)

entry_age = tk.Entry(
    input_frame,
    width=25
)
entry_age.grid(row=1, column=1, padx=10)


# Gender
tk.Label(
    input_frame,
    text="Gender:",
    font=("Arial", 12)
).grid(row=1, column=2, padx=10)

entry_gender = tk.Entry(
    input_frame,
    width=25
)
entry_gender.grid(row=1, column=3, padx=10)


# Phone
tk.Label(
    input_frame,
    text="Phone:",
    font=("Arial", 12)
).grid(row=2, column=0, padx=10, pady=8)

entry_phone = tk.Entry(
    input_frame,
    width=25
)
entry_phone.grid(row=2, column=1, padx=10)


# Disease
tk.Label(
    input_frame,
    text="Disease:",
    font=("Arial", 12)
).grid(row=2, column=2, padx=10)

entry_disease = tk.Entry(
    input_frame,
    width=25
)
entry_disease.grid(row=2, column=3, padx=10)


# Doctor
tk.Label(
    input_frame,
    text="Doctor:",
    font=("Arial", 12)
).grid(row=3, column=0, padx=10, pady=8)

entry_doctor = tk.Entry(
    input_frame,
    width=25
)
entry_doctor.grid(row=3, column=1, padx=10)



button_frame = tk.Frame(root)
button_frame.pack(pady=15)

tk.Button(
    button_frame,
    text="Add Patient",
    width=15,
    command=add_patient
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="View Patients",
    width=15,
    command=view_patients
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="Search Patient",
    width=15,
    command=search_patient
).grid(row=0, column=2, padx=5)

tk.Button(
    button_frame,
    text="Update Patient",
    width=15,
    command=update_patient
).grid(row=0, column=3, padx=5)

tk.Button(
    button_frame,
    text="Delete Patient",
    width=15,
    command=delete_patient
).grid(row=0, column=4, padx=5)

tk.Button(
    button_frame,
    text="Clear",
    width=15,
    command=clear_fields
).grid(row=0, column=5, padx=5)


tk.Label(
    root,
    text="Patient Records",
    font=("Arial", 16, "bold")
).pack(pady=5)

list_frame = tk.Frame(root)
list_frame.pack(pady=5)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

patient_list = tk.Listbox(
    list_frame,
    width=125,
    height=15,
    yscrollcommand=scrollbar.set,
    font=("Arial", 10)
)

patient_list.pack(side=tk.LEFT)

scrollbar.config(command=patient_list.yview)

view_patients()

root.mainloop()

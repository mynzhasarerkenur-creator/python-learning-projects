import json

class Patient:
    def __init__(self, name, temp):
        self.name = name
        self.temp = temp

    def show_patients(self):
        print(f"name: {self.name} temp: {self.temp}")

    def to_dict(self):
        return {"name": self.name, "temp": self.temp}


patients = []
try:
    with open("mini_patients.json", "r") as files:
            patients_data = json.load(files)
            for data in patients_data:
                patients.append(Patient(data["name"], data["temp"]))
except FileNotFoundError:
    patients_data = []

while True:
    print("1 - добавить пациента")
    print("2 - показать пациентов")
    print("3 - выйти")

    choise = input("выбор: ")

    if choise == "1":
        name = input("name: ")
        temp = float(input("temp: "))
        patients.append(Patient(name, temp))

    elif choise == "2":
        if len(patients) < 1:
            print("Now patients")
        else:
            for patient in patients:
                patient.show_patients()

    elif choise == "3":
        patients_data = []
        for patient in patients:
            patients_data.append(patient.to_dict())
        with open("mini_patients.json", "w") as files:
            json.dump(patients_data, files, indent= 4)
        break


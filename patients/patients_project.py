import json


class Patient:
    def __init__(self, name, temp):
        self.name = name
        self.temp = temp

    def show_info(self):
        print(f"name: {self.name}, temp: {self.temp}")

    def check_temp(self):
        if self.temp > 37:
            print("Высокая температура")
        else:
            print("Норма")

    def extra_info(self):
        print("Нет доп информации")

    def to_dict(self):
        return {"name": self.name, "temp": self.temp}


class VipPatient(Patient):
    def __init__(self, name, temp, vip_level):
        super().__init__(name, temp)
        self.vip_level = vip_level

    def extra_info(self):
        print(f"{self.name}'s VIP level: {self.vip_level}")


class ChildPatient(Patient):
    def __init__(self, name, temp, parent_name):
        super().__init__(name, temp)
        self.parent_name = parent_name

    def extra_info(self):
        print(f"{self.name}'s parent is {self.parent_name}")


class EmergencyPatient(Patient):
    def __init__(self, name, temp, priority):
        super().__init__(name, temp)
        self.priority = priority

    def extra_info(self):
        print(f"priority: {self.priority}")


try:
    with open("patients.json", "r") as files:
        patients_data = json.load(files)
except FileNotFoundError, json.JSONDecodeError:
    patients_data = []

patients = []

for patient in patients_data:
    patients.append(Patient(patient["name"], patient["temp"]))
p1 = Patient("Ali", 38.5)
print("test to_dict2", p1.to_dict())

while True:
    try:
        print("1 - добавить пациента")
        print("2 - показать всех")
        print("3 - выйти")

        choice = input("выбор: ")

        if choice == "1":
            name = input("Имя: ")
            temp = float(input("Температура: "))
            patient_type = input(
                "Тип:\n"
                "1 - обычный\n"
                "2 - vip\n"
                "3 - child\n"
                "4 - emergency\n"
                "Выбор: "
            )
            if patient_type == "1":
                patients.append(Patient(name, temp))
                print("Пациент успешно добавлен")
            elif patient_type == "2":
                vip_level = input(
                    "VIP level: \n"
                    "1 - Gold\n"
                    "2 - Platinum\n"
                    "3 - Dimond\n"
                    "Выбор: "
                )

                if vip_level == "1":
                    vip_level = "Gold"
                    patients.append(VipPatient(name, temp, vip_level))
                    print("Пациент успешно добавлен")
                elif vip_level == "2":
                    vip_level = "Platinum"
                    patients.append(VipPatient(name, temp, vip_level))
                    print("Пациент успешно добавлен")
                elif vip_level == "3":
                    vip_level = "Dimond"
                    patients.append(VipPatient(name, temp, vip_level))
                    print("Пациент успешно добавлен")
                else:
                    print("Неверный выбор")
            elif patient_type == "3":
                parent_name = input("parent: ")
                patients.append(ChildPatient(name, temp, parent_name))
                print("Пациент успешно добавлен")
            elif patient_type == "4":
                priority = input(
                    "priority:\n" "1 - LOW\n " "2 - MEDIUM\n" "3 - HIGH\n" "выбор: "
                )
                if priority == "1":
                    priority = "LOW"
                    patients.append(EmergencyPatient(name, temp, priority))
                    print("Пациент успешно добавлен")
                elif priority == "2":
                    priority = "MEDIUM"
                    patients.append(EmergencyPatient(name, temp, priority))
                    print("Пациент успешно добавлен")
                elif priority == "3":
                    priority = "HIGH"
                    patients.append(EmergencyPatient(name, temp, priority))
                    print("Пациент успешно добавлен")
                else:
                    print("Неверный выбор")

        elif choice == "2":
            if not patients:
                print("Список пациентов еще пуст")
            else:
                for patient in patients:
                    patient.show_info()
                    patient.check_temp()
                    patient.extra_info()
                    print()
        
        
        elif choice == "3":
            break
    except ValueError:
        print("Температура должна быть числом")

print(patients_data)

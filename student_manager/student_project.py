import json


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_student(self):
        print(f"студент: {self.name}")
        print(f"возраст: {self.age}")
        print()

    def to_dict(self):
        return {"name": self.name, "age": self.age}

def load_student():
        students = []
        try:
            with open("student_manager/student.json", "r") as files:
                students_data = json.load(files)
            for data in students_data:
                students.append(Student(data["name"], data["age"]))
        except (FileNotFoundError, json.JSONDecodeError):
            students = []
        return students

students = load_student()

def save_student():
    students_data = []
    for student in students:
        students_data.append(student.to_dict())
    with open('student_manager/student.json', 'w') as files:
        json.dump(students_data,files, indent = 4) 

while True:
    print(
    '1 - добавить студента\n' 
    '2 - показать студентов\n' 
    '3 - найти студента\n' 
    '4 - удалить студента\n' 
    '5 - выйти'
    )
    choise = input('выбор:')

    if choise =='1':
        name = input('Имя студента: ')
        age = int(input('возраст студента: '))
        students.append(Student(name,age))
        print('Студент успешно добавлен!')
    elif choise =='2':
        if len(students) == 0:
            print('сначало добавьте студентов')
            print()
        else:
            for student in students:
                student.show_student()
    elif choise =='3':
        search = input('введите имя студента: ')
        print()
        found = False
        for student in students:
            if search.lower() in student.name.lower():
                student.show_student()
                found = True
        if found == False:
            print('Студент таким именем не зарегестрирован')
            print()
    elif choise =='4':
        for num,student in enumerate(students, start = 1):
            print(f'{num}. ', end = '')
            student.show_student()
        num_input = int(input('напишите номер студента: '))
        index = num_input - 1
        try:
            del students[index]
            print('студент удалено из базы')
        except IndexError:
            print('Неверный номер студента')
    elif choise =='5':
        save_student()         
        break
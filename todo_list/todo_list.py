import json


class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done

    def show_tasks(self):
        done = self.done
        task_status = "выполнен" if done == True else "не выполнен"
        print(f"{self.title} - {task_status}")

    def to_dict(self):
        return {"title": self.title, "done": self.done}


tasks = []

try:
    with open("todo_list/todo.json", "r") as files:
        task_data = json.load(files)
        for data in task_data:
            tasks.append(Task(data["title"], data["done"]))
except FileNotFoundError, json.JSONDecodeError:
    task_data = []

while True:
    print("1 - добавить задачу")
    print("2 - показать задачи")
    print("3 - отметить выполненной")
    print("4 - выйти")

    choise = input("выбор: ")

    if choise == "1":

        title = input("задача: ")
        tasks.append(Task(title))
        print('Задача добавлено ')
        print()

    elif choise == "2":
        if not tasks:
            print("No tasks")
            print()
        else:
            for num, task in enumerate(tasks, start=1):
                print(f"{num}. ", end="")
                task.show_tasks()
    elif choise == "3":
        for num, task in enumerate(tasks, start=1):
            print(f"{num}. ", end="")
            task.show_tasks()
        num_input = int(input("выберите задачу по номеру: "))
        index = num_input - 1
        tasks[index].done = True
    elif choise == "4":
        task_data = []
        for task in tasks:
            task_data.append(task.to_dict())
        with open('todo_list/todo.json', 'w') as files:
            json.dump(task_data, files, indent = 4)
        break

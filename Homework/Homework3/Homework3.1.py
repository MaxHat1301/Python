class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def str(self):
        status = "Виконано" if self.completed else "Не виконано"
        return (f"Назва: {self.title}\n"
                f"Опис: {self.description}\n"
                f"Дедлайн: {self.deadline}\n"
                f"Стан: {status}")

class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]
    def mark_task_as_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_as_completed()
                break

    def display_tasks(self):
        if not self.tasks:
            print("Список завдань порожній.")
        else:
            for idx, task in enumerate(self.tasks, 1):
                print(f"\nЗавдання #{idx}")
                print(task)
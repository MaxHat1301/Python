class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def str(self):
        status = "Виконано" if self.completed else "Не виконано"
        return f"{self.title} - {self.description} (Дедлайн: {self.deadline}, Стан: {status})"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()

    def show_tasks(self):
        if not self.tasks:
            print("Завдань немає.")
        else:
            for task in self.tasks:
                print(task)
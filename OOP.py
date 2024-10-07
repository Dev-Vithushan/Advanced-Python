import os
import json
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def complete_task(self):
        self.completed = True

    def __repr__(self):
        return f"{self.title} | Due: {self.due_date} | Completed: {self.completed}"

class TaskManager:
    def __init__(self, task_file='tasks.json'):
        self.task_file = task_file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.task_file):
            with open(self.task_file, 'r') as file:
                return [Task(**task) for task in json.load(file)]
        return []

    def save_tasks(self):
        with open(self.task_file, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def add_task(self, title, description, due_date):
        task = Task(title, description, due_date)
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task_title):
        self.tasks = [task for task in self.tasks if task.title != task_title]
        self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for task in self.tasks:
            print(task)

    def mark_task_completed(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                task.complete_task()
                self.save_tasks()
                return
        print(f"Task '{task_title}' not found.")

def main():
    manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter task due date (YYYY-MM-DD): ")

            try:
                datetime.strptime(due_date, '%Y-%m-%d')
                manager.add_task(title, description, due_date)
                print("Task added successfully.")
            except ValueError:
                print("Invalid date format. Please enter date as YYYY-MM-DD.")

        elif choice == '2':
            manager.view_tasks()

        elif choice == '3':
            task_title = input("Enter the title of the task to remove: ")
            manager.remove_task(task_title)
            print(f"Task '{task_title}' removed.")

        elif choice == '4':
            task_title = input("Enter the title of the task to mark as completed: ")
            manager.mark_task_completed(task_title)

        elif choice == '5':
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid option. Please choose a valid action.")

if __name__ == '__main__':
    main()

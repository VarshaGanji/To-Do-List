import os

class ToDoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{idx}. {task['task']} - {status}")

    def update_task(self, task_number, new_task):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["task"] = new_task
            print(f"Task {task_number} updated to '{new_task}'.")
        else:
            print("Invalid task number.")

    def complete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            deleted_task = self.tasks.pop(task_number - 1)
            print(f"Task '{deleted_task['task']}' deleted.")
        else:
            print("Invalid task number.")

    def run(self):
        while True:
            print("\nTo-Do List Menu:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Update Task")
            print("4. Complete Task")
            print("5. Delete Task")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                task = input("Enter the task: ")
                self.add_task(task)
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                task_number = int(input("Enter the task number to update: "))
                new_task = input("Enter the new task: ")
                self.update_task(task_number, new_task)
            elif choice == '4':
                task_number = int(input("Enter the task number to mark as complete: "))
                self.complete_task(task_number)
            elif choice == '5':
                task_number = int(input("Enter the task number to delete: "))
                self.delete_task(task_number)
            elif choice == '6':
                print("Exiting the to-do app. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = ToDoApp()
    app.run()

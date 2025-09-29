class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        print("\n--- To-Do List ---")
        for i, task_item in enumerate(self.tasks, 1):
            status = "✓" if task_item["completed"] else " "
            print(f"{i}. [{status}] {task_item['task']}")
        print("------------------")

    def mark_task_as_done(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as done.")
        else:
            print("Invalid task number.")

    def remove_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' removed.")
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n===== To-Do List Manager =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            try:
                task_num = int(input("Enter the task number to mark as done: "))
                todo_list.mark_task_as_done(task_num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            try:
                task_num = int(input("Enter the task number to remove: "))
                todo_list.remove_task(task_num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            print("Exiting To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
import datetime

from app.task import Task
from app.to_do_list import ToDoList


def parse_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD format.")
        return None

def add_task_cli(todo_list):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date_str = input("Enter task due date (YYYY-MM-DD): ")
    due_date = parse_date(due_date_str)
    priority = input("Enter task priority (Low, Medium, High): ")

    task = Task(title, description, due_date, priority)
    todo_list.add_task(task)
    print("Task added successfully.")

def remove_task_cli(todo_list):
    task_index = int(input("Enter the index of the task to remove: "))
    if 0 <= task_index < len(todo_list.tasks):
        todo_list.remove_task(todo_list.tasks[task_index])
        print("Task removed successfully.")
    else:
        print("Invalid task index.")

def mark_task_as_completed_cli(todo_list):
    task_index = int(input("Enter the index of the task to mark as completed: "))
    if 0 <= task_index < len(todo_list.tasks):
        todo_list.mark_task_as_completed(todo_list.tasks[task_index])
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

def display_tasks_cli(todo_list):
    print("\nAll tasks:")
    for i, task in enumerate(todo_list.tasks):
        print(f"{i}. {task}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List App")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_task_cli(todo_list)
        elif choice == 2:
            display_tasks_cli(todo_list)
            remove_task_cli(todo_list)
        elif choice == 3:
            display_tasks_cli(todo_list)
            mark_task_as_completed_cli(todo_list)
        elif choice == 4:
            display_tasks_cli(todo_list)
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
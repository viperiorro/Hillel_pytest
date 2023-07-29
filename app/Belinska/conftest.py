import pytest

from app.task import Task

from app.to_do_list import ToDoList


@pytest.fixture
def general_task(task_data):
    task = Task(title=task_data["title"], description=task_data["description"],
                due_date=task_data["due_date"], priority=task_data["priority"])
    return task


@pytest.fixture
def specific_task(task_data):
    task = Task(title=task_data["title"], description=task_data["description"],
                due_date=task_data["due_date"], priority=task_data["priority"])
    return task


@pytest.fixture
def empty_todo_list():
    return ToDoList()


@pytest.fixture
def todo_list_with_tasks():
    todo_list = ToDoList()
    task1 = Task("Task 1", "This is task 1", "28.07.2023", "Low")
    task2 = Task("Task 2", "This is task 2", "29.07.2023", "High")
    todo_list.add_task(task1)
    todo_list.add_task(task2)
    return todo_list


@pytest.fixture
def task1():
    return Task("Task 1", "This is task 1", "28.07.2023", "Low")


@pytest.fixture
def task2():
    return Task("Task 2", "This is task 2", "29.07.2023", "High")

import pytest

from app.task import Task

from app.to_do_list import ToDoList


@pytest.fixture
def general_task():
    title = "General Task"
    description = "This is a General task"
    due_date = "28.07.2023"
    priority = "Low"
    task = Task(title, description, due_date, priority)
    return task


@pytest.fixture(scope="class")
def completed_task():
    task = Task(title="Completed Task", description="This task is completed", due_date="30.07.2023",
                priority="Low")
    return task


@pytest.fixture
def empty_todo_list():
    return ToDoList()


@pytest.fixture
def todo_list_with_tasks(task1, task2):
    todo_list = ToDoList()
    todo_list.add_task(task1)
    todo_list.add_task(task2)
    return todo_list


@pytest.fixture
def task1():
    return Task("Task 1", "This is task 1", "28.07.2023", "Low")


@pytest.fixture
def task2():
    return Task("Task 2", "This is task 2", "29.07.2023", "High")

import pytest

from app.task import Task
from app.to_do_list import ToDoList


@pytest.fixture()
def task_main():
    return Task("Test", "Create test", "2023-07-30", "High")


@pytest.fixture(scope="class")
def task_completed():
    return Task("Test completed", "Description: completed", "2023-08-28", "Low")


@pytest.fixture()
def create_to_do_list():
    return ToDoList()


@pytest.fixture()
def create_to_do_list_with_task(task1, task2):
    to_do_list = ToDoList()
    to_do_list.add_task(task1)
    to_do_list.add_task(task2)
    return to_do_list


@pytest.fixture()
def task1():
    return Task("Task 1", "Description: first task", "2023-08-28", "Low")


@pytest.fixture()
def task2():
    return Task("Task 2", "Description: second task", "2023-07-31", "High")

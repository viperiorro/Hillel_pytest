import pytest

from app.task import Task
from app.to_do_list import ToDoList


@pytest.fixture()
def task_object():
    return Task("Test", "Create test", "2023-07-30", "High")

@pytest.fixture()
def task_object2():
    return Task("Test2", "Create test2", "2023-08-25", "Low")


@pytest.fixture()
def create_to_do_list():
    return ToDoList()

@pytest.fixture()
def create_to_do_list_with_task(create_to_do_list, task_object):
    create_to_do_list.add_task(task_object)
    return create_to_do_list



import pytest
from app.task import Task
from app.to_do_list import ToDoList


@pytest.fixture(scope="function")
def new_task():
    return Task("Test Task", "Description for testing")


@pytest.fixture(scope="function")
def new_todo_list():
    return ToDoList()

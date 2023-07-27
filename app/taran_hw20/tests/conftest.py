import pytest
from app.task import Task
from app.to_do_list import ToDoList


@pytest.fixture()
def create_task():
    title = "test1"
    description = "test description"
    due_date = "2023-07-26"
    priority = "low"
    return Task(title, description, due_date, priority)


@pytest.fixture(scope="module")
def create_to_do_list():
    return ToDoList()


@pytest.fixture(scope="module")
def create_task_for_to_do_list():
    title = "test1"
    description = "test description"
    due_date = "2023-07-26"
    priority = "low"
    return Task(title, description, due_date, priority)


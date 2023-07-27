import pytest
from app.to_do_list import ToDoList
from app.task import Task


@pytest.fixture(scope="class")
def task_object():
    return Task("test title", "test description", "2023-07-24", "Low")


@pytest.fixture
def to_do_list_ob():
    return ToDoList()

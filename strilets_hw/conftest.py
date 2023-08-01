import pytest

from app.task import Task
from app.to_do_list import ToDoList


@pytest.fixture
def sample_task():
    title = "Title"
    description = "Description"
    due_date = "2023-08-01"
    priority = "High"
    return Task(title, description, due_date, priority)


@pytest.fixture
def test_data():
    return {
        "title": "Title",
        "description": "Description",
        "due_date": "2023-07-30",
        "priority": "Low",
    }


@pytest.fixture
def sample_to_do_list():
    return ToDoList()


@pytest.fixture
def capsys(capsys):
    return capsys

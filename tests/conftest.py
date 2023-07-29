import pytest
from app.to_do_list import ToDoList


@pytest.fixture(scope="function")
def todo_list_object():
    yield ToDoList()
    ToDoList().tasks.clear()


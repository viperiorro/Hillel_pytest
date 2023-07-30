import pytest

from app.task import Task
from app.to_do_list import ToDoList


@pytest.fixture(scope="module")
def task_object():
    return Task(
        title="Title_01",
        description="Description_01",
        due_date="2023-07-30",
        priority="Medium",
    )


@pytest.fixture()
def task_object_1():
    return Task(
        title="Title_02", description="Description_02", due_date=None, priority="Low"
    )


@pytest.fixture()
def to_do_list_empty_object():
    return ToDoList()


@pytest.fixture()
def to_do_list_tasks(to_do_list_empty_object):
    return to_do_list_empty_object.tasks


@pytest.fixture()
def to_do_list_obj_with_tasks(to_do_list_empty_object, task_object, task_object_1):
    to_do_list_empty_object.add_task(task_object)
    to_do_list_empty_object.add_task(task_object_1)
    return to_do_list_empty_object

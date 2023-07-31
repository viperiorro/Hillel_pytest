import pytest

from app.task import Task

@pytest.fixture(scope='module')
def task_main():
    task = Task("Title", "Description", "2023-07-31", "High")
    return task

@pytest.mark.task
def test_task_mark_as_completed(task_main):
    task_main = Task("Title", "Description", "2023-07-31", "High")  # Create a new instance for the test
    assert not task_main.completed
    task_main.mark_as_completed()
    assert task_main.completed

@pytest.mark.task
def test_task_str_representation(task_main):
    task_main = Task("Title", "Description", "2023-07-31", "High")
    expected_str = "Title - Description - Due: 2023-07-31 - Priority: High - Completed: False"
    assert str(task_main) == expected_str

@pytest.mark.task
def test_task_initial_completed_state(task_main):
    assert not task_main.completed

import pytest

from app.task import Task


@pytest.mark.priority_low
@pytest.mark.parametrize("task_data", [
    {"title": "Task 1", "description": "Description 1", "due_date": "28.07.2023", "priority": "Low"},
    {"title": "Task 2", "description": "Description 2", "due_date": "29.07.2023", "priority": "Low"},
    {"title": "Task 3", "description": "Description 3", "due_date": "30.07.2023", "priority": "Low"},
])
def test_task_low_specification(general_task, task_data):
    assert general_task.title == task_data["title"]
    assert general_task.description == task_data["description"]
    assert general_task.due_date == task_data["due_date"]
    assert general_task.priority == task_data["priority"]
    assert not general_task.completed


@pytest.mark.priority_high
def test_task_high_specification(specific_task):
    assert specific_task.title == "Specific Task Title"
    assert specific_task.description == "This is a Specific task description"
    assert specific_task.due_date == "29.07.2023"
    assert specific_task.priority == "High"
    assert not specific_task.completed


def test_mark_as_completed(completed_task):
    assert not completed_task.completed
    completed_task.mark_as_completed()
    assert completed_task.completed


def test_task_str(general_task):
    expected_str = "General Task - This is a General task - Due: 28.07.2023 - Priority: Low - Completed: True"
    assert str(general_task) == expected_str


@pytest.mark.xfail(reason="The medium task is not implemented yet")
def test_incomplete_task():
    task = Task(title="Medium Task", description="This task should not be completed")
    assert not task.completed


@pytest.mark.skip(reason="Skipping this test for now")
def test_skipped_task():
    task = Task(title="Skipped Task", description="This task should not be executed")
    assert not task.completed

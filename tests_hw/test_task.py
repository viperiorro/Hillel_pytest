import pytest
from app.task import Task


@pytest.mark.completed
def test_mark_as_completed(new_task):
    new_task.mark_as_completed()
    assert new_task.completed == True


def test_task_str_representation(new_task):
    expected_str = "Test Task - Description for testing - Due: None - Priority: None - Completed: False"
    assert str(new_task) == expected_str


@pytest.mark.initialization
def test_task_initialization():
    title = "Test Task"
    description = "Description for testing"
    due_date = "2023-08-31"
    priority = "High"

    new_task = Task(title, description, due_date, priority)

    assert new_task.title == title
    assert new_task.description == description
    assert new_task.due_date == due_date
    assert new_task.priority == priority
    assert new_task.completed == False

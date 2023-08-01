import pytest
from app.task import Task


@pytest.mark.task_test
def test_task_init(sample_task, test_data):
    task = Task(**test_data)

    assert task.title == test_data["title"]
    assert task.description == test_data["description"]
    assert task.due_date == test_data["due_date"]
    assert task.priority == test_data["priority"]
    assert not task.completed


@pytest.mark.task_test
def test_mark_task_as_completed(sample_task):
    sample_task.mark_as_completed()
    assert sample_task.completed


@pytest.mark.task_test
def test_task_str(sample_task):
    expected_str = "Title - Description - Due: 2023-08-01 - Priority: High - Completed: False"
    assert str(sample_task) == expected_str


@pytest.mark.skip(reason="Skipping this test for now - Pending implementation of the attribute.")
def test_skip(sample_task):
    assigned_to = "Tim Cook"
    sample_task.assigned_to = assigned_to

    assert sample_task.assigned_to == assigned_to


@pytest.mark.xfail(reason="Expected to fail - More attributes need to be implemented.")
def test_xfail(sample_task):
    progress = 50
    sample_task.progress = progress

    assert sample_task.progress == progress

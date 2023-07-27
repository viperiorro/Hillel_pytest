import pytest
from app.task import Task


@pytest.mark.task_suite
@pytest.mark.parametrize("title, description, date, priority, expected_result",
                         [("title1", "desc1", "1111-11-11", "low",
                           ["title1", "desc1", "1111-11-11", "low", False])])
def test_task_initialization(title, description, date, priority, expected_result):
    task = Task(title, description, date, priority)
    assert task.title == expected_result[0]
    assert task.description == expected_result[1]
    assert task.due_date == expected_result[2]
    assert task.priority == expected_result[3]
    assert task.completed == expected_result[4]


@pytest.mark.task_suite
@pytest.mark.xfail
@pytest.mark.parametrize("description", [("desc1")])
def test_task_initialization_without_title(description):
    task = Task(description=description)
    assert 0


@pytest.mark.task_suite
@pytest.mark.xfail
@pytest.mark.parametrize("title", [("title1")])
def test_task_initialization_without_description(title):
    task = Task(title=title)
    assert 0


@pytest.mark.task_suite
@pytest.mark.parametrize("title, description, expected_result",
                         [("title1", "desc1",
                           ["title1", "desc1", None, None, False])])
def test_task_initialization_with_required_parameters(title, description, expected_result):
    task = Task(title, description)
    assert task.title == expected_result[0]
    assert task.description == expected_result[1]
    assert task.due_date == expected_result[2]
    assert task.priority == expected_result[3]
    assert task.completed == expected_result[4]


@pytest.mark.task_suite
def test_marked_task(create_task):
    create_task.mark_as_completed()
    assert create_task.completed == True


@pytest.mark.task_suite
@pytest.mark.skip("Test skip")
def test_skip_marked_task(create_task):
    create_task.mark_as_completed()
    assert create_task.completed == True


@pytest.mark.task_suite
def test_str_method(create_task):
    result = create_task.__str__()
    expected_result = "test1 - test description - Due: 2023-07-26 - Priority: low - Completed: False"
    assert result == expected_result

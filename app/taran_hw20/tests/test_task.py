import pytest
from app.task import Task


@pytest.mark.task_suite
@pytest.mark.xfail
@pytest.mark.parametrize(
    "params, expected_result",
    [
        (
            {
                "title": "title1",
                "description": "desc1",
                "due_date": "1111-11-11",
                "priority": "low",
            },
            {
                "title": "title1",
                "description": "desc1",
                "due_date": "1111-11-11",
                "priority": "low",
                "completed": False,
            },
        ),
        (
            {"title": "title2", "description": "desc2"},
            {
                "title": "title2",
                "description": "desc2",
                "due_date": None,
                "priority": None,
                "completed": False,
            },
        ),
        ({"title": "title3"}, None),
        ({"description": "desc4"}, None),
    ],
)
def test_task_initialization(params, expected_result):
    args = []
    for key, value in params.items():
        args.append(value)
    task = Task(*args)
    assert task.title == expected_result["title"]
    assert task.description == expected_result["description"]
    assert task.due_date == expected_result["due_date"]
    assert task.priority == expected_result["priority"]
    assert task.completed == expected_result["completed"]


@pytest.mark.task_suite
def test_marked_task(create_task):
    create_task.mark_as_completed()
    assert create_task.completed


@pytest.mark.task_suite
@pytest.mark.skip("Test skip")
def test_skip_marked_task(create_task):
    create_task.mark_as_completed()
    assert create_task.completed


@pytest.mark.task_suite
def test_str_method(create_task):
    result = create_task.__str__()
    expected_result = (
        "test1 - test description - Due: 2023-07-26 - Priority: low - Completed: False"
    )
    assert result == expected_result

import pytest


from app.task import Task


@pytest.mark.task_suite
@pytest.mark.init_suite
def test_init_task():
    actual_result = Task(title="Title_01", description="Description_01")
    expected_result = {
        "title": "Title_01",
        "description": "Description_01",
        "due_date": None,
        "priority": None,
        "completed": False,
    }
    assert actual_result.title == expected_result["title"]
    assert actual_result.description == expected_result["description"]
    assert actual_result.due_date == expected_result["due_date"]
    assert actual_result.priority == expected_result["priority"]
    assert actual_result.completed == expected_result["completed"]


@pytest.mark.task_suite
@pytest.mark.init_suite
@pytest.mark.parametrize(
    "title, description, due_date, priority, expected_result",
    [
        (
            "Title_01",
            "Description_01",
            "2023-07-29",
            "Medium",
            {
                "title": "Title_01",
                "description": "Description_01",
                "due_date": "2023-07-29",
                "priority": "Medium",
                "completed": False,
            },
        ),
        (
            "Title_02",
            "Description_02",
            "2023-07-30",
            "Low",
            {
                "title": "Title_02",
                "description": "Description_02",
                "due_date": "2023-07-30",
                "priority": "Low",
                "completed": False,
            },
        ),
        (
            "Title_03",
            "Description_03",
            "2023-07-28",
            "High",
            {
                "title": "Title_03",
                "description": "Description_03",
                "due_date": "2023-07-28",
                "priority": "High",
                "completed": False,
            },
        ),
    ],
)
def test_init_different_tasks(title, description, due_date, priority, expected_result):
    actual_result = Task(title, description, due_date, priority)
    assert actual_result.title == expected_result["title"]
    assert actual_result.description == expected_result["description"]
    assert actual_result.due_date == expected_result["due_date"]
    assert actual_result.priority == expected_result["priority"]
    assert actual_result.completed == expected_result["completed"]


@pytest.mark.task_suite
@pytest.mark.skip(
    "'completed' is defined in method and is not passed as a parameter when creating an object"
)
def test_mark_as_completed(task_object):
    task_object.mark_as_completed()
    assert task_object.completed


@pytest.mark.task_suite
def test_str_completed(task_object):
    task_object.mark_as_completed()
    actual_result = task_object.__str__()
    expected_result = "Title_01 - Description_01 - Due: 2023-07-30 - Priority: Medium - Completed: True"

    assert actual_result == expected_result


@pytest.mark.task_suite
@pytest.mark.init_suite
@pytest.mark.xfail(reason="Unable initialization of object without Title")
def test_init_without_title():
    Task(description="Description_01")

    assert 0


@pytest.mark.task_suite
@pytest.mark.init_suite
@pytest.mark.xfail(reason="Unable initialization of object without Description")
def test_init_without_description():
    Task(title="Title_01")

    assert 0

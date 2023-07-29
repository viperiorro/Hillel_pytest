import pytest
from app.task import Task


__new_task = Task(title="My task #1", description="Positive testing", due_date="2023-07-28", priority="High")
__false_str = "My task #1 - Positive testing - Due: 2023-07-28 - Priority: High - Completed: False"
__true_str = "My task #1 - Positive testing - Due: 2023-07-28 - Priority: High - Completed: True"

@pytest.mark.test
@pytest.mark.positive
def test_add_task_pos(todo_list_object):
    todo_list_object.add_task(__new_task)
    assert str(todo_list_object.tasks[0]) == __false_str

@pytest.mark.parametrize("test_tada", [
        {"title": "My task #1", "description": "Positive testing", "due_date": "2023-07-28", "priority": "High"},
        {"title": "My task #2", "description": "Positive testing", "due_date": "2023-07-29", "priority": "High"},
        {"title": "My task #3", "description": "Positive testing", "due_date": "2023-06-28", "priority": "Low"}
    ])
@pytest.mark.positive
def test_remove_task_pos(todo_list_object, test_tada):
    todo_list_object.add_task(test_tada)
    todo_list_object.remove_task(test_tada)
    assert len(todo_list_object.tasks) == 0

@pytest.mark.test
@pytest.mark.positive
def test_remove_task_pos(todo_list_object):
    todo_list_object.add_task("1")
    todo_list_object.add_task("2")
    todo_list_object.remove_task("1")
    assert len(todo_list_object.tasks) == 1

@pytest.mark.positive
def test_display_tasks_pos(todo_list_object):
    todo_list_object.add_task(__new_task)
    todo_list_object.display_tasks()
    assert str(todo_list_object.tasks[0]) == __false_str

@pytest.mark.positive
def test_get_pending_task_pos(todo_list_object):
    todo_list_object.add_task(__new_task)
    todo_list_object.get_pending_tasks()
    assert str(todo_list_object.tasks[0]) == __false_str

@pytest.mark.positive
def test_mark_task_pos(todo_list_object):
    todo_list_object.add_task(__new_task)
    todo_list_object.mark_task_as_completed(__new_task)
    assert str(todo_list_object.tasks[0]) == __true_str

@pytest.mark.positive
def test_get_completed_tasks_pos(todo_list_object):
    todo_list_object.add_task(__new_task)
    todo_list_object.mark_task_as_completed(todo_list_object.tasks[0])
    assert str(todo_list_object.tasks[0]) == __true_str

@pytest.mark.test
@pytest.mark.negative
@pytest.mark.xfail
def test_add_task_neg(todo_list_object):
    todo_list_object.add_task(__new_task)
    assert str(todo_list_object.tasks[0]) == __true_str


@pytest.mark.negative
def test_display_tasks_neg(todo_list_object):
    todo_list_object.add_task(__new_task)
    todo_list_object.remove_task(__new_task)
    todo_list_object.display_tasks()
    assert len(todo_list_object.tasks) == 0

@pytest.mark.negative
def test_get_pending_task_neg(todo_list_object):
    todo_list_object.add_task(__new_task)
    todo_list_object.mark_task_as_completed(__new_task)
    todo_list_object.get_pending_tasks()
    assert str(todo_list_object.tasks[0]) == __true_str

@pytest.mark.negative
def test_mark_task_neg(todo_list_object):
    todo_list_object.add_task(Task(title="My task #1", description="Positive testing", due_date="2023-07-28", priority="High"))
    todo_list_object.add_task(__new_task)
    todo_list_object.mark_task_as_completed(__new_task)
    assert str(todo_list_object.tasks[0]) == __false_str




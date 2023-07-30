import pytest

from app.task import Task

from app.to_do_list import ToDoList


def test_todo_list_initialization():
    todo_list = ToDoList()
    assert len(todo_list.tasks) == 0


@pytest.mark.standard
def test_add_task(empty_todo_list):
    task = Task("Task 1", "This is a new task", "30.07.2023", "Low")
    empty_todo_list.add_task(task)
    assert len(empty_todo_list.tasks) == 1


def test_remove_task(empty_todo_list, task1):
    empty_todo_list.add_task(task1)
    assert len(empty_todo_list.tasks) == 1
    empty_todo_list.remove_task(task1)
    assert len(empty_todo_list.tasks) == 0


def test_mark_task_as_completed(todo_list_with_tasks, task1):
    assert not task1.completed
    todo_list_with_tasks.mark_task_as_completed(task1)
    assert task1.completed


@pytest.mark.extended
@pytest.mark.skip(reason="Manually check the output for display_tasks().")
def test_display_tasks(todo_list_with_tasks):
    print("Displaying tasks:")
    todo_list_with_tasks.display_tasks()


def test_get_pending_tasks(todo_list_with_tasks, task1, task2):
    assert len(todo_list_with_tasks.get_pending_tasks()) == 2
    todo_list_with_tasks.mark_task_as_completed(task1)
    assert len(todo_list_with_tasks.get_pending_tasks()) == 1
    assert todo_list_with_tasks.get_pending_tasks()[0] == task2
    todo_list_with_tasks.mark_task_as_completed(task2)
    assert len(todo_list_with_tasks.get_pending_tasks()) == 0


@pytest.mark.xfail(reason="The get_completed_tasks method is not yet implemented correctly.")
def test_get_completed_tasks(todo_list_with_tasks, task1):
    assert len(todo_list_with_tasks.get_completed_tasks()) == 0
    todo_list_with_tasks.mark_task_as_completed(task1)
    assert len(todo_list_with_tasks.get_completed_tasks()) == 1
    assert todo_list_with_tasks.get_completed_tasks()[0] == task1

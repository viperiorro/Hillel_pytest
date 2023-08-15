import pytest
from app.task import Task
from app.to_do_list import ToDoList


@pytest.mark.priority
def test_add_task(new_todo_list, new_task):
    new_todo_list.add_task(new_task)
    assert len(new_todo_list.tasks) == 1


@pytest.mark.completed
def test_remove_task(new_todo_list, new_task):
    new_todo_list.add_task(new_task)
    new_todo_list.remove_task(new_task)
    assert len(new_todo_list.tasks) == 0




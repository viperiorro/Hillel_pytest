import pytest

from app.task import Task
from app.to_do_list import ToDoList


@pytest.fixture(scope='module')
def todolist_main():
    todolist = ToDoList()
    task1 = Task("Task 1", "Description for Task 1", "2023-07-29", "Low")
    task2 = Task("Task 2", "Description for Task 2", "2023-07-30", "Medium")
    todolist.add_task(task1)
    todolist.add_task(task2)
    return todolist


@pytest.mark.todolist
def test_todolist_add_task(todolist_main):
    initial_task_count = len(todolist_main.tasks)
    task3 = Task("Task 3", "Description for Task 3", "2023-08-01", "High")
    todolist_main.add_task(task3)
    assert len(todolist_main.tasks) == initial_task_count + 1


@pytest.mark.todolist
def test_todolist_remove_task(todolist_main):
    initial_task_count = len(todolist_main.tasks)
    task_to_remove = todolist_main.tasks[0]
    todolist_main.remove_task(task_to_remove)
    assert len(todolist_main.tasks) == initial_task_count - 1


@pytest.mark.todolist
def test_todolist_mark_task_as_completed(todolist_main):
    task_to_mark_completed = todolist_main.tasks[0]
    assert not task_to_mark_completed.completed
    todolist_main.mark_task_as_completed(task_to_mark_completed)
    assert task_to_mark_completed.completed


@pytest.mark.todolist
def test_todolist_get_pending_tasks(todolist_main):
    pending_tasks = todolist_main.get_pending_tasks()
    assert all(not task.completed for task in pending_tasks)


@pytest.mark.todolist
def test_todolist_get_completed_tasks(todolist_main):
    completed_tasks = todolist_main.get_completed_tasks()
    assert all(task.completed for task in completed_tasks)


@pytest.mark.todolist
def test_todolist_display_tasks(todolist_main):
    expected_output = "Task 1 - Description for Task 1 - Due: 2023-07-29 - Priority: Low - Completed: False\n" \
                      "Task 2 - Description for Task 2 - Due: 2023-07-30 - Priority: Medium - Completed: False\n"
    assert all(expected_output)
    print(f"Tasks in ToDoList: {expected_output}")

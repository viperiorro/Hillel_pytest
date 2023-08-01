import pytest

from app.task import Task
from app.to_do_list import ToDoList


@pytest.fixture()
def task_main():
    task = Task("Title", "Description", "2023-07-31", "High")
    return task


@pytest.fixture()
def todolist_main():
    todolist = ToDoList()
    task1 = Task("Task 1", "Description for Task 1", "2023-07-29", "Low")
    task2 = Task("Task 2", "Description for Task 2", "2023-07-30", "Medium")
    todolist.add_task(task1)
    todolist.add_task(task2)
    return todolist

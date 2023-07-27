import pytest
import sys


@pytest.mark.to_do_list
def test_add_task(to_do_list_ob):
    to_do_list_ob.add_task("test app")
    assert "test app" in to_do_list_ob.tasks


@pytest.mark.to_do_list
@pytest.mark.parametrize("test_task", [
    "first_task",
    "second_task",
    "third_task"
])
def test_remove_task(to_do_list_ob, test_task):
    to_do_list_ob.add_task(test_task)
    to_do_list_ob.remove_task(test_task)
    assert test_task not in to_do_list_ob.tasks


@pytest.mark.to_do_list
def test_completed_mark(to_do_list_ob, task_object):
    to_do_list_ob.add_task(task=task_object)
    to_do_list_ob.mark_task_as_completed(task=task_object)
    assert task_object.completed


@pytest.mark.to_do_list
def test_display_tasks(to_do_list_ob):
    to_do_list_ob.add_task("first")
    to_do_list_ob.add_task("second")
    to_do_list_ob.add_task("third")
    # write output from display_tasks to file
    with open("Output.txt", "w") as file:
        sys.stdout = file
        to_do_list_ob.display_tasks()
    # read output and join it to result string
    result = ""
    with open("Output.txt", "r") as f:
        result = "".join(f.read())

    assert result == "first\nsecond\nthird\n"


@pytest.mark.to_do_list
def test_get_pending_tasks(to_do_list_ob, task_object):
    to_do_list_ob.add_task(task=task_object)
    assert to_do_list_ob.get_pending_tasks()[0] == to_do_list_ob.tasks[0]


@pytest.mark.to_do_list
def test_get_completed_tasks(to_do_list_ob, task_object):
    to_do_list_ob.add_task(task=task_object)
    to_do_list_ob.mark_task_as_completed(task=task_object)
    assert to_do_list_ob.get_completed_tasks()[0] == to_do_list_ob.tasks[0]

import pytest


@pytest.mark.to_do_list_suite
@pytest.mark.init_suite
def test_init(to_do_list_tasks):
    assert len(to_do_list_tasks) == 0


@pytest.mark.to_do_list_suite
def test_add_task(to_do_list_empty_object, task_object):
    to_do_list_empty_object.add_task(task=task_object)
    assert len(to_do_list_empty_object.tasks) == 1


@pytest.mark.to_do_list_suite
@pytest.mark.skip(reason="Adding task with the same parameters is not implemented yet")
def test_add_task_twice(to_do_list_empty_object, task_object):
    to_do_list_empty_object.add_task(task=task_object)
    to_do_list_empty_object.add_task(task=task_object)
    assert len(to_do_list_empty_object.tasks) == 2


@pytest.mark.to_do_list_suite
def test_remove_task(to_do_list_obj_with_tasks, task_object, task_object_1):
    to_do_list_obj_with_tasks.remove_task(task=task_object_1)
    assert to_do_list_obj_with_tasks.tasks == [
        task_object
    ]  # checks if removed specified task in the list


@pytest.mark.to_do_list_suite
def test_mark_task_as_completed(to_do_list_obj_with_tasks, task_object):
    to_do_list_obj_with_tasks.mark_task_as_completed(task=task_object)
    assert task_object.completed  # checks if completed specified task in the list


@pytest.mark.to_do_list_suite
def test_display_tasks(to_do_list_empty_object, task_object, capsys):
    to_do_list_empty_object.add_task(task=task_object)
    to_do_list_empty_object.display_tasks()
    actual_result = capsys.readouterr().out
    expected_result = "Title_01 - Description_01 - Due: 2023-07-30 - Priority: Medium - Completed: True\n"

    assert actual_result == expected_result


@pytest.mark.to_do_list_suite
def test_get_pending_tasks(to_do_list_obj_with_tasks, task_object, task_object_1):
    to_do_list_obj_with_tasks.mark_task_as_completed(task=task_object)
    actual_result = to_do_list_obj_with_tasks.get_pending_tasks()
    expected_result = [task_object_1]

    assert actual_result == expected_result


@pytest.mark.to_do_list_suite
def test_get_completed_tasks(to_do_list_obj_with_tasks, task_object, task_object_1):
    to_do_list_obj_with_tasks.mark_task_as_completed(task=task_object)
    to_do_list_obj_with_tasks.mark_task_as_completed(task=task_object_1)
    actual_result = to_do_list_obj_with_tasks.get_completed_tasks()
    expected_result = to_do_list_obj_with_tasks.tasks

    assert actual_result == expected_result

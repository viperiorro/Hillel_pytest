import pytest
from app.to_do_list import ToDoList


@pytest.mark.todo_list_suite
def test_todolist_initialization():
    todolist = ToDoList()
    assert todolist.tasks == []


@pytest.mark.todo_list_suite
def test_add_task(create_task_for_to_do_list, create_to_do_list):
    create_to_do_list.add_task(create_task_for_to_do_list)
    result = create_to_do_list.tasks
    assert result[0] == create_task_for_to_do_list


@pytest.mark.todo_list_suite
@pytest.mark.xfail
def test_add_task_whithout_params(create_to_do_list):
    create_to_do_list.add_task()
    assert 0


@pytest.mark.todo_list_suite
def test_remove_task(create_task_for_to_do_list, create_to_do_list):
    create_to_do_list.add_task(create_task_for_to_do_list)
    create_to_do_list.remove_task(create_task_for_to_do_list)
    result = create_to_do_list.tasks
    assert len(result) == 1


@pytest.mark.todo_list_suite
@pytest.mark.xfail
def test_remove_task_non_existing_task(create_task_for_to_do_list, create_to_do_list):
    create_to_do_list.remove_task(create_task_for_to_do_list)
    assert 0


@pytest.mark.todo_list_suite
def test_marked_task_as_completed(create_task_for_to_do_list, create_to_do_list):
    create_to_do_list.add_task(create_task_for_to_do_list)
    create_to_do_list.mark_task_as_completed(create_task_for_to_do_list)
    assert create_to_do_list.tasks[0].completed


@pytest.mark.todo_list_suite
@pytest.mark.xfail
def test_marked_completed_non_existing_task(
    create_task_for_to_do_list, create_to_do_list
):
    create_to_do_list.mark_task_as_completed(create_task_for_to_do_list)
    assert 0


@pytest.mark.todo_list_suite
def test_display_tasks(create_task_for_to_do_list, create_to_do_list, capsys):
    create_to_do_list.display_tasks()
    result = capsys.readouterr()
    expected_result = (
        "test1 - test description - Due: 2023-07-26 - Priority: low - Completed: True\n"
    )
    assert result.out == expected_result


@pytest.mark.todo_list_suite
def test_get_pending_tasks(create_task, create_to_do_list):
    create_to_do_list.add_task(create_task)
    assert create_to_do_list.get_pending_tasks() == [create_task]


@pytest.mark.todo_list_suite
def test_get_completed_tasks(create_task_for_to_do_list, create_to_do_list):
    assert create_to_do_list.get_completed_tasks() == [create_task_for_to_do_list]

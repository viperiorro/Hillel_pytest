import pytest


@pytest.mark.to_do_list_test
def test_list_init(sample_to_do_list):
    assert len(sample_to_do_list.tasks) == 0


@pytest.mark.to_do_list_test
def test_add_task(sample_to_do_list, sample_task):
    sample_to_do_list.add_task(sample_task)
    assert len(sample_to_do_list.tasks) == 1


@pytest.mark.to_do_list_test
def test_remove_task(sample_to_do_list, sample_task):
    sample_to_do_list.add_task(sample_task)
    sample_to_do_list.remove_task(sample_task)
    assert len(sample_to_do_list.tasks) == 0


@pytest.mark.to_do_list_test
def test_mark_task_as_completed(sample_to_do_list, sample_task):
    sample_to_do_list.add_task(sample_task)
    sample_to_do_list.mark_task_as_completed(sample_task)
    assert sample_task.completed


@pytest.mark.to_do_list_test
def test_display_tasks(sample_to_do_list, sample_task, capsys):
    sample_to_do_list.add_task(sample_task)
    sample_to_do_list.display_tasks()
    captured = capsys.readouterr()

    expected_output = sample_task.__str__() + "\n"
    assert captured.out == expected_output


@pytest.mark.to_do_list_test
def test_get_pending_tasks(sample_to_do_list, sample_task):
    sample_to_do_list.add_task(task=sample_task)
    assert sample_to_do_list.get_pending_tasks()[0] == sample_to_do_list.tasks[0]


@pytest.mark.to_do_list_test
def test_get_completed_tasks(sample_to_do_list, sample_task):
    sample_to_do_list.add_task(task=sample_task)
    sample_to_do_list.mark_task_as_completed(task=sample_task)
    assert sample_to_do_list.get_completed_tasks()[0] == sample_to_do_list.tasks[0]

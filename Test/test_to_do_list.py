import pytest


class TestToDoList:
    @pytest.mark.test_to_do_list
    def test_init(self, create_to_do_list):
        assert create_to_do_list.tasks == []


    @pytest.mark.test_to_do_list
    def test_add_task(self, create_to_do_list_with_task, task_object):
        actual_result = create_to_do_list_with_task.tasks
        assert actual_result[0] == task_object


    @pytest.mark.test_to_do_list
    def test_remove_task(self, create_to_do_list_with_task, task_object):
        create_to_do_list_with_task.remove_task(task_object)
        assert task_object not in create_to_do_list_with_task.tasks


    @pytest.mark.test_to_do_list
    def test_mark_task_as_completed(self, create_to_do_list_with_task, task_object):
        create_to_do_list_with_task.mark_task_as_completed(task_object)
        assert task_object.completed


    @pytest.mark.test_to_do_list
    def test_display_tasks(self, create_to_do_list, task_object, capsys):
        create_to_do_list.add_task(task_object)
        create_to_do_list.display_tasks()
        captured = capsys.readouterr()
        assert task_object.__str__() + "\n" == captured.out

    @pytest.mark.test_to_do_list
    def test_get_pending_tasks(self, create_to_do_list, task_object, task_object2):
        create_to_do_list.add_task(task_object)
        create_to_do_list.add_task(task_object2)
        assert create_to_do_list.get_pending_tasks() == [task_object, task_object2]


    @pytest.mark.test_to_do_list
    def test_get_completed_tasks(self, create_to_do_list, task_object, task_object2):
        create_to_do_list.add_task(task_object)
        create_to_do_list.add_task(task_object2)
        create_to_do_list.mark_task_as_completed(task_object)
        create_to_do_list.mark_task_as_completed(task_object2)
        assert create_to_do_list.get_completed_tasks() == [task_object, task_object2]



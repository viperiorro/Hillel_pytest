import pytest

from app.task import Task


class TestTask:
    @pytest.mark.test_task
    @pytest.mark.parametrize("test_data, expected_result", [({"title": "test1",
                                                              "description": "create_test",
                                                              "due_date": "2023-07-30",
                                                              "priority": "High"},
                                                             {"title": "test1",
                                                              "description": "create_test",
                                                              "due_date": "2023-07-30",
                                                              "priority": "High"}),
                                                            ({"title": "test2",
                                                              "description": "create_test2"},
                                                             {"title": "test2",
                                                              "description": "create_test2",
                                                              "due_date": None,
                                                              "priority": None})])
    def test_init(self, test_data, expected_result):
        list_data = []
        for key, value in test_data.items():
            list_data.append(value)
        test_task = Task(*list_data)
        assert test_task.title == expected_result["title"]
        assert test_task.description == expected_result["description"]
        assert test_task.due_date == expected_result["due_date"]
        assert test_task.priority == expected_result["priority"]
        assert test_task.completed is False

    @pytest.mark.test_task
    def test_mark_as_completed(self, task_object_completed):
        actual_result = task_object_completed.__str__()
        expected_result = "Test - Create test - Due: 2023-07-30 - Priority: High - Completed: True"
        assert actual_result == expected_result

    @pytest.mark.xfail(reason="some reason")
    @pytest.mark.test_task
    def test_init_completed(self, task_object):
        assert task_object.completed is True

    @pytest.mark.skip(reason="some reason")
    @pytest.mark.test_task
    def test_init_completed2(self, task_object):
        assert task_object.completed is False

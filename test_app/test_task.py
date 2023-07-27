import pytest
from datetime import date


class TestTask:
    @pytest.mark.task
    def test_title(self, task_object):
        assert task_object.title == "test title"

    @pytest.mark.task
    def test_description(self, task_object):
        assert task_object.description == "test description"

    @pytest.mark.task
    @pytest.mark.xfail  # compare to current date
    def test_date(self, task_object):
        current_date = date.today()
        assert task_object.due_date == current_date.strftime("%Y-%m-%d")

    @pytest.mark.task
    def test_priority(self, task_object):
        assert task_object.priority == "Low"

    @pytest.mark.task
    def test_completion_default(self, task_object):
        assert task_object.completed is False

    @pytest.mark.task
    def test_completed(self, task_object):
        task_object.mark_as_completed()
        assert task_object.completed

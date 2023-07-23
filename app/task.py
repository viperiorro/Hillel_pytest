class Task:
    def __init__(self, title, description, due_date=None, priority=None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        return f"{self.title} - {self.description} - Due: {self.due_date} - Priority: {self.priority} - Completed: {self.completed}"

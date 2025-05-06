import unittest
from hello import add_task, mark_task_done, list_tasks

class TestToDoApp(unittest.TestCase):
    def setUp(self):
        """
        Set up a fresh list of tasks for each test.
        """
        self.tasks = [
            {"name": "Task 1", "done": False},
            {"name": "Task 2", "done": True},
        ]

    def test_add_task(self):
        """
        Test adding a new task to the list.
        """
        add_task(self.tasks, "New Task")
        self.assertEqual(len(self.tasks), 3)  # Ensure the task list has grown
        self.assertEqual(self.tasks[-1]["name"], "New Task")  # Check the task name
        self.assertFalse(self.tasks[-1]["done"])  # Ensure the task is not marked as done

    def test_mark_task_done(self):
        """
        Test marking a task as done.
        """
        mark_task_done(self.tasks, 0)  # Mark the first task as done
        self.assertTrue(self.tasks[0]["done"])  # Ensure the task is marked as done

    def test_mark_task_done_invalid_index(self):
        """
        Test marking a task as done with an invalid index.
        """
        with self.assertLogs(level="ERROR") as log:
            mark_task_done(self.tasks, 10)  # Invalid index
        self.assertIn("Invalid task index.", log.output[0])

    def test_list_tasks(self):
        """
        Test listing all tasks.
        """
        with self.assertLogs(level="INFO") as log:
            list_tasks(self.tasks)  # Call the list_tasks function

        # Combine all log messages into a single string for easier checking
        log_output = "\n".join(log.output)

        # Check that the expected output is in the logs
        self.assertIn("1. Task 1 [Not Done]", log_output)  # Check first task
        self.assertIn("2. Task 2 [Done]", log_output)  # Check second task

if __name__ == "__main__":
    unittest.main()
import unittest
import task_manager 

class TestCaseTaskManager(unittest.TestCase):

    def test_setUp(self):
        tm = task_manager.TaskManager()

    def test_create_task(self):
        """ Checks if it creates correctly a new task with the title as parameter. When that happens, the method returns True"""
        tm = task_manager.TaskManager()
        respuesta = tm.addTask("Tarea 1")
        self.assertEqual(respuesta, True)

    def test_complete_task(self):
        """ If a task is in the dictionary it will mark it as completed and returns a True"""
        tm = task_manager.TaskManager()
        tm.addTask("Tarea 1")
        respuesta = tm.completeTask("Tarea 1")
        self.assertEqual(respuesta, True)
        self.assertEqual(tm.completeTask("Tarea z"), False)


    def test_delete_task(self):
        """ If a task is in the dictionary, it will mark delete it and returns a True"""
        tm = task_manager.TaskManager()
        tm.addTask("Tarea 1")
        self.assertEqual(tm.deleteTask("Tarea 1"), True)
        self.assertEqual(tm.deleteTask("Tarea 1"), False)


    def test_get_completed_tasks(self):
        """ It returns a list with all the titles of the completed tasks"""
        tm = task_manager.TaskManager()
        tm.addTask("Tarea 1")
        tm.addTask("Tarea 2")
        tm.addTask("Tarea 3")
        tm.completeTask("Tarea 1")
        tm.completeTask("Tarea 3")
        respuesta = tm.get_complete_tasks()
        self.assertEqual(respuesta, ["Tarea 1", "Tarea 3"])

    def test_get_uncompleted_tasks(self):
        """ It returns a list with all the titles of the uncompleted tasks"""
        tm = task_manager.TaskManager()
        tm.addTask("Tarea 1")
        tm.addTask("Tarea 2")
        tm.addTask("Tarea 3")
        tm.addTask("Tarea 4")
        tm.completeTask("Tarea 1")
        tm.completeTask("Tarea 3")
        respuesta = tm.get_uncomplete_tasks()
        self.assertEqual(respuesta, ["Tarea 2", "Tarea 4"])

    
    def test_returns_no_tasks(self):
        tm = task_manager.TaskManager()
        self.assertEqual(tm.get_complete_tasks(), [])
        self.assertEqual(tm.get_uncomplete_tasks(), [])
    



    

class TaskManager:
    def __init__(self):
        self.tasks = dict()
    

    def addTask(self, my_title):
        if my_title not in self.tasks.keys():
            self.tasks[my_title] = False
            return True
        return False
    
    
    def completeTask(self, my_title):
        if my_title in self.tasks.keys():
            self.tasks[my_title] = True
            return True
        return False


    def deleteTask(self, my_title):
        if my_title in self.tasks.keys():
            del self.tasks[my_title]
            return True
        return False
    
    def get_complete_tasks(self):
        completed_tasks = []
        if len(self.tasks) > 0:
            for title, value in self.tasks.items():
                if value:
                    completed_tasks.append(title)
        return completed_tasks 
    

    def get_uncomplete_tasks(self):
        uncompleted_tasks = []
        if len(self.tasks) > 0:
            for title, value in self.tasks.items():
                if not value:
                    uncompleted_tasks.append(title)
        return uncompleted_tasks 
             
    

    """ Requirements:

    - Add a task with a title- OK 
    - Mark a task as completed (True) via title- OK
    - Delete a task via title - OK 
    - Get all the completed tasks - OK 
    - Gett all the uncompleted tasks- OK

    - Special case: there are no tasks

    """ 

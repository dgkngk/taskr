from datamodels.Status import Status

class TaskModel:
    def __init__(self):
        self.title = ""
        self.description = ""
        self.status = Status.Open
        self.active = True
        
    def as_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "status": self.status.value,
            "active": self.active
        }
    
    def set_with_dict(self, task_as_dict):
        self.title = task_as_dict["title"]
        self.description = task_as_dict["description"]
        self.status = Status(task_as_dict["status"])
        self.active = task_as_dict["active"]
    
    def __eq__(self, __value: object) -> bool:
        return self.as_dict() == __value
        
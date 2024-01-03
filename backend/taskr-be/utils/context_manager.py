from utils.cache_util import CacheHelper
from utils.logger_util import taskr_logger

class ContextManager:
    def __init__(self):
        self._cache = CacheHelper()
        self._ctx_dict = {"tasks": []}
    
    def get_ctx_dict(self):
        return self._ctx_dict
    
    def load_context(self):
        try:
            loaded = self._cache.read_cache_file("ctx.cache")
            if loaded is None:
                self._ctx_dict = {"tasks": []}
            else:
                self._ctx_dict = loaded
            return True
        except Exception as e:
            taskr_logger.exception("Could not load context, setting empty context")
            self._ctx_dict = {"tasks": []}
            return False

    def get_all_tasks(self):
        self.load_context()
        return self._ctx_dict["tasks"]
    
    def add_task(self, task):
        self.load_context()
        before_save = self._ctx_dict.copy()
        try:
            self._ctx_dict["tasks"].append(task)
            save_result = self._cache.save_obj_to_file(self._ctx_dict, "ctx.cache")
            if not save_result:
                self._ctx_dict = before_save
                return False
            return True
        except Exception as e:
            taskr_logger.exception("Could not add task")
            self._ctx_dict = before_save
            return False
        
    def remove_task(self, task_id):
        self.load_context()
        before_save = self._ctx_dict.copy()
        try:
            for task in self._ctx_dict["tasks"]:
                if task.title == task_id:
                    self._ctx_dict["tasks"].remove(task)
            save_result = self._cache.save_obj_to_file(self._ctx_dict, "ctx.cache")
            if not save_result:
                self._ctx_dict = before_save
                return False
            return True
        except Exception as e:
            taskr_logger.exception("Could not remove task ")
            self._ctx_dict = before_save
            return False
    
    def task_exists(self, task):
        self.load_context()
        return task in [task.title for task in self._ctx_dict["tasks"]]
    
    def get_task(self, task_id):
        self.load_context()
        for task in self._ctx_dict["tasks"]:
            if task.title == task_id:
                return task
        taskr_logger.error(f"Could not find task with id {task_id}")
        return None
    
    def update_task(self, task):
        self.load_context()
        before_save = self._ctx_dict.copy()
        try:
            self._ctx_dict["tasks"].remove(task)
            self._ctx_dict["tasks"].append(task)
            save_result = self._cache.save_obj_to_file(self._ctx_dict, "ctx.cache")
            if not save_result:
                self._ctx_dict = before_save
                return False
            return True
        except Exception as e:
            taskr_logger.exception("Could not update task ")
            self._ctx_dict = before_save
            return False
        
    def clear_context(self):
        self._ctx_dict = {"tasks": []}
        before_save = self._ctx_dict.copy()
        save_result = self._cache.save_obj_to_file(self._ctx_dict, "ctx.cache")
        if not save_result:
            self._ctx_dict = before_save
            return False
        return True
    
import pytest
from unittest.mock import MagicMock
from utils import taskr_logger
from utils.cache_util import CacheHelper
from utils.context_manager import ContextManager 

@pytest.fixture
def context_manager():
    return ContextManager()

def test_load_context_success(context_manager, mocker):
    mocker.patch.object(CacheHelper, 'read_cache_file', return_value={"tasks": ["task1", "task2"]})
    assert context_manager.load_context() is True
    assert context_manager.get_ctx_dict() == {"tasks": ["task1", "task2"]}

def test_load_context_exception(context_manager, mocker):
    mocker.patch.object(CacheHelper, 'read_cache_file', side_effect=Exception("Some error"))
    
    assert context_manager.load_context() is False
    assert context_manager.get_ctx_dict() == {"tasks": []}

def test_get_all_tasks(context_manager, mocker):
    mocker.patch.object(CacheHelper, 'read_cache_file', return_value={"tasks": ["task1", "task2"]})
    assert context_manager.get_all_tasks() == ["task1", "task2"]

def test_add_task_success(context_manager, mocker):
    mocker.patch.object(CacheHelper, 'read_cache_file', return_value={"tasks": ["task1"]})
    mocker.patch.object(CacheHelper, 'save_obj_to_file', return_value=True)
    assert context_manager.add_task("new_task") is True
    assert context_manager.get_ctx_dict() == {"tasks": ["task1", "new_task"]}

def test_add_task_exception(context_manager, mocker):
    mocker.patch.object(CacheHelper, 'read_cache_file', return_value={"tasks": ["task1"]})
    mocker.patch.object(CacheHelper, 'save_obj_to_file', side_effect=Exception("Some error"))
    
    
    assert context_manager.add_task("new_task") is False
    assert context_manager.get_ctx_dict() == {"tasks": ["task1"]}

def test_remove_task_success(context_manager, mocker):
    mocker.patch.object(CacheHelper, 'read_cache_file', return_value={"tasks": ["task1", "task2"]})
    mocker.patch.object(CacheHelper, 'save_obj_to_file', return_value=True)
    assert context_manager.remove_task("task1") is True
    assert context_manager.get_ctx_dict() == {"tasks": ["task2"]}

def test_remove_task_exception(context_manager, mocker):
    task_obj1 = MagicMock(title="task1")
    mocker.patch.object(CacheHelper, 'read_cache_file', return_value={"tasks": [task_obj1]})
    mocker.patch.object(CacheHelper, 'save_obj_to_file', return_value=False)
    
    
    assert context_manager.remove_task(task_obj1) is False
    assert context_manager.get_ctx_dict() == {"tasks": [task_obj1]}

def test_task_exists(context_manager, mocker):
    mocker.patch.object(CacheHelper, 'read_cache_file', return_value={"tasks": ["task1", "task2"]})
    assert context_manager.task_exists("task1") is True
    assert context_manager.task_exists("task3") is False

def test_get_task(context_manager, mocker):
    task_obj1 = MagicMock(title="task1")
    task_obj2 = MagicMock(title="task2")
    mocker.patch.object(CacheHelper, 'read_cache_file', return_value={"tasks": [task_obj1, task_obj2]})
    
    task_obj = MagicMock(title="task1")
    assert context_manager.get_task("task1").title == task_obj.title

def test_get_task_not_found(context_manager, mocker):
    mocker.patch.object(CacheHelper, 'read_cache_file', return_value={"tasks": ["task1", "task2"]})
    mocker.patch.object(taskr_logger, 'error')
    
    assert context_manager.get_task("task3") is None

def test_update_task_success(context_manager, mocker):
    task_obj = MagicMock(title="task1")
    task_obj2 = MagicMock(title="task2")
    mocker.patch.object(CacheHelper, 'read_cache_file', return_value={"tasks": [task_obj, task_obj2]})
    mocker.patch.object(CacheHelper, 'save_obj_to_file', return_value=True)
    
    task_obj.status="done"
    assert context_manager.update_task(task_obj) is True
    assert context_manager.get_ctx_dict() == {"tasks": [task_obj2, task_obj]}
    assert context_manager.get_ctx_dict()["tasks"][1].status == "done"

def test_update_task_exception(context_manager, mocker):
    mocker.patch.object(CacheHelper, 'read_cache_file', return_value={"tasks": ["task1", "task2"]})
    mocker.patch.object(CacheHelper, 'save_obj_to_file', side_effect=Exception("Some error"))
    
    
    task_obj = MagicMock(title="task1")
    assert context_manager.update_task(task_obj) is False
    assert context_manager.get_ctx_dict() == {"tasks": ["task1", "task2"]}

def test_clear_context(context_manager, mocker):
    mocker.patch.object(CacheHelper, 'save_obj_to_file', return_value=True)
    context_manager.clear_context()
    assert context_manager.get_ctx_dict() == {"tasks": []}

import pytest
from datamodels.Status import Status  
from datamodels.TaskModel import TaskModel

@pytest.fixture
def sample_task():
    return TaskModel()

def test_task_model_default_values(sample_task):
    assert sample_task.title == ""
    assert sample_task.description == ""
    assert sample_task.status == Status.Open
    assert sample_task.active is True

def test_task_model_as_dict(sample_task):
    sample_task.title = "Sample Task"
    sample_task.description = "Description of the task"
    sample_task.status = Status.Testing
    sample_task.active = False
    
    expected_dict = {
        "title": "Sample Task",
        "description": "Description of the task",
        "status": Status.Testing.value,
        "active": False
    }
    
    assert sample_task.as_dict() == expected_dict

def test_task_model_set_with_dict(sample_task):
    task_dict = {
        "title": "Updated Task",
        "description": "Updated description",
        "status": Status.Done.value,
        "active": True
    }
    
    sample_task.set_with_dict(task_dict)
    
    assert sample_task.title == "Updated Task"
    assert sample_task.description == "Updated description"
    assert sample_task.status == Status.Done
    assert sample_task.active is True

def test_task_model_equality(sample_task):
    task1 = TaskModel()
    task2 = TaskModel()

    assert task1 == task2  # Both have default values
    
    task1.title = "Task 1"
    task2.title = "Task 1"
    
    assert task1 == task2  # Both have the same title
    
    task2.title = "Task 2"
    
    assert task1 != task2  # Titles are different

    task2.title = "Task 1"
    task1.status = Status.Testing
    
    assert task1 != task2  # Status is different

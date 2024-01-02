from utils.cache_util import CacheHelper

test_dict = {"a": 1, "b": 2, "c": 3}

def test_save_obj_to_file():
    assert CacheHelper().save_obj_to_file(test_dict, "test_cache")

def test_read_cache_file():
    assert CacheHelper().read_cache_file("test_cache") == test_dict

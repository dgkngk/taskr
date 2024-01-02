import os
import pickle
from typing import Any
from utils import taskr_logger


class CacheHelper:
    def __init__(self, cache_dir: str = ".cache"):
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)

        self.cache_dir = cache_dir

    def save_obj_to_file(self, obj, filename: str) -> bool:
        try:
            file_path = os.path.join(self.cache_dir, filename)
            with open(file_path, "wb") as f:
                pickle.dump(obj, f)
            return True
        except pickle.PickleError:
            taskr_logger.error(f"Unable to save {filename} in {self.cache_dir}")
            return False
        except Exception:
            taskr_logger.exception(f"Unable to save {filename} because of exception")
            return False

    def read_cache_file(self, filename: str) -> Any:
        try:
            file_path = os.path.join(self.cache_dir, filename)
            with open(file_path, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            taskr_logger.error(f"Unable to load {filename}, no cache found.")
            return None
        except Exception:
            taskr_logger.exception(f"Unable to load {filename} because of exception")
            return None

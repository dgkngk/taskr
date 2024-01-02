from utils import taskr_logger

def test_taskr_logger_init():
    assert taskr_logger is not None
    
def test_taskt_logger_utils():
    assert taskr_logger.critical("test") is None
    assert taskr_logger.error("test") is None
    assert taskr_logger.info("test") is None
    assert taskr_logger.warning("test") is None
    assert taskr_logger.exception("test") is None
    assert taskr_logger.debug("test") is None
import pytest
import logging

def setup_logger(name="LOG"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Удаляем все существующие обработчики
    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger

@pytest.fixture
def logger(request):
    logger = setup_logger()

    def fin():
        # Удалить все обработчики потока
        for handler in logger.handlers[:]:
            handler.close()
            logger.removeHandler(handler)

    request.addfinalizer(fin)

    return logger
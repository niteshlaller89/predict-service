from typing import Callable

StartupCb = Callable[[], None]


def preload_model():
    """
    In order to load model on memory to each worker
    """
    from services.predict import MachineLearningModelHandlerScore

    MachineLearningModelHandlerScore.get_model()


def create_start_app_handler() -> StartupCb:
    def startup_cb() -> None:
        preload_model()

    return startup_cb

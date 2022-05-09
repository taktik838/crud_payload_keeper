import logging
from queue import Queue
import sys
from threading import Thread

import settings


file_handler = logging.FileHandler(settings.PATH_TO_FILE)
stdout_handler = logging.StreamHandler(sys.stdout)

class ThreadLoggingManager:
    def __init__(self, n_workers: int = settings.LOGGING_N_WORKERS):
        self._queue: Queue[logging.LogRecord] = Queue(-1)

        self._workers = tuple(
            Thread(target=self._work, args=(self._queue, ))
            for _ in range(n_workers)
        )

    @staticmethod
    def _work(queue: "Queue[logging.LogRecord]"):
        while True:
            record = queue.get()
            if settings.LOG_TO_FILE:
                file_handler.handle(record)
            else:
                stdout_handler.handle(record)

    def run_workers(self) -> None:
        for worker in self._workers:
            worker.run()

    def add_record(self, record: logging.LogRecord) -> None:
        self._queue.put(record)


class MultiThreadingHandler(logging.Handler):
    def __init__(self, level=logging.NOTSET) -> None:
        self._thread_logging_manager = ThreadLoggingManager(n_workers = settings.LOGGING_N_WORKERS)
        self._thread_logging_manager.run_workers()
        super().__init__(level)

    def emit(self, record: logging.LogRecord) -> None:
        self._thread_logging_manager.add_record(record)


server_logger = logging.getLogger("server_logger")
server_logger.setLevel(settings.LOGGING_LEVEL)
server_logger.addHandler(MultiThreadingHandler())

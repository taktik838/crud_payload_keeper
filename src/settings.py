from enum import Enum
import os


# Logging
LOG_TO_FILE: bool = bool(int(os.getenv("LOG_TO_FILE", 0)))
PATH_TO_FILE: str = os.getenv("PATH_TO_FILE", "")
LOGGING_N_WORKERS: int = int(os.getenv("LOGGING_N_WORKERS", 4))

class LoggingLevel(str, Enum):
    CRITICAL = "CRITICAL"
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"
    DEBUG = "DEBUG"
    NOTSET = "NOTSET"

LOGGING_LEVEL: LoggingLevel = LoggingLevel(os.getenv("LOGGING_LEVEL", "DEBUG"))


# Mongo
MONGO_CONNECTION_STRING: str = os.getenv("MONGO_CONNECTION_STRING", "mongodb://localhost:27017")

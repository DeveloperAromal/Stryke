from datetime import datetime

class Logger:
    def __init__(self):
        pass  

    def _write_log(self, level: str, message: str):
        timestamp = datetime.now().strftime("%d/%m/%y - %H:%M:%S")
        log_entry = f"[{timestamp}] - {level.upper()} - {message}"
        print(log_entry)

    def info(self, message: str):
        self._write_log("info", message)

    def warn(self, message: str):
        self._write_log("warn", message)

    def error(self, message: str):
        self._write_log("error", message)

    def success(self, message: str):
        self._write_log("success", message)


logger = Logger()

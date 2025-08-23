from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True) 

class Logger:
    def __init__(self):
        pass  

    def _write_log(self, level: str, message: str):
        timestamp = datetime.now().strftime("%d/%m/%y - %H:%M:%S")

        if level.lower() == "info":
            color = Fore.CYAN
        elif level.lower() == "warn":
            color = Fore.YELLOW
        elif level.lower() == "error":
            color = Fore.RED
        elif level.lower() == "success":
            color = Fore.GREEN
        else:
            color = Fore.WHITE

        log_entry = f"{color}[{timestamp}] - {level.upper()} - {message}{Style.RESET_ALL}"
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

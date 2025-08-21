from colorama import Fore, Style, init
import datetime

init(autoreset=True)



"""

This is just a custom logging function 

"""
class Logging:
    def __init__(self, msg, msg_type="info"):
        self.msg = msg
        self.msg_type = msg_type.lower()

    def log_symbol(self):

        match self.msg_type:
            case "success":
                return "+"
            case "info":
                return "~"
            case "warn":
                return "!"
            case "error":
                return "x"
            case _:
                return "?"

    def log_color(self):

        match self.msg_type:
            case "success":
                return Fore.GREEN
            case "info":
                return Fore.CYAN
            case "warn":
                return Fore.YELLOW
            case "error":
                return Fore.RED
            case _:
                return Fore.WHITE

    def log(self):
        
      
        print(f"[{self.log_symbol()}] - [{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] - {self.msg}")
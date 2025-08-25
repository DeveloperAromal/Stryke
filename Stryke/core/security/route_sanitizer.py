import re

from utils.log import logger

"""

Some sql vunerable commands
that are harmfull to system

"""


sql_keywords = [
    "select", "drop", "insert", "delete", "update", "union", "alter", "create",
    "truncate", "replace", "exec", "execute", "merge", "call", "declare", "cast",
    "convert", "substr", "substring", "mid", "ascii", "char", "hex", "unhex",
    "floor", "rand", "benchmark", "sleep", "waitfor delay", "pg_sleep", "dbms_pipe.receive_message",
    "xp_cmdshell", "xp_reg", "load_file", "into outfile", "into dumpfile", "union all",
    "group by", "order by", "having", "where", "like", "and", "or", "not", "xor",
    "information_schema", "sys.databases", "master..sysdatabases", "version()", "@@version",
    "current_user", "database()", "user()", "current_database()",
    "--", "#", ";", "/*", "*/", "@@", "@",
    "admin'--", "admin'#", "admin'/*",
    "' or '1'='1", "' or 1=1 --", '" or "1"="1', '" or 1=1 --',
    "') or ('1'='1'--", "') or 1=1--",
    "') or 1=1 #", "') or ('a'='a",
    "'') or 1=1--",
    "' or 1=1 -- -", "' or 1=1-- -",
    "%27", "%22", "%3B", "%23", "%2D%2D",
    "<script>", "</script>", "<img", "<iframe", "<svg", "<body", "<a",
    "javascript:", "onload", "onerror", "onmouseover", "onclick", "onfocus",
    "alert(", "prompt(", "confirm(", "document.cookie", "window.location",
    "eval(", "src=", "href=", "style=", "data:text/html,", "data:text/javascript,",
    "xss", "xss_test", "throw 1", "location='javascript:", "alert`1`",
    "&#x", "&#", "%3c", "%3e", "%2f", "%22", "%27",
    "..", "../", "..\\", "....//", "%2e%2e%2f", "%2e%2e\\", "%252e%252e%252f",
    "%c0%af", "%c1%9c", "etc/passwd", "etc/shadow", "windows/system32", "web.config",
    "boot.ini", "c:\\", "/etc/",
    "null", "%00"
    "|", "||", "&", "&&", ";",
    "`", "$(", "<", ">",
    "ls", "cat", "more", "head", "tail", "whoami", "ifconfig", "ipconfig",
    "pwd", "id", "uname", "wget", "curl", "nc", "bash", "sh", "cmd", "powershell",
    "rm -rf", "rmdir /s /q",
    "nslookup", "ping",
    "unauthenticated", "authorization", "permission", "privilege",
    "access_denied", "forbidden", "restricted_access",
    "base64", "base64_decode", "eval", "system", "exec", "passthru"
]


def checkRoute(path: str) -> tuple[bool, str | None]:
    for keyword in sql_keywords:
        if keyword in path.lower():
            return False, keyword 
    return True, None

    


class RouteSanitizer:
    def __init__(self, path):
        self.path = path
    
    
    def sanitize(self):
        
        log = logger
        
        cleaned = re.sub(r"[^a-zA-Z0-9/_-]", "", self.path)
        cleaned = re.sub(r"/+", "/", cleaned)


        if not cleaned.startswith("/"):
            return ("/" + cleaned)
        
        
        safe, keyword = checkRoute(cleaned)
        
        if not safe:
            log.info(f"Malicious payload detected: {keyword} in path {self.path}")
            raise ValueError(f"Malicious payload in path: {keyword}")   
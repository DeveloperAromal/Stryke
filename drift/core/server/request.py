"""

Author: Aromal
github: https://github.com/DeveloperAromal/

"""



class Request:
    def __init__(self, method, path, body=None, headers=None):
        
        self.method = method
        self.path = path
        self.body = body
        self.headers = headers or {}
        



class Response:
    def __init__(self, content, status):
        
        self.content = content
        self.status = status
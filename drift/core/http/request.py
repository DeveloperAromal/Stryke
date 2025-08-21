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
        
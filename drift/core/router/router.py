"""
Author: Aromal
github: https://github.com/DeveloperAromal/

"""

class Router:
    
    def __init__(self):
        self.router = {}
        
    def add_router(self, method, path, func):
        self.router[(method.upper(), path)] = func
        
    """
    GET Req Decorator
    """
        
    def get(self, path):
        
        def decorator(func):
            self.add_router("GET", path, func)
            
            return func
        
        return decorator
    
    
    """
    POST Req Decorator
    """
    
    def post(self, path):
        
        def decorator(func):
            self.add_router("POST", path, func)
            
            return func
        
        return decorator
    
    
    def handle(self, method, path):
   
        key = (method.upper(), path)
        func = self.router.get(key)
        
        if func:
            return func()
        else:
            return f"404 Not Found: {method} {path}"
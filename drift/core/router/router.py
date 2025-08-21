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
            
            self.add_router(path, "GET", func)
            
            return func
        
        return decorator
    
    
    """
    
    POST Req Decorator
    
    """
    
    def post(self, path):
        
        def decorator(func):
            
            self.add_router(path, "POST", func)
            
            return func
        
        return decorator
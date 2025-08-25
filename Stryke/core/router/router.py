"""
Author: Aromal
github: https://github.com/DeveloperAromal/

"""
import inspect

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
    
    
    def handle(self, method, path, request_data=None):
   
        key = (method.upper(), path)
        func = self.router.get(key)
        
        if func:
            
            sig = inspect.signature(func)
            
            if sig.parameters:
                if isinstance(request_data, dict):
                    
                    try:
                        return func(**request_data)
                    
                    except (TypeError, ValueError) as e:
                        return f"400 Bad Request: Missing or incorrect arguments. Details: {e}"
                
                else:
                    return "400 Bad Request: Request data must be a valid mapping for this endpoint."
                
            else:
                return func()
        else:
            return f"404 Not Found: {method} {path}"
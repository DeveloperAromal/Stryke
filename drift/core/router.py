class Router:
    
    def __init__(self):
        self.router = {}
        
    def add_router(self, method, path, func):
        self.router[(method.upper(), path)] = func
        
        
        
    def get(self, path):
        
        def decorator(func):
            
            self.add_router(path, "GET", func)
            
            return func
        
        return decorator
    
    
    
    def post(self, path):
        
        def decorator(func):
            
            self.add_router(path, "POST", func)
            
            return func
        
        return decorator
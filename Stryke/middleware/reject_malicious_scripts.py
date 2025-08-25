from core.security import RouteSanitizer
from utils.log import logger
from functools import wraps


def safe(func):       
            
    @wraps(func)
                
    def wrapper(*args, **kwargs):
        
        
        if args:
            path = args[0]
        
        else:
            path = kwargs.get("path", "")
                    
        log = logger
            
        try:
            safe_path = RouteSanitizer(path).sanitize()
                        
            return safe_path
                    
        except ValueError as e:
            log.warn(f"Blocked request: {path} -> Reason: {e}")
            raise ValueError(f"Blocked request due to malicious payload: {e}")
                    
        return func(*args, **kwargs)
                
    return wrapper
        
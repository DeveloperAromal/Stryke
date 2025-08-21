from utils.log import Logging
from requests import Request


class Server:
    def __init__(self, router):
        self.router = router
        
        
    def run(self, method, path):

        
        log = Logging()
        
        log("Connected...", "success")
        log("Port Running on 3000 ...", "success")
        
        
        req = Request(method=method, path=path)

        handler = self.router.resolve(path, method)
        
        if handler:
            response = handler(req)
            Logging(f"Response: {response}", "info").log()
            
        else:
            Logging(f"No route found for {path}", "warn").log
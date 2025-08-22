from utils.log import Logging
from net.socket_server import SocketServer

class Server:
    def __init__(self, router):
        self.router = router
        self.sock_server = SocketServer()
        
        
        
    def run(self):
        def handler(raw_requests):
            return self.router.handle(raw_requests)

            
        self.sock_server.start(handler)
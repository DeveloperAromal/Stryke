from .net.socket_server import SocketServer

class Server:
    def __init__(self, router):
        self.router = router
        self.sock_server = SocketServer()
        
    def run(self):
        def handler(raw_requests):
            first_line = raw_requests.splitlines()[0]
            method, path, _ = first_line.split()
            
            return self.router.handle(method, path)

        self.sock_server.start(handler)
        
        
    
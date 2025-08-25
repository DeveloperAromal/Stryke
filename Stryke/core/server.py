"""
Author: Aromal
github: https://github.com/DeveloperAromal/

"""
from .net.socket_server import SocketServer
from middleware.reject_malicious_scripts import RouteSanitizer

class Server:
    def __init__(self, router):
        self.router = router
        self.sock_server = SocketServer()

    def run(self):
        def handler(method, path, request_data):
            
            try:
                RouteSanitizer(path).sanitize()
            except ValueError as e:
                print(f"Blocked request: {path} -> Reason: {e}")
                return "400 Bad Request: Malicious payload blocked"

            return self.router.handle(method, path, request_data)

        self.sock_server.start(handler)
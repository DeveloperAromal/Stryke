import socket
from utils.log import Logging



class SocketServer:
    def __init__(self, host="127.0.0.1", port="49250"):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.log = Logging()
        
    
    
    def start(self, handler):
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        
        self.log("Server started...", "success").log()
        self.log(f"Listening on {self.host}:{self.port}", "success").log()
        
        
        while True:
            client, addr = self.sock.accept()
            self.log(f"Connection from {addr}", "info")
            data = client.recv(1024).decode()
            

            
            if not data:
                client.close()
                continue
            
            
            response = handler(data)
            client.sendall(response.encode("utf-8"))
            client.close
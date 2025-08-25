"""
Author: Aromal
github: https://github.com/DeveloperAromal/

"""

import socket
import json
from utils.log import logger

class SocketServer:
    def __init__(self, host="127.0.0.1", port=49250):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.log = logger
        self.running = False

    def start(self, handler):
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        self.sock.settimeout(1.0) 

        self.log.success("Server started...")
        self.log.success(f"Listening on http://{self.host}:{self.port}")
        self.running = True

        try:
            while self.running:
                try:
                    client, addr = self.sock.accept()
                except socket.timeout:
                    continue 

                data = client.recv(1024).decode()

                if not data:
                    client.close()
                    continue

                request_line = data.splitlines()[0]
                if not request_line.startswith(("GET", "POST")):
                    client.close()
                    continue

                parts = request_line.split()
                if len(parts) >= 2:
                    method = parts[0]
                    path = parts[1]
                    self.log.info(f"Request from {addr}: {method} {path}")
                    
                    
                    request_data = None
                    
                    
                    if method == "POST":
                        body_start = data.find("\r\n\r\n")
                        
                        if body_start != -1:
                            body = data[body_start + 4:]
                            try:
                                request_data = json.loads(body)
                            except json.JSONDecodeError as e:
                                self.log.error(f"JSON decode error: {e}")
                                client.sendall(b"HTTP/1.1 400 Bad Request\r\nContent-Length: 0\r\n\r\n")
                                client.close()
                                continue
                        

                    try:
                        response_body = handler(method, path, request_data)
                        http_response = (
                            f"HTTP/1.1 200 OK\r\n"
                            f"Content-Type: text/plain\r\n"
                            f"Content-Length: {len(response_body)}\r\n\r\n"
                            f"{response_body}"
                        )
                        client.sendall(http_response.encode("utf-8"))
                        
                    except Exception as e:
                        self.log.error(f"Handler error: {e}")
                    finally:
                        client.close()
                else:
                    client.close()
                    
        except KeyboardInterrupt:
            self.log.success("Server stopping due to Ctrl+C...")
        finally:
            self.sock.close()
            self.log.success("Server socket closed.")
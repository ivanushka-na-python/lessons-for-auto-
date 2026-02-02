import socket
import json

class SocketApi():
    HEADERS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n' 
    HEADERS_404 = 'HTTP/1.1 404\r\nContent-Type: text/html; charset=utf-8\r\n\r\n' 
    HEADERS_JSON = 'HTTP/1.1 200 OK\r\nContent-Type: application/json; charset=utf-8\r\n\r\n'

    def __init__(self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            print(f'Working... on port {port}')
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind(('127.0.0.1', port))
            server.listen(4)

            client, address = server.accept()
            data = client.recv(1024).decode('utf-8')
            method, route = (data.split(' ')[0], data.split(' ')[1])
           
            print(data)

            self._server = server
            self._address = address
            self._data = data
            self._port = port

            self.client = client
            self.method = method
            self.route = route


    def send_html(self, path):
        with open(path) as file:
            content = file.read()
            raw = self.HEADERS + content
            self.client.send(raw.encode('utf-8'))


    def send_raw_html(self, content):
        raw = self.HEADERS + content
        self.client.send(raw.encode('utf-8'))

    
    def send_json(self, data):
        content = json.dumps(data)
        raw = self.HEADERS_JSON + content
        self.client.send(raw.encode('utf-8'))


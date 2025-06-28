# Filename:  simple_http_server.py
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, World!")

def run_server(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000) #Listen on all interfaces, port 8000
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()
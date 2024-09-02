from urllib import parse
from http.server import HTTPServer, SimpleHTTPRequestHandler

class servidorBasico(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.address_string()
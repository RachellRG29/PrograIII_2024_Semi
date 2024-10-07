import http.server
import socketserver
import os
import Autenticacion.logic_auth as logic_auth #importamos la logica del login y register
from urllib.parse import parse_qs

PORT = 3307

# Se estableció el directorio
DIRECTORY = "PrograIII_2024_semi"

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Modifica la ruta para que sirva desde el directorio especificado
        path = super().translate_path(path)
        return os.path.join(DIRECTORY, path.lstrip('/'))

    def do_GET(self):
        # Redirige la raíz a la página de inicio
        if self.path == '/':
            self.path = '/index_inicio.html'
        return super().do_GET()

    def do_POST(self):
        if self.path == '/register':
            self.handle_register()
        elif self.path == '/login':
            self.handle_login()
        else:
            self.send_error(404, "No encontrado :c ")

    def handle_register(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Llama a la función de registro en auth.py
        success, message = logic_auth.handle_register(post_data)

        if success:
            self.send_response(302)  # Redirige después del registro
            self.send_header('Location', '/Autenticacion/index_login.html')
            self.end_headers()
        else:
            self.send_response(400)  # Bad request
            self.end_headers()
            self.wfile.write(message.encode('utf-8'))

    # En el método handle_login
    def handle_login(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Llama a la función de login en logic_auth.py
        success, message = logic_auth.handle_login(post_data)

        if success:
            self.send_response(302)
            self.send_header('Location', '/Pantalla_princ/index_pant_prin.html')
            self.end_headers()
        else:
            # Redirige con un mensaje de error en la URL
            self.send_response(302)
            self.send_header('Location', f'/Autenticacion/index_login.html?error={message}')
            self.end_headers()


        def list_directory(self, path):
            # No muestra el listado del directorio
            self.send_error(403, "Forbidden")

# Configura el manejador de solicitudes
handler = CustomHTTPRequestHandler

# Crea el servidor
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Ejecutando en el puerto {PORT}")
    httpd.serve_forever()

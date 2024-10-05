import http.server
import socketserver
import os

#puerto 8000
PORT = 8000

#se establecio el diretorio 
DIRECTORY = "PrograIII_2024_semi"

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        #Modifica la ruta para que sirva desde el directorio especificado
        path = super().translate_path(path)
        return os.path.join(DIRECTORY, path.lstrip('/'))

    def do_GET(self):
        #Redirige la raíz a la pagina de inicio
        if self.path == '/':
            self.path = '/index_inicio.html'
        return super().do_GET()

    def list_directory(self, path):
        #no muestra el listado del directorio
        self.send_error(403, "Forbidden")

# Configura el manejador de solicitudes
handler = CustomHTTPRequestHandler

# Crea el servidor
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Ejecutando en el puerto {PORT}")
    httpd.serve_forever()

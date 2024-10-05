from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

# Clase que permite inicializar el servidor
class servidorBasico(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index_inicio.html' #para acceder a la pagina de inicio
        return SimpleHTTPRequestHandler.do_GET(self)

if __name__ == "__main__":
    servidor = HTTPServer(('0.0.0.0', 8080), servidorBasico)

    # Habilitar SSL/TLS
    servidor.socket = ssl.wrap_socket(servidor.socket,
                                      keyfile="server.pem",
                                      certfile="server.pem",
                                      server_side=True)

    print("Servidor HTTPS corriendo en el puerto 8080...")
    servidor.serve_forever()


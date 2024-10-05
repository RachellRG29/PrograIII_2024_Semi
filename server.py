import http.server
import socketserver
import os
import mysql.connector
import urllib.parse 
from urllib.parse import parse_qs

PORT = 3307

# Se establece el directorio 
DIRECTORY = "PrograIII_2024_semi"

# Conexión a la base de datos
def db_connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db_consolexpress"
    )

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
            self.send_error(404, "Not Found :c ")

#--REGISTER-----------------
    def handle_register(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = parse_qs(post_data.decode('utf-8'))

        # Verifica si las claves existen
        if 'username' not in data or 'email' not in data or 'password' not in data or 'confirm_password' not in data:
            self.send_response(400)  # Bad request
            self.end_headers()
            self.wfile.write(b'Missing fields in registration form.')
            return

        username = data['username'][0]
        email = data['email'][0]
        password = data['password'][0]
        confirm_password = data['confirm_password'][0]

        if password != confirm_password:
            self.send_response(400)
            self.end_headers()
            self.wfile.write('Las contraseñas no coinciden.')
            return

        # Conectar a la base de datos
        conn = db_connect()
        cursor = conn.cursor()

        # Inserta el registro en la tabla
        try:
            cursor.execute("INSERT INTO register (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
            conn.commit()
        except mysql.connector.Error as err:
            self.send_response(500)  # Internal Server Error
            self.end_headers()
            self.wfile.write(b'Error en la base de datos: No se pudo registrar al usuario.')
            cursor.close()
            conn.close()
            return  

        cursor.close()
        conn.close()

        # Redirigir al inicio de sesión después de registrarse
        self.send_response(302)  # Redirige después del registro
        self.send_header('Location', '/Autenticacion/index_login.html')
        self.end_headers()

#-----LOGIN-------------
    def handle_login(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = parse_qs(post_data.decode('utf-8'))

        # Extrae los datos
        if 'username' not in data or 'password' not in data:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'Missing fields in login form.')
            return

        username = data['username'][0]
        password = data['password'][0]

        # Conectar a la base de datos
        conn = db_connect()
        cursor = conn.cursor()

        # Verifica el login
        cursor.execute("SELECT * FROM register WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user:
            self.send_response(302)
            self.send_header('Location', '/Pantalla_princ/index_pant_prin.html')
            self.end_headers()  # Corrección aquí
        else:
            self.send_response(401)
            self.end_headers()
            self.wfile.write('Usuario o contraseña inválidos.')

    def list_directory(self, path):
        # No muestra el listado del directorio
        self.send_error(403, "Forbidden")  

# Configura el manejador de solicitudes
handler = CustomHTTPRequestHandler

# Crea el servidor
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Ejecutando en el puerto {PORT}")
    httpd.serve_forever()

#----LOGICA PARA EL FUNCIONAMIENTO DEL LOGIN Y REGISTER
import mysql.connector
from urllib.parse import parse_qs
from flask import Flask, jsonify,render_template, request

app= Flask(__name__)

# Para conectar a la base de datos
def db_connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db_consolexpress"
    )

# Maneja el registro de los usuarios
def handle_register(post_data):
    data = parse_qs(post_data.decode('utf-8'))

    if 'username' not in data or 'email' not in data or 'password' not in data or 'confirm_password' not in data:
        return False, 'Missing fields in registration form.'

    username = data['username'][0]
    email = data['email'][0]
    password = data['password'][0]
    confirm_password = data['confirm_password'][0]

    if password != confirm_password:
        return jsonify({
            "message": "por favor ingrese su contraseña",
            "success": False
        })

    #return False, 'Las contraseñas no concuerdan :c'

    # Conectar a la base de datos
    conn = db_connect()
    cursor = conn.cursor()

    # Inserta el registro en la tabla register
    try:
        cursor.execute("INSERT INTO register (username, email, password, confirm_password) VALUES (%s, %s, %s, %s)", (username, email, password, confirm_password))
        conn.commit()
        success = True
        message = 'Registro exitoso.'
    except mysql.connector.Error as err:
        success = False
        message = 'Error en la base de datos: Could not register user.'
    
    cursor.close()
    conn.close()

    return success, message

# Maneja el inicio de sesión
def handle_login(post_data):
    data = parse_qs(post_data.decode('utf-8'))

    if 'username' not in data or 'password' not in data:
        return False, 'Faltan campos en el formulario de inicio de sesión.'

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
        return True, 'Inicio de sesión exitoso.'
    else:
        return False, 'Usuario o contraseña incorrectos.'

import mysql.connector
from urllib.parse import parse_qs
from flask import Flask, jsonify,render_template, request

app= Flask(__name__)

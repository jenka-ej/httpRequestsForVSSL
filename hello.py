from flask import Flask
import requests

app = Flask(__name__)

@app.route("/resume17", methods=['POST'])
def resume17():
    requests.patch('http://localhost:8000/api/setplaycontrol?serial=CC909321FDDD&number=2&playstate=0')

@app.route("/pause17", methods=['POST'])
def pause17():
    requests.patch('http://localhost:8000/api/setplaycontrol?serial=CC909321FDDD&number=2&playstate=2')

@app.route("/resume21", methods=['POST'])
def resume21():
    requests.patch('http://localhost:8000/api/setplaycontrol?serial=CC909321FDDD&number=3&playstate=0')

@app.route("/pause21", methods=['POST'])
def pause21():
    requests.patch('http://localhost:8000/api/setplaycontrol?serial=CC909321FDDD&number=3&playstate=2')


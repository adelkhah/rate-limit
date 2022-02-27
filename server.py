from bottle import Bottle, route, run, response, static_file, request
from json import dumps
from multiprocessing import Process
import requests
import sys
from pathlib import Path
import threading
import datetime


app = Bottle()

blocked_ip = []
last_request_time = {}
username = "username"
password = "password"

@app.route('/login', method='POST')
def login():
    body = request.json
    req_time = datetime.datetime.now()
    client_ip = request.environ.get('HTTP_X_FORWARDED_FOR') or request.environ.get('REMOTE_ADDR')
    if client_ip in blocked_ip:
        print("you are blocked")
        return 500

    if body["username"] == username and body["password"] == password:
        print("login saccesfully")
    else:
        if client_ip in last_request_time.keys():

            delta = req_time - last_request_time[client_ip]

            if delta < datetime.timedelta(seconds=3):
                blocked_ip.append(client_ip)
                print("next time block")
            else:
                last_request_time[client_ip] = req_time
                print("incorrect username or password")
        else:
            last_request_time[client_ip] = req_time
            print("incorrect username or password")

@app.route('/myIP')
def myIP():
    client_ip = request.environ.get('HTTP_X_FORWARDED_FOR') or request.environ.get('REMOTE_ADDR')
    print(['Your IP is: {}\n'.format(client_ip)])



app.run(host='localhost', port=8080)


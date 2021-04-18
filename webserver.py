from flask import Flask
from flask import render_template
import requests
API_ENDPOINT = 'https://discord.com/api/v8'
from threading import Thread
import json
with open('config.json') as f:
  config = json.load(f)
app = Flask('', static_url_path='/webserver/static')

def exchange_code(code):
  data = {
    'client_id': config['client_id'],
    'client_secret': config['client_secret'],
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': config['redirect'],
    'scope': config['scopes']
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  r = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers)
  r.raise_for_status()
  return r.json()

@app.route('/')
def home():
    f = open("webserver/html/index.html", "r")
    return f.read()

@app.route('/')
def getaccesstoken():
    f = open("webserver/html/index.html", "r")
    return f.read()
    
def run():
  app.run(host="0.0.0.0",port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()
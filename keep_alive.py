from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    line="Hey There! I'm Pari the bot. This web server exists cause I need Regular pings to stay alive :(("
    return line

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

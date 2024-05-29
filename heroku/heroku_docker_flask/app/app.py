from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return os.environ.get("TESTVAR", "no value set")

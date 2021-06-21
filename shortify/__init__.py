from flask import Flask
import os

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SHORTIFY_SECRET_KEY")

from shortify import routes
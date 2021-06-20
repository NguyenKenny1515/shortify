from flask import Flask

app = Flask(__name__)

app.config["SECRET_KEY"] = "38ef006410412179afdc6a63ab9d1b09"

from shortify import routes
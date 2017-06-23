from flask import Flask, send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
db = SQLAlchemy(app)


@app.route("/media/<path:file>")
def send_media(file):
    return send_from_directory(directory=config.MEDIA_PATH, filename=file)


@app.route('/')
def landing_page():
    return _send_template("landing_page.html")


@app.route('/asak')
def asak():
    return _send_template("asak.html")


@app.route('/asak')
def categories():
    return _send_template("asak.html")


def _send_template(file):
    return send_from_directory(directory=config.TEMPLATES_PATH, filename=file)


if __name__ == '__main__':
    app.run(debug=config.DEBUG)

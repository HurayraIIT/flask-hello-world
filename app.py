from flask import Flask, request, render_template, url_for, send_from_directory
import requests

app = Flask(__name__, static_folder='static')
application = app


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == "__main__":
    app.run(debug=True)
    
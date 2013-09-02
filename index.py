from flask import Flask, request, make_response, redirect, url_for, Response
from cdata import CData
import os


app = Flask(__name__)
cd = CData()


@app.route("/")
def hello():
    return "hello"


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cd.create_token(username, password)
        return redirect('/apps')
    else:
        return redirect(url_for('static', filename='login.html'))


@app.route("/apps")
def get_apps():
    # return "apps"
    return cd.get_apps()

@app.route("/<appname>")
def get_app_info(appname):
    return cd.get_info(appname)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=int(os.environ['PORT']))

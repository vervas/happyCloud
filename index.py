from flask import Flask
from cdata import CData
import os


app = Flask(__name__)
cd = CData()


@app.route("/")
def hello():
    return "Welcome"


@app.route("/<appname>")
def get_app_info(appname):
    cd.create_token('at+happycloud@cloudcontrol.de', 'malaka')
    return cd.get_info(appname)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=int(os.environ['PORT']))

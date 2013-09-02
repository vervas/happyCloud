from flask import Flask
from cdata import CData
app = Flask(__name__)
cd = CData()


@app.route("/")
def hello():
    return "Welcome"


@app.route("/<appname>")
def get_app_info(appname):
    cd.api.set_token('fn7tFd4ALwk2yYcnd9Tqqqn38TYG2S')
    return cd.get_info(appname)


if __name__ == "__main__":
    app.run()

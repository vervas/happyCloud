from flask import Flask
from cdata import CData
app = Flask(__name__)
cd = CData()


@app.route("/")
def hello():
    return "Welcome"


@app.route("/face/<face>")
def get_app_face(face):
    return cd.get_face(face)


@app.route("/<appname>")
def get_app_info(appname):
    cd.api.set_token('fn7tFd4ALwk2yYcnd9Tqqqn38TYG2S')
    import pdb; pdb.set_trace()
    return cd.get_apps()


if __name__ == "__main__":
    app.run()

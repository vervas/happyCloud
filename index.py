from flask import Flask
from cdata import CData
app = Flask(__name__)

@app.route("/")
def hello():
    cdata = CData()
    return "Welcome"

if __name__ == "__main__":
    app.run()

from flask import (Flask,
                   render_template,
                   request)
import socket


app = Flask(__name__)


@app.route('/')
def index():
    hostname = socket.gethostname()
    requester = request.remote_addr
    context = {
        "hostname": hostname,
        "requester": requester
    }
    return render_template("index.html", context=context)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5789, debug=True)

from flask import (Flask,
                   render_template,
                   request)
import socket


app = Flask(__name__)


@app.route('/')
def index():
    hostname = socket.gethostname()
    hosting_ip = socket.gethostbyname(hostname)
    requester = request.remote_addr
    context = {
        "hostname": hostname,
        "hosting_ip": hosting_ip,
        "requester": requester,
    }
    print(context)
    return render_template("index.html", context=context)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5789, debug=True)

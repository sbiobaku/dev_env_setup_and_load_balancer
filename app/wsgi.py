#/usr/local/bin/python3
from flask import Flask
from flask import jsonify 
from flask import render_template
import redis
import socket
import debugpy
debugpy.listen(("0.0.0.0", 5678))



app = Flask(__name__)

r = redis.Redis(host="redis", port=6379)

@app.route('/')
def Hello_world():
    return render_template("index.html", hostname=socket.gethostname())

@app.route('/health')
def health():
    return jsonify( status="down")

@app.route("/hits")
def hits():
    r.incr("hits")
    num_hits = r.get("hits").decode("utf-8")
    return num_hits
    #return render_template("hits.html", hits="fuck you")

if __name__ == "__main__":
    app.run(debug=True)
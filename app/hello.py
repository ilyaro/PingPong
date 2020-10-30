import flask
from flask import request
import shlex, subprocess
import sys

app = flask.Flask(__name__)


@app.route("/")
def hello():
    return "PingPong Game of 2 Microservices"

@app.route("/pingpong")
def pingpong():
    iterations = request.args.get('iterations')
    return "Number of PingPong iterations: " + iterations

@app.route("/intense")
def intense():
    def load_cpu():
        """
        Run a cpu load command for 60 seconds.
        """
        ## Prinet the message first
        yield "CPU will be load for 60 seconds" + "<br/>\n"
        ##seconds = "6"
        try:
             proc = subprocess.Popen(['/usr/bin/stress --cpu 4 --timeout 6'],shell=True)
             proc.communicate()
        finally:
           pass 
        yield "Done - The CPU was loaded now for 60 seconds"
    return flask.Response(load_cpu(), mimetype='text/html') 



if __name__ == "__main__":
    ## Add check if port number is a numbers in the port allowed range
    inport = int(sys.argv[1])
    app.run(host='0.0.0.0', port=inport)

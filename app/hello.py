import flask
import shlex, subprocess

app = flask.Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"

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
    app.run(host='0.0.0.0', port=8089)

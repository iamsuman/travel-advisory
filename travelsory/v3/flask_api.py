import flask
from travelsory.v3 import lookup


app = flask.Flask(__name__)
# app.config["DEBUG"] = True



@app.route("/health", methods=["GET"])
def health():
    return "{\"code\":200,\"status\":\"ok\"}"

@app.route("/diag", methods=["GET"])
def diag():
    return "{\"code\":200,\"status\":\"ok\"}"

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000)
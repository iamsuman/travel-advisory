import flask

app = flask.Flask(__name__)
#app.config["DEBUG"] = True


@app.route("/health", methods=["GET"])
def home():
    return "{\"code\":200,\"status\":\"ok\"}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
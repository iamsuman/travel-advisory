from flask import Flask, request
from travelsory.v3 import lookup

RESPONSE_TEMPLATE = {
    "api_status": {
        "request": {
            "item": ""
        },
        "reply": {
            "cache": "",
            "code": "",
            "status": "",
            "note": "",
            "count": ""
        }
    },
    "data": ""
}

app = Flask(__name__)
# app.config["DEBUG"] = True


@app.route("/health", methods=["GET"])
def health():
    return "{\"code\":200,\"status\":\"ok\"}"


@app.route("/diag", methods=["GET"])
def diag():
    response = {
    "api_status": {
        "request": {
            "item": ""
        },
        "reply": {
            "cache": "",
            "code": 200,
            "status": "ok",
            "note": "Diag test",
            "count": "0"
        }
    },
    "data": False
}
    return response


@app.route("/convert", methods=["GET"])
def convert():
    req_dict = request.args
    if req_dict.get("countryCode"):
        countrycode = req_dict["countryCode"]
        return "countryCode is " + countrycode
    else:
        return


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

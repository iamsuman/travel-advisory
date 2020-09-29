from flask import Flask, request, jsonify
from travelsory.v3.travel import lookup

response_template = {
    "api_status": {
        "request": {
            "item": ""
        },
        "reply": {
            "cache": "cached",
            "code": 200,
            "status": "ok",
            "note": "",
            "count": "0"
        }
    },
    "data": False
}

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"code":200,"status":"ok"})


@app.route("/diag", methods=["GET"])
def diag():
    response = response_template
    response["note"] = "Diag test"
    return jsonify(response)


@app.route("/convert", methods=["GET"])
def convert():
    req_dict = request.args
    code = 404
    result_json = {}
    if req_dict.get("countryCode"):
        input_value = req_dict["countryCode"]
        for country_code in input_value.split(","):
            country = core.get_country(data, country_code)
            if country != "404: Country Code does not exist":
                code = 200
            result_json[country_code] = {}
            result_json[country_code]["country_code"] = country_code
            result_json[country_code]["name"] = core.get_country(data, country_code)

    response = response_template
    if code == 200:
        response["data"] = result_json
        response["api_status"]["reply"]["count"] = len(result_json)
        response["api_status"]["reply"]["note"] = \
            "The api works, we could match requested country code."
    else:
        response["api_status"]["reply"]["status"] = "Not Found"
        response["api_status"]["reply"]["note"] = \
            "The api works, but we could not find the item you were looking for."

    response["api_status"]["reply"]["code"] = code
    return jsonify(response)


if __name__ == "__main__":
    core = lookup.Core()
    data = core.load_travel_data("data.json")
    app.run(host='0.0.0.0', port=5000)

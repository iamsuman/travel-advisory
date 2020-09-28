import argparse
import json
import sys


# def parse_cli():
#     parser = argparse.ArgumentParser(
#         description="Program to lookup countrycode",
#         formatter_class=argparse.RawDescriptionHelpFormatter,
#         epilog="Doc: https://github.com/iamsuman/travel-advisory")
#     parser.add_argument("-c", "--countryCode", help="countryCode", required=True, default="")
#     args = parser.parse_args()
#     return args

def parse_cli():
    parser = argparse.ArgumentParser(
        description="Program to lookup countrycode",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Doc: https://github.com/iamsuman/travel-advisory")
    parser.add_argument("-c", "--countryCode", help="countryCode", required=True, default="")
    args = parser.parse_args()
    return args


def validate_args(country_code):
    if country_code.isalpha():
        return "alpha"
    else:
        try:
            # country_code = '{"countryCode":["AU", "AD"]}'
            out = json.loads(country_code)
            if out.get("countryCode"):
                if isinstance(out.get("countryCode"), list):
                    return "json"
        except:
            sys.exit("Not a valid input, need json format like \'{\"countryCode\":[\"AU\", \"AD\"]}\'")


def load_travel_data(file_name):
    with open("data.json", "r") as json_file:
        country_dict = json.load(json_file)
    data = country_dict["data"]
    return data


def get_country(data, country_code):
    if data.get(country_code):
        return data[country_code]["name"]
    else:
        return "404: Country Code does not exist"


def main():
    args = parse_cli()
    data = load_travel_data("data.json")
    input_type = validate_args(args.countryCode)
    if input_type == "alpha":
        country = get_country(data, args.countryCode)
        print(country)
    elif input_type == "json":
        input_dict = json.loads(args.countryCode)
        result_json = {}
        for country_code in input_dict["countryCode"]:
            result_json[country_code] = get_country(data, country_code)
        print(result_json)


if __name__ == "__main__":
    main()

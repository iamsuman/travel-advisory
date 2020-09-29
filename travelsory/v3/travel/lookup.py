import argparse
import json
import sys


class Core:
    # def ___init__(self):

    def parse_cli(self):
        parser = argparse.ArgumentParser(
            description="Program to lookup countrycode",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="Doc: https://github.com/iamsuman/travel-advisory")
        parser.add_argument("-c", "--countryCode", help="countryCode", required=True, default="")
        args = parser.parse_args()
        return args

    def validate_args(self, country_code):
        if country_code.isalpha():
            return "alpha"
        elif isinstance(country_code, list):
            return "list"
        else:
            try:
                # country_code = '{"countryCode":["AU", "AD"]}'
                out = json.loads(country_code)
                if out.get("countryCode"):
                    if isinstance(out.get("countryCode"), list):
                        return "json"
            except:
                sys.exit("Not a valid input, need json format like \'{\"countryCode\":[\"AU\", \"AD\"]}\'")

    def load_travel_data(self, file_name):
        with open(file_name, "r") as json_file:
            country_dict = json.load(json_file)
        data = country_dict["data"]
        return data

    def get_country(self, data, country_code):
        if data.get(country_code):
            return data[country_code]["name"]
        else:
            return "404: Country Code does not exist"

    def execute(self, args):
        data = self.load_travel_data("data.json")
        input_type = self.validate_args(args.countryCode)
        if input_type == "alpha":
            country = self.get_country(data, args.countryCode)
            print(country)
        elif input_type == "json":
            input_dict = json.loads(args.countryCode)
            result_json = {}
            for country_code in input_dict["countryCode"]:
                result_json[country_code] = self.get_country(data, country_code)
            print(result_json)


def main():
    core = Core()
    args = core.parse_cli()
    core.execute(args)


if __name__ == "__main__":
    main()

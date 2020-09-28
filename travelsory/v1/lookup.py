import requests
import argparse

URL = "https://www.travel-advisory.info/api"


def parse_cli():
    parser = argparse.ArgumentParser(
        description="Program to lookup countrycode",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Doc: https://github.intuit.com/iamsuman")
    parser.add_argument("-c", "--countryCode", help="countryCode", required=True, default="")
    args = parser.parse_args()
    return args


def get_country(country_code):
    url = URL + "?countrycode=" + country_code
    # print(url)
    response = requests.get(url).json()
    # print(response["api_status"])
    api_status = response["api_status"]
    if api_status["reply"]["status"] == "ok" and api_status["request"]["item"] == str(country_code).lower():
        return response["data"][country_code]["name"]
    else:
        return api_status["reply"]["code"] + " " + api_status["request"]["item"]


def main():
    args = parse_cli()
    # print(args.countryCode)
    country = get_country(args.countryCode)
    print(country)


if __name__ == "__main__":
    main()


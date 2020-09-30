import requests
import argparse
# from requests import exceptions
import sys

class Monitor:
    # def ___init__(self):

    def parse_cli(self):
        parser = argparse.ArgumentParser(
            description="Program to Monitor rest api",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="Doc: https://github.com/iamsuman/travel-advisory")
        parser.add_argument("-u", "--url", help="URL of Rest API", required=True, default="")
        args = parser.parse_args()
        return args

    def monitor(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                response_json = response.json()
                if response_json.get("code") == 200:
                    return response_json
                else:
                    return {"code": 204, status: "ok"}
            else:
                return {"code": response.status_code, status: ""}
        except requests.exceptions.ConnectionError as err:
            return {"code": 521, "status": err}

    def send_page(self, url, status_code, status_msg):
        print("There is issue with Service {}".format(url))
        print("{}:{}".format(status_code,status_msg))
        pass


def main():
    mon = Monitor()
    args = mon.parse_cli()
    status = mon.monitor(args.url)
    if status["code"] != 200:
        mon.send_page(args.url, status["code"], status["status"])
    else:
        print("Success")


if __name__ == "__main__":
    main()
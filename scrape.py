import requests
import threading
import gsheets
import json


def get_ap_file(file_location):
    r = requests.get(file_location)
    return r.text


def run_ap_periodically(file_location, time_interval, i, parse_func):
    i += 1
    if i > 5:
        exit(0)
    t = threading.Timer(time_interval, lambda: run_ap_periodically(
        file_location, time_interval, i, parse_func))
    t.start()
    text = get_ap_file(file_location)
    response = json.loads(parse_func(text))
    gsheets.send_to_sheets(response["president"]["ev"]["dem"],
                           response["president"]["ev"]["gop"],
                           response["senate"]["seats"]["dem"],
                           response["senate"]["seats"]["gop"],
                           response["house"]["seats"]["dem"],
                           response["house"]["seats"]["gop"])

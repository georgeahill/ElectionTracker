import requests
import json
import scrape
# https://interactives.ap.org/2016/general-election/?SITE=APQA


def json_parsing(json_text):
    pass


def bop_parse(json_text):
    with open('response.json', 'r') as f:
        return f.read()


if __name__ == '__main__':
    json_text = scrape.get_ap_file(
        "https://interactives.ap.org/interactives/2016/general-election/live-data/production/2016-11-08/bop.json")
    json_parsing(json_text)

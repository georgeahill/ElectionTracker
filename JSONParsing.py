import requests
import json
import scrape
# https://interactives.ap.org/2016/general-election/?SITE=APQA


def json_parsing(json_text):

    


    senateSeats = {"gop":gopSenateSeats,"dem":demSenateSeats,"other":otherSenateSeats}
    senateStates = {"gop":gopSenateStates,"dem":demSenateStates,"other":otherSenateStates}
    houseSeats = {"gop":gopHouseSeats,"dem":demHouseSeats,"other":otherHouseSeats}
    houseStates = {"gop":gopHouseStates,"dem":demHouseStates,"other":otherHouseStates}
    ev = {"gop":gopEv,"dem":demEv,"other":otherEv}
    presStates = {"gop":gopPresStates,"dem":demPresStates,"other":otherPresStates}
    senate = {"seats": senateSeats, "states": senateStates}
    house = {"seats": houseSeats, "states": houseStates}
    president = {"ev": ev, "states": presStates}
    newJson = {"president": president, "house": house, "senate": senate}
    return json.dumps(newJson)


def bop_parse(json_text):
    with open('response.json', 'r') as f:
        return f.read()


if __name__ == '__main__':
    json_text = scrape.get_ap_file("https://interactives.ap.org/interactives/2016/general-election/live-data/production/2016-11-08/bop.json")
    json_parsing(json_text)

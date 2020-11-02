import requests
import json
import scrape
# https://interactives.ap.org/2016/general-election/?SITE=APQA


def json_parsing(json_text):
    #string converted to json
    json_text = json.loads(json_text)
    #gets data from json
    presidentData = json_text["president"]
    senateData = json_text["senate"]
    houseData = json_text["house"]

    gopPresidentData = presidentData["gop"]
    demsPresidentData = presidentData["dem"]

    gopSenateData = senateData["gop"]
    demSenateData = senateData["dem"]

    gopHouseData = houseData["gop"]
    demHouseData = houseData["dem"]

    gopEv = gopPresidentData["count"]
    demEv = demsPresidentData["count"]
    otherEv = 0

    gopPresStates = 0
    demPresStates = 0
    otherPresStates = 0

    gopSenateSeats = gopSenateData["count"]
    demSenateSeats  = demSenateData["count"]
    otherSenateSeats = 0
    
    gopSenateStates = 0
    demSenateStates = 0
    otherSenateStates = 0

    gopHouseSeats = gopHouseData["count"]
    demHouseSeats = demHouseData["count"]
    otherHouseSeats = 0

    gopHouseStates = 0
    demHouseStates = 0
    otherHouseStates = 0



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
    print(json_parsing(json_text))

import requests
import json
import scrape
import datetime
# https://interactives.ap.org/2016/general-election/?SITE=APQA


def json_parsing(json_text,house_json_text,evDict):
    #wont run until, evDict is sent in
    #please send me the house_json_test from the gardian

    #json_text arguement is for the president JSON
    #evDict is the dictonary you are gonna send me with all the electoral votes and corresponding state names
    #e.g. evDict = {'AZ':23,'CO':2}

    #string converted to json
    json_text = json.loads(json_text)
    #gets data from json
    gopEv = 0
    demEv = 0
    otherEv = 0

    for state in json_text:
        if state == "US":
            pass
        else:
            stateWinner = json_text[state]['winner']
            #please make sure dict uses same abrivations as the file
            stateEv = evDict[state]
            if stateWinner == "Trump":
                gopEv = gopEv + stateEv
            elif stateWinner == "Biden":
                demEv = demEv + stateEv
            else:
                otherEv = otherEv + stateEv 
    
    #house and senate data
    house_json_text = json.loads(house_json_text)
    
    senateData = house_json_text["Senate"]
    houseData = house_json_text["House"]

    wonHouseData = houseData["won"]

    gopHouseSeats = wonHouseData["R"]
    demHouseSeats = wonHouseData["D"]
    otherHouseSeats = wonHouseData["O"]

    totalSenateData = senateData["seats"]
    
    gopSenateSeats = totalSenateData["R"]
    demSenateSeats = totalSenateData["D"]
    otherSenateSeats = totalSenateData["O"]
    

    #old code, kept it here just in case
    #will delete once finished
    '''
    presidentData = json_text["president"]


    gopPresidentData = presidentData["gop"]
    demsPresidentData = presidentData["dem"]

    gopSenateData = senateData["gop"]
    demSenateData = senateData["dem"]

    gopHouseData = houseData["gop"]
    demHouseData = houseData["dem"]

    try:
        gopEv = gopPresidentData["count"]
        if gopEv is None or gopEv =='':
            gopEv = 0 
    except :
        gopEv = 0
    try:
        demEv = demsPresidentData["count"]
        if demEv is None or demEv =='':
            demEv = 0 
    except:
        demEv = 0
    otherEv = 0

    try:
        gopSenateSeats = gopSenateData["count"]
        if gopSenateSeats is None or gopSenateSeats =='':
            gopSenateSeats = 0 
    except:
        gopSenateSeats = 0
    try:
        demSenateSeats  = demSenateData["count"]
        if demSenateSeats is None or demSenateSeats =='':
            demSenateSeats = 0 
    except:
        demSenateSeats =0
    otherSenateSeats = 0 

    try:
        gopHouseSeats = gopHouseData["count"]
        if gopHouseSeats is None or gopHouseSeats =='':
            gopHouseSeats = 0 
    except:
        gopHouseSeats = 0
    try:
        demHouseSeats = demHouseData["count"]
        if demHouseSeats is None or demHouseSeats =='':
            demHouseSeats = 0 
    except:
        demHouseSeats = 0
    otherHouseSeats = 0
    '''

    #fills in the blanks for jason
    gopPresStates = 0
    demPresStates = 0
    otherPresStates = 0

    gopHouseStates = 0
    demHouseStates = 0
    otherHouseStates = 0

    gopSenateStates = 0
    demSenateStates = 0
    otherSenateStates = 0




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
    #just some tests I ran
    #2020-11-04T00:58:15.843+00:00
    #print(datetime.datetime.now())
    gardien_time = scrape.get_ap_file("https://interactive.guim.co.uk/2020/11/us-general-election-data/prod/last_updated.json") 
    currentTime = json.loads(gardien_time)
    house_info = scrape.get_ap_file("https://interactive.guim.co.uk/2020/11/us-general-election-data/prod/data-out/"+currentTime["time"]+"/topline.json")
    #print(house_info)
    #json_text = scrape.get_ap_file("https://interactives.ap.org/interactives/2016/general-election/live-data/production/2016-11-08/bop.json")
    #json_text= (open('sampleData.json','r')).read()
    #print(json_parsing(json_text,house_info))
    

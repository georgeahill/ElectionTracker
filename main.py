import scrape
import JSONParsing
import gsheets


def main():
    bop_file = "https://interactives.ap.org/interactives/2016/general-election/live-data/production/2016-11-08/bop.json"
    pres_file = "https://interactives.ap.org/interactives/2016/general-election/live-data/production/2016-11-08/president.json"
    gsheets.authgsheet()

    #steals the gardiens time and then wacks it into the url
    gardien_time = scrape.run_ap_periodically("https://interactive.guim.co.uk/2020/11/us-general-election-data/prod/last_updated.json") 
    currentTime = json.loads(gardien_time)
    #make sure you send the house_file over to the JSON parsing fucntion else it wont work
    house_file = scrape.run_ap_periodically("https://interactive.guim.co.uk/2020/11/us-general-election-data/prod/data-out/"+currentTime["time"]+"/topline.json")


    scrape.run_ap_periodically(
        "https://interactives.ap.org/interactives/2016/general-election/live-data/production/2016-11-08/bop.json", 10.0, 0, JSONParsing.bop_parse)
    # run_ap_periodically("https://interactives.ap.org/interactives/2016/general-election/live-data/production/2016-11-08/president.json", 10.0, 0, JSONParsing.pres_parse)

    

if __name__ == '__main__':
    main()

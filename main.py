import scrape
import JSONParsing
import gsheets


def main():
    bop_file = "https://interactives.ap.org/interactives/2016/general-election/live-data/production/2016-11-08/bop.json"
    pres_file = "https://interactives.ap.org/interactives/2016/general-election/live-data/production/2016-11-08/president.json"
    gsheets.authgsheet()

    scrape.run_ap_periodically(
        "https://interactives.ap.org/interactives/2016/general-election/live-data/production/2016-11-08/bop.json", 10.0, 0, JSONParsing.bop_parse)
    # run_ap_periodically("https://interactives.ap.org/interactives/2016/general-election/live-data/production/2016-11-08/president.json", 10.0, 0, JSONParsing.pres_parse)


if __name__ == '__main__':
    main()

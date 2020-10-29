import requests
import threading


def get_ap_file(file_location):
    r = requests.get(file_location)
    return r.text


def run_ap_periodically(file_location, time_interval, i):
    i += 1
    if i > 5:
        exit(0)
    t = threading.Timer(time_interval, lambda: run_ap_periodically(file_location, time_interval, i))
    t.start()
    text = get_ap_file(file_location)
    print(text[:20])

if __name__ == '__main__':
    run_ap_periodically("https://interactives.ap.org/interactives/2016/general-election/live-data/production/2016-11-08/bop.json", 5.0, 0)
    run_ap_periodically("https://interactives.ap.org/interactives/2016/general-election/live-data/production/2016-11-08/president.json", 5.0, 0)
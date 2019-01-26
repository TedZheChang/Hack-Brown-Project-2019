import requests
from bs4 import BeautifulSoup

class Scraper:

    def scrapeRatty(self):

        url = "https://dining.brown.edu/cafe/sharpe-refectory"
        r = requests.get(url)
        c = r.content
        html = BeautifulSoup(c, 'html.parser')
        specials = html.find_all('button', {'class': 'h4 site-panel__daypart-item-title'})

        for special in specials:
            if "chicken finger" in special.text:
                return \
            {
            "conf": "Ratty has Chicken Fingers",
            "stat": "Helllll yeah"
            }
        return \
        {
            "conf": "Ratty does not have Chicken Fingers",
            "stat": "Guess I'll die then"
        }
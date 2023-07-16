import requests
from selectorlib import Extractor


class Temperature:
    """
    Represent a temperature value extracted from timeanddate.com/weather_webpage.
    """

    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    static_url = 'https://www.timeanddate.com/weather/'
    yaml_path = 'temperature.yaml'

    def __init__(self, country, city):
        self.country = country.replace(' ', '-')
        self.city = city.replace(' ', '-')

    def _build_url(self):
        """
        Builds the url concatenating country and city name
        """
        return self.static_url + self.country + '/' + self.city

    def _scrape(self):
        """
        Extracts a value as instructed by the .yaml file and returns a dictionary
        """
        url = self._build_url()
        extractor = Extractor.from_yaml_file(self.yaml_path)
        request = requests.get(url, headers=self.headers)
        content = request.text
        return extractor.extract(content)

    def get(self):
        """
        Cleans the output of _scrape
        """
        scraped_content = self._scrape()
        return float(scraped_content['temp'].replace('\xa0°C', '').strip())

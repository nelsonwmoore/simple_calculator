"""Get meteorites data from NASA API and calculate stats."""

import json
from urllib.request import urlopen

from simple_calculator.main import SimpleCalculator

URL = "https://data.nasa.gov/resource/y77d-th95.json"


class MeteoriteStats:
    """Meteorite statistics class."""

    def get_data(self):
        """Get meteorites data from NASA API."""
        if not URL.startswith(("http://", "https://")):
            raise ValueError(urlopen)

        with urlopen(URL) as url:  # noqa: S310
            print(type(json.loads(url.read().decode())))
            return json.loads(url.read().decode())

    def average_mass(self, data):
        """Calculate the average mass of meteorites."""
        calculator = SimpleCalculator()
        masses = [float(d["mass"]) for d in data if "mass" in d]
        return calculator.avg(masses)

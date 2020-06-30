#!/bin/python

import json
from dataclasses import dataclass

arrowdict = {0:   '➡',
             45:  '↗',
             90:  '⬆',
             135: '↖',
             180: '⬅',
             225: '↙',
             270: '⬇',
             315: '↘',
             360: '➡' }


@dataclass
class WeatherData:
    station: str
    text: str
    temp: float
    dewpoint: float
    wind_dir: int
    wind_speed: float
    bar_pressure: int
    visibility: int
    precip_hour: float
    humidity: float
    heat_index: float

    def pretty(self):
        print(f"""Weather at {self.station}:
{self.text}
✋{round(self.heat_index, 1)}°C | 🌡 {round(self.temp, 1)}°C
{self.arrow(self.wind_dir)} {self.wind_speed} km/h""")

    @staticmethod
    def extract_station(url):
        idx = url.rfind('/')
        return url[idx+1:]

    @staticmethod
    def arrow(angle):
        for key in arrowdict:
            if angle < key + 22.5 and angle >= key - 22.5:
                return arrowdict[key]

        raise ValueError("invalid value fed to WeatherData.arrow: {}", angle)


with open("forecast2.json") as f:
    weather = json.load(f)
    weather_data = WeatherData(
        WeatherData.extract_station(
            weather['properties']['station']
        ),
        weather['properties']['textDescription'],
        weather['properties']['temperature']['value'],
        weather['properties']['dewpoint']['value'],
        weather['properties']['windDirection']['value'],
        weather['properties']['windSpeed']['value'],
        weather['properties']['barometricPressure']['value'],
        weather['properties']['visibility']['value'],
        weather['properties']['precipitationLastHour']['value'],
        weather['properties']['relativeHumidity']['value'],
        weather['properties']['heatIndex']['value'],
    )

    weather_data.pretty()

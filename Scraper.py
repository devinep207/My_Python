import pandas as pd
import requests 
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=42.981355000000065&lon=-71.44170499999996')  #imports the url we need
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
week = soup.find(id="seven-day-forecast-body")  #specifies the tag our info is in
#print(week)P

items = week.find_all(class_='tombstone-container')
#print(items)

#print(items[0].find(class_='period-name').get_text())
#print(items[0].find(class_='short-desc').get_text())
#print(items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]    #loops through and collects period names
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]
#print(period_names)
#print(short_descriptions)
#print(temperatures)

weather_stuff = pd.DataFrame(
    {'period': period_names,
     'short_descriptions':short_descriptions,
     'temperatures':temperatures
    })

print(weather_stuff)

weather_stuff.to_csv('C:\MyPy\weather.csv')

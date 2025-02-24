import requests
from selenium import webdriver
import folium
import datetime
import time

def locationCoordinates():
    try:
        response = requests.get('https://ipinfo.io') #gets json from ipinfo
        data = response.json()
        loc = data['loc'].split(',')
        lat, long = float(loc[0]), float(loc[1])
        city = data.get('city', 'Unknown')
        state = data.get('region', 'Unknown')
        return lat, long, city, state
    except:
        print("Internet Not available")
        exit()
        return False

def gps_locator():
    obj = folium.Map(location=[0,0], zoom_start=2)
    try:
        lat,long,city,state = locationCoordinates()
        print(f'You Are in {city}, {state}')
        print(f'Your Latitude is {lat} and Longitude is {long}')
        folium.Marker(location=[lat,long], popup='Current Location').add_to(obj)

        filename = "C:/Users/xab/Location" + str(datetime.date.today()) + ".html"
        obj.save(filename)
        return filename
    except:
        print("Internet Not available")
        exit()
        return False

if __name__ == "__main__":
    print('-----------gps using python-----------')

    page = gps_locator()
    print('\nopening file.......')
    dr = webdriver.Edge()
    dr.get(page)
    time.sleep(30)
    quit()
    print('browser closed....')
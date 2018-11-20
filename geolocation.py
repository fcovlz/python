"""
@ Description
    This function returns the geo location from the city you select

@ Pass/Fail @b criteria
    None

@ Usage
    From terminal:
        geolocation.py

Certification Project
Q2: Create a script called location that return the location parameters of any location you want.
"""

from geocoder

def geolocation():
    while True:
        place = raw_input ("Write a city you want to locate, otherwise, write N")
        if place != "N":
            g = geocoder.google(place)
            print(g.latlng)
        else:
            break

if __name__ == "__main__":
    geolocation()
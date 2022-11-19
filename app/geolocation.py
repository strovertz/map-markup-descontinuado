import random
from geopy.geocoders import Nominatim
import csv

def get_lat(lat):
    dec_lat = random.random()/100
    return lat+dec_lat

def get_lon(lon):
    dec_lon = random.random()/100
    return lon+dec_lon
        
def generate_random_data(late, longe):
    print('%.6f %.6f \n' % (late, longe))
    address = get_address((late), (longe))
    if address == None:
        late = get_lat(random.uniform(0.00, 90.00))
        longe = get_lon(random.uniform(0.00, 180.00))
        generate_random_data(late, longe)
    lat_lon = [late, longe]
    #print('%.6f' % lat_lon[1])
    return lat_lon
    
def get_address(lati, longi):
    geolocator = Nominatim(user_agent="my_request")
    location = geolocator.reverse((lati, longi))
    print(location)
    return location

def read_data():    
    file = open ('data/User_data.csv')
    type(file)
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    header
    rows = []
    for row in csvreader:
        rows.append(row)
    rows
    file.close()
    return rows
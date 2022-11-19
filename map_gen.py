from geolocation import *
import folium

def set_markup(mapa, user_data):
    j = 1
    for i in user_data:
        popupe = "user" + str(j) + "\n" + "AudioDump: " + str(i[3]) + "\nWebcamDump: " + str(i[4])
        folium.Marker([i[1], i[2]], popup = popupe).add_to(mapa)
        j = j + 1
    return mapa
    
def map_html():
    
    lat_lon = generate_random_data(random.uniform(-20.11, 57.12), random.uniform(-20.11, 57.12))
    user_data = read_data()
    mapa = folium.Map(location=[lat_lon[0], lat_lon[1]], zoom_start=1)
    mapa = set_markup(mapa, user_data)
    mapa.save("my_map1.html" )
    
map_html()
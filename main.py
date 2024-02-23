import folium

# Utwórz obiekt mapy
mymap = folium.Map(location=[ 50.0374, 22.0049], zoom_start=60)

# Funkcja callback, która wyświetla współrzędne po najechaniu kursorem
def on_move(event):
    lat, lon = event['lat'], event['lng']
    print(f'Współrzędne kursora: {lat}, {lon}')

# Dodaj zdarzenie 'on_move' do mapy
mymap.add_child(folium.LatLngPopup())

# Przypisz funkcję callback do zdarzenia 'mousemove'
mymap.add_child(folium.ClickForMarker(popup=None))
mymap.add_child(folium.LatLngPopup())

# Zapisz mapę do pliku HTML
mymap.save('mapa.html')

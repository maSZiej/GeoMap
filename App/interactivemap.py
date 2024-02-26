from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource
from bokeh.models.tiles import WMTSTileSource

import random

# Utworzenie źródła danych dla punktów
source = ColumnDataSource(data=dict(lat=[], lon=[]))

# Utworzenie mapy z użyciem źródła danych
map_center = [51.5, -0.1]  # Środek mapy (dla przykładu: Londyn)
url = 'https://a.tile.openstreetmap.org/{Z}/{X}/{Y}.png'
tile_source = WMTSTileSource(url=url)
p = figure(x_range=(map_center[1]-0.1, map_center[1]+0.1), y_range=(map_center[0]-0.1, map_center[0]+0.1),
           x_axis_type="mercator", y_axis_type="mercator")
p.add_tile(tile_source)
p.circle(x="lon", y="lat", size=10, fill_color="blue", fill_alpha=0.8, source=source)

# Funkcja dodająca losowy punkt do mapy
def add_random_point():
    new_data = dict(lat=[random.uniform(51.3, 51.7)], lon=[random.uniform(-0.3, 0.1)])
    source.stream(new_data, rollover=10)

# Dodanie przycisku do wywoływania funkcji dodającej punkt
from bokeh.models import Button
button = Button(label="Dodaj punkt")
button.on_click(add_random_point)

# Dodanie elementów do layoutu
curdoc().add_root(p)
curdoc().add_root(button)

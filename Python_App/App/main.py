from fastapi import FastAPI
import random

app = FastAPI()

points = [
    (50.1210, 21.9232),
    (49.9752, 21.8511),
    (50.1122, 22.2713),
    (49.9500, 22.2652)
]


# Funkcja sprawdzająca, czy punkt znajduje się wewnątrz figury
def is_inside_polygon(x, y, polygon):
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside


# Generowanie losowego punktu wewnątrz figury
def generate_random_point_inside_polygon(polygon):
    min_x = min(point[0] for point in polygon)
    max_x = max(point[0] for point in polygon)
    min_y = min(point[1] for point in polygon)
    max_y = max(point[1] for point in polygon)

    while True:
        random_x = random.uniform(min_x, max_x)
        random_y = random.uniform(min_y, max_y)

        if is_inside_polygon(random_x, random_y, polygon):
            return random_x, random_y


# Wygenerowanie losowego punktu wewnątrz figury
random_point_inside_polygon = generate_random_point_inside_polygon(points)
print("Losowy punkt wewnątrz figury:")
print("Latitude:", random_point_inside_polygon[0])
print("Longitude:", random_point_inside_polygon[1])



@app.get("/points")
def get_points():
    random_point_inside_polygon = generate_random_point_inside_polygon(points)
    return  random_point_inside_polygon


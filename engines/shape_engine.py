import json, os
SHAPES_DIR = os.path.join(os.getcwd(), 'data', 'shapes')
os.makedirs(SHAPES_DIR, exist_ok=True)
def save_geojson(name, geojson):
    path = os.path.join(SHAPES_DIR, f"{name}.geojson")
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(geojson, f)
    return path

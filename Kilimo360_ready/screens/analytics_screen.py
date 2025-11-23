from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from engines.analytics_engine import shoelace_area, perimeter
import os, json, math

KV='''
<AnalyticsScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Analytics'
            left_action_items: [['arrow-left', lambda x: app.root.current = 'home']]
            elevation: 10
        BoxLayout:
            orientation: 'vertical'
            padding: dp(10)
            MDLabel:
                id: info
                text: 'Load a saved shape from data/shapes and compute area/perimeter (approx).'
                halign: 'left'
        BoxLayout:
            size_hint_y: None
            height: dp(56)
            MDRectangleFlatButton:
                text: 'Compute Most Recent Shape'
                on_release: root.compute_recent()
'''

class AnalyticsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Builder.load_string(KV)

    def compute_recent(self):
        shapes_dir = os.path.join(os.getcwd(), 'data', 'shapes')
        files = [f for f in os.listdir(shapes_dir) if f.endswith('.geojson')]
        if not files:
            return
        files.sort(key=lambda x: os.path.getmtime(os.path.join(shapes_dir, x)))
        path = os.path.join(shapes_dir, files[-1])
        with open(path, 'r', encoding='utf-8') as f:
            gj = json.load(f)
        coords = gj.get('geometry', {}).get('coordinates', [[]])[0]
        # convert lon/lat to meters via equirectangular approx around centroid
        lons = [c[0] for c in coords]
        lats = [c[1] for c in coords]
        mean_lat = sum(lats)/len(lats)
        meters = []
        for lon, lat in zip(lons, lats):
            x = (lon - lons[0]) * 111320 * math.cos(math.radians(mean_lat))
            y = (lat - lats[0]) * 110540
            meters.append((x,y))
        area = shoelace_area(meters)
        per = perimeter(meters)
        self.ids.info.text = f'Area ≈ {area:.2f} m²\nPerimeter ≈ {per:.2f} m'

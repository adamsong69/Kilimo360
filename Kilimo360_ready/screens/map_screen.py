from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy_garden.mapview import MapView, MapMarker
from kivy.graphics import Color, Line, Ellipse
from kivy.uix.widget import Widget
from engines.shape_engine import save_geojson
import json, math, os

KV = '''
<MapScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Map / Shapes'
            left_action_items: [['arrow-left', lambda x: app.root.current = 'home']]
            elevation: 10
        MapView:
            id: mapview
            lat: -6.8
            lon: 39.2
            zoom: 12
        BoxLayout:
            size_hint_y: None
            height: dp(56)
            MDRectangleFlatButton:
                text: 'Start Draw'
                on_release: root.start_draw()
            MDRectangleFlatButton:
                text: 'Save Shape'
                on_release: root.save_shape()
'''

class DrawWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.points = []  # store lat,lon tuples for logic
        self.line = None

    def on_touch_down(self, touch):
        # ignore touches outside map area handled by parent
        if not self.collide_point(*touch.pos):
            return False
        # add a small circle and start line
        with self.canvas:
            Color(1,0,0)
            d = 6.
            Ellipse(pos=(touch.x-d/2, touch.y-d/2), size=(d,d))
            if not self.line:
                self.line = Line(points=[touch.x, touch.y], width=2)
            else:
                self.line.points += [touch.x, touch.y]
        self.points.append((touch.x, touch.y))
        return True

    def on_touch_move(self, touch):
        if self.line and self.collide_point(*touch.pos):
            self.line.points += [touch.x, touch.y]
            self.points.append((touch.x, touch.y))
            return True
        return False

class MapScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Builder.load_string(KV)
        self.drawing = False
        self.draw_widget = None

    def on_enter(self):
        pass

    def start_draw(self):
        if not self.drawing:
            # create overlay widget for drawing on top of map
            self.draw_widget = DrawWidget(size=self.ids.mapview.size, pos=self.ids.mapview.pos)
            self.ids.mapview.add_widget(self.draw_widget)
            self.drawing = True

    def save_shape(self):
        if not self.draw_widget:
            return
        # naive conversion: map screen XY -> lat/lon via MapView.get_latlon_at
        mv = self.ids.mapview
        pts = []
        for x,y in self.draw_widget.points:
            lat, lon = mv.get_latlon_at(x, y)
            pts.append([lon, lat])  # GeoJSON expects [lon, lat]
        geo = {
            "type":"Feature",
            "properties":{"name":"shape_"+str(int(os.times()[4]))},
            "geometry":{"type":"Polygon","coordinates":[pts]}
        }
        path = save_geojson('shape_'+str(int(os.times()[4])), geo)
        from kivymd.toast import toast
        toast(f'Saved: {path}')
        # remove drawing overlay
        try:
            mv.remove_widget(self.draw_widget)
        except Exception:
            pass
        self.draw_widget = None
        self.drawing = False

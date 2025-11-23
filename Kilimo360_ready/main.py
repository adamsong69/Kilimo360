from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

from screens.home_screen import HomeScreen
from screens.forms_screen import FormsScreen
from screens.map_screen import MapScreen
from screens.analytics_screen import AnalyticsScreen

Window.size = (360, 640)  # desktop testing size

KV = '''
ScreenManager:
    HomeScreen:
        name: 'home'
    FormsScreen:
        name: 'forms'
    MapScreen:
        name: 'map'
    AnalyticsScreen:
        name: 'analytics'
'''

class KilimoApp(MDApp):
    def build(self):
        self.title = 'Kilimo360'
        return Builder.load_string(KV)

if __name__ == '__main__':
    KilimoApp().run()

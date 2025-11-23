from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.boxlayout import MDBoxLayout

KV = '''
<HomeScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Kilimo360 - Home'
            elevation: 10
        MDBoxLayout:
            padding: dp(10)
            orientation: 'vertical'
            spacing: dp(10)
            MDRectangleFlatButton:
                text: 'Start Data Collection (Forms)'
                pos_hint: {'center_x': .5}
                on_release: app.root.current = 'forms'
            MDRectangleFlatButton:
                text: 'Open Map / Shapes'
                pos_hint: {'center_x': .5}
                on_release: app.root.current = 'map'
            MDRectangleFlatButton:
                text: 'Analytics'
                pos_hint: {'center_x': .5}
                on_release: app.root.current = 'analytics'
'''

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Builder.load_string(KV)

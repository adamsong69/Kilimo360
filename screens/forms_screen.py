from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
import os, json
from engines.form_engine import init_db, save_submission

KV = '''
<FormsScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Forms'
            left_action_items: [['arrow-left', lambda x: app.root.current = 'home']]
            elevation: 10
        ScrollView:
            BoxLayout:
                id: form_container
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                padding: dp(10)
                spacing: dp(10)
        BoxLayout:
            size_hint_y: None
            height: dp(56)
            padding: dp(10)
            MDRaisedButton:
                text: 'Load Sample Form'
                on_release: root.load_sample_form()
            MDRaisedButton:
                text: 'Save Submission'
                on_release: root.save_form()
'''

class FormsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Builder.load_string(KV)
        init_db()
        self.form_fields = []

    def load_sample_form(self):
        forms_dir = os.path.join(os.getcwd(), 'data', 'forms')
        path = os.path.join(forms_dir, 'sample_form.json')
        if not os.path.exists(path):
            return
        with open(path, 'r', encoding='utf-8') as f:
            form = json.load(f)
        container = self.ids.get('form_container')
        container.clear_widgets()
        self.form_fields = []
        for q in form.get('questions', []):
            lbl = MDTextField(hint_text=q.get('label', q.get('name')))
            lbl.field_name = q.get('name')
            container.add_widget(lbl)
            self.form_fields.append(lbl)
        # add a spacer
        container.height = container.minimum_height + 20

    def save_form(self):
        data = {}
        for fld in self.form_fields:
            data[getattr(fld, 'field_name', 'field')] = fld.text
        save_submission('sample_form', data)
        from kivymd.toast import toast
        toast('Saved locally to submissions.db')

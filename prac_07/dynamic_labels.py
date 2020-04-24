
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ['jai', 'jordan', 'paul', 'paula']

    def build(self):
        self.title = 'Dynamic lists'
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

    def create_labels(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.labels_box.add_widget(temp_label)


DynamicLabelsApp().run()

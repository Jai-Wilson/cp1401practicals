
from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

MILES_TO_KM = 1.60934

class ConvertMilesToKm(App):

    Distance = StringProperty()

    def build(self):

        self.title = 'Convert Miles to Kilometers'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        distance_in_km = self.get_valid_miles()
        distance_in_miles = distance_in_km * MILES_TO_KM
        self.root.ids.output_distance.text = str(distance_in_miles)

    def handle_change(self, change):
        distance_in_km = self.get_valid_miles() + change
        self.root.ids.input_distance.text = str(distance_in_km)
        self.handle_convert()


    def get_valid_miles(self):
        try:
            user_input = float(self.root.ids.input_distance.text)
            return user_input
        except ValueError:
            return 0





ConvertMilesToKm().run()
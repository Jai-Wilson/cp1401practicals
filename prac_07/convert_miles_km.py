
from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

MILES_TO_KM = 1.60934

class ConvertMilesToKm(App):

    Distance = StringProperty()

    def build(self):
        '''Build the kivy app from the kv file'''

        self.title = 'Convert Miles to Kilometers'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        '''Convert user entered miles to kilometers'''
        distance_in_km = self.get_valid_miles()
        distance_in_miles = distance_in_km * MILES_TO_KM
        self.root.ids.output_distance.text = str(distance_in_miles)

    def handle_change(self, change):
        '''Convert user miles to kilomeers when the up/down button is pressed, increasing and
        decreasing the user input by 1'''
        distance_in_km = self.get_valid_miles() + change
        self.root.ids.input_distance.text = str(distance_in_km)
        self.handle_convert()


    def get_valid_miles(self):
        '''check user input to be valid float variable. If not, use 0'''
        try:
            user_input = float(self.root.ids.input_distance.text)
            return user_input
        except ValueError:
            return 0





ConvertMilesToKm().run()
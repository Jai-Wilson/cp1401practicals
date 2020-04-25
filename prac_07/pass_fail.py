from kivy.app import App
from kivy.lang import Builder

class StudentScoreCalculator(App):

    def build(self):
        self.title = 'Student score calculator'
        self.root = Builder.load_file('pass_fail.kv')

    def handle_calculate(self):

        score = int(self.root.ids.score_input.text)
        if score >= 0 and score < 50:
            result = 'fail'
            self.root.ids.score_output.text = result
        elif score >=50 and score < 65:
            result = 'pass'
            self.root.ids.score_output.text = result
        elif score >= 65 and score < 75:
            result = 'credit'
            self.root.ids.score_output.text = result
        elif score >= 75 and score < 85:
            result = 'distinction'
            self.root.ids.score_output.text = result
        elif score >=85 and score <100:
            result = 'high distinction'
            self.root.ids.score_output.text = result
        elif score >=100:
            result = 'cheating'
            self.root.ids.score_output.text = result
    def handle_clear(self):
        self.root.ids.score_input.text = ''
        self.root.ids.score_output.text = 'Enter score above to calculate grade'

StudentScoreCalculator().run()
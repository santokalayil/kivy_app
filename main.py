# python -m pip install kivy[base] --user
# python -m pip install pygame --user
# set PATH=%PATH%;'C:\Users\Santo Kalayil\AppData\Roaming\Python\Python39\Scripts\'

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# Window.size = (500, 700)  # set window size


Builder.load_file(filename='calc.kv')


class MyLayout(Widget):
    number_array = []
    operation_order = []
    def clear(self):
        self.ids.calc_input.text = '0'

    def button_press(self, button):
        # remove 0 if first time
        prior = self.ids.calc_input.text
        if prior == '0':
            self.ids.calc_input.text = ''
        self.ids.calc_input.text += str(button)

    def operation_press(self, button):
        prior = self.ids.calc_input.text
        if prior == '0':
            return
        else:
            self.number_array.append(int(button))
            if button == '+':
                self.operation_order.append('+')




class CalculatorApp(App):
    def build(self):
        return MyLayout()


def start_app():
    CalculatorApp().run()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_app()


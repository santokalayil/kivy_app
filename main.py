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
    pass


class CalculatorApp(App):
    def build(self):
        return MyLayout()


def start_app():
    CalculatorApp().run()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_app()


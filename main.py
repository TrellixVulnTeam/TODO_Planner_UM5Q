import kivy
from kivy.app import App
from kivy.uix.label import Label

class TDOOApp(App):
    def build(self):
        return Label(text="asdf")


if __name__ == "__main__":
    TDOOApp().run()

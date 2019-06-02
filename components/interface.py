from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class PathFinder(BoxLayout):
    pass

class ShowQueues(BoxLayout):
    pass

class Configurations(BoxLayout):
    pass

class Interface(App):
    def build(self):
        return PathFinder()


Interface().run()


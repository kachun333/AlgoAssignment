from kivy.app import App

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

from kivy.garden.mapview import MapView, MapMarker


class MainScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.add_widget(Label(text='User Name'))
        mapview = MapView(zoom=11, lat=2.7456, lon=101.7072, size_hint=(1.6, 1))
        mapview.add_widget(MapMarker(lat=2.7456, lon=101.7072))
        self.add_widget(mapview)


class MyApp(App):

    def build(self):
        return MainScreen()


if __name__ == '__main__':
    MyApp().run()

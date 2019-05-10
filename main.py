import random
from math import *

from kivy.core.window import Window 
Window. size = (1920, 1080)

from kivy.properties import NumericProperty, ObjectProperty, ListProperty, AliasProperty, BooleanProperty, StringProperty
from kivy.app import App
from kivy.clock import Clock

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


from kivy.graphics import Color, Line
from kivy.graphics.transformation import Matrix
from kivy.graphics.context_instructions import Translate, Scale

from kivy.garden.mapview import MapView, MapMarker, MapLayer#, MIN_LONGITUDE, MIN_LATITUDE, MAX_LATITUDE, MAX_LONGITUDE
from mapview.utils import clamp

from kivy.garden.cefpython import CEFBrowser

from lineMap import LineMapLayer


class MapViewApp(App):
    mapview = None
 
    def __init__(self, **kwargs):
        super(MapViewApp, self).__init__(**kwargs)
        Clock.schedule_once(self.post, 0)
 
    def build(self):
        layout = BoxLayout(orientation='vertical')
        return layout
 
    def post(self, *args):
        layout = FloatLayout()
        self.mapview = MapView(zoom=9, lat=2.7456, lon=101.7072)
        #for l in locations:
        #    self.mapview.add_widget(MapMarker(lat=l['lat'], lon=l['lon']))
        line = LineMapLayer()
        self.mapview.add_layer(line, mode="scatter")  # window scatter
        layout.add_widget(self.mapview)
        
        self.root.add_widget(layout)
        b = BoxLayout(orientation='horizontal',height='32dp',size_hint_y=None)
        b.add_widget(Button(text="Zoom in",on_press=lambda a: setattr(self.mapview,'zoom',clamp(self.mapview.zoom+1, 0, 10))))
        b.add_widget(Button(text="Zoom out",on_press=lambda a: setattr(self.mapview,'zoom',clamp(self.mapview.zoom-1, 0, 10))))
        b.add_widget(Button(text="AddPoint",on_press=lambda a: line.add_point()))
        self.root.add_widget(b)


locations = {}
locations['Kuala Lumpur'] = {'lat':2.7456, 'lon':101.7072}
locations['Brasilia'] = {'lat':-15.8697, 'lon':-47.9172}
locations['Tokyo'] = {'lat':35.5494, 'lon':139.7798}
locations['London'] = {'lat':51.5048, 'lon':0.0495}
locations['New York'] = {'lat':40.6413, 'lon':-73.7781}
locations['Bangkok'] = {'lat':13.6900, 'lon':100.7501}
locations['Kabul'] = {'lat':34.5609, 'lon':69.2101}
locations['California'] = {'lat':33.6762, 'lon':-117.8675} # testing purpose
destinations = ['Kuala Lumpur', 'Brasilia', 'Tokyo', 'London', 'New York', 'Bangkok', 'Kabul', 'California']


class MainScreen(BoxLayout):

    def choose_destination(self, instance):
        self.destination = instance.text
        self.line.coordinates=[[2.7456, 101.7072], [locations[instance.text]['lat'], locations[instance.text]['lon']]]
        self.left_label.text = 'From Kuala Lumpur\nTo {}'.format(self.destination)

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.destination = 'Kuala Lumpur'
        
        left_layout = BoxLayout(orientation = 'vertical')
        self.left_label = Label(text='From Kuala Lumpur\nTo {}'.format(self.destination))
        left_layout.add_widget(self.left_label)
        for d in destinations:
            btn = Button(text=d)
            #btn.bind(state=self.choose_destination)
            btn.bind(on_press=self.choose_destination)
            left_layout.add_widget(btn)
        #b = BoxLayout(orientation='horizontal',height='32dp',size_hint_y=None)
        #b.add_widget(Button(text="Zoom in",on_press=lambda a: setattr(self.mapview,'zoom',clamp(self.mapview.zoom+1, 3, 10))))
        #b.add_widget(Button(text="Zoom out",on_press=lambda a: setattr(self.mapview,'zoom',clamp(self.mapview.zoom-1, 3, 10))))
        #left_layout.add_widget(b)
        self.add_widget(left_layout)
        
        self.mapview = MapView(zoom=8, lat=2.7456, lon=101.7072, size_hint=(1.8, 1))
        #self.mapview.add_widget(MapMarker(lat=2.7456, lon=101.7072))
        self.addMaker()
        # "./map.html?path=Kuala+Lumpur,Tokyo,New+York&id=1234"
        self.webview = CEFBrowser(url="file:///home/thechee/Documents/Acedemic/S2_19/WIA2005/AlgoAssignment/map.html?path=Kuala+Lumpur,Tokyo,New+York&id=1234", size_hint=(1.8, 1))
        self.add_widget(self.webview)
        self.line.reposition()
        self.line.coordinates=[[2.7456, 101.7072], [2.7456, 101.7072]]
    
    def addMaker(self):
        for l in locations.keys():
            self.mapview.add_widget(MapMarker(lat=locations[l]['lat'], lon=locations[l]['lon']))
        self.line = LineMapLayer()
        self.mapview.add_layer(self.line, mode="scatter")


class MyApp(App):

    def build(self):
        return MainScreen()


if __name__ == '__main__':
    MyApp().run()
    #MapViewApp().run()

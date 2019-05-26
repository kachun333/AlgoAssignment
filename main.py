import random
from math import *

#from kivy.core.window import Window 
#Window.size = (1280, 720)

from kivy.config import Config
#Config.set('kivy', 'log_level', 'debug')
#Config.set('graphics', 'fullscreen', 'auto')
Config.set('graphics', 'width', '2560')
Config.set('graphics', 'height', '1440')

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

#from kivy.garden.mapview import MapView, MapMarker, MapLayer#, MIN_LONGITUDE, MIN_LATITUDE, MAX_LATITUDE, MAX_LONGITUDE
#from mapview.utils import clamp

from kivy.garden.cefpython import CEFBrowser
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas, NavigationToolbar2Kivy

#from lineMap import LineMapLayer
from distance import *
from distance import MapGraph
from wordFrequency import CitySentiment, city
from probability import probability

# class MapViewApp(App):
#     mapview = None
 
#     def __init__(self, **kwargs):
#         super(MapViewApp, self).__init__(**kwargs)
#         Clock.schedule_once(self.post, 0)
 
#     def build(self):
#         layout = BoxLayout(orientation='vertical')
#         return layout
 
#     def post(self, *args):
#         layout = FloatLayout()
#         self.mapview = MapView(zoom=9, lat=2.7456, lon=101.7072)
#         #for l in locations:
#         #    self.mapview.add_widget(MapMarker(lat=l['lat'], lon=l['lon']))
#         line = LineMapLayer()
#         self.mapview.add_layer(line, mode="scatter")  # window scatter
#         layout.add_widget(self.mapview)
        
#         self.root.add_widget(layout)
#         b = BoxLayout(orientation='horizontal',height='32dp',size_hint_y=None)
#         b.add_widget(Button(text="Zoom in",on_press=lambda a: setattr(self.mapview,'zoom',clamp(self.mapview.zoom+1, 0, 10))))
#         b.add_widget(Button(text="Zoom out",on_press=lambda a: setattr(self.mapview,'zoom',clamp(self.mapview.zoom-1, 0, 10))))
#         b.add_widget(Button(text="AddPoint",on_press=lambda a: line.add_point()))
#         self.root.add_widget(b)


locations = {}
locations['Kuala Lumpur'] = {'lat':2.7456, 'lon':101.7072}
locations['Brasilia'] = {'lat':-15.8697, 'lon':-47.9172}
locations['Tokyo'] = {'lat':35.5494, 'lon':139.7798}
locations['London'] = {'lat':51.5048, 'lon':0.0495}
locations['New York'] = {'lat':40.6413, 'lon':-73.7781}
locations['Bangkok'] = {'lat':13.6900, 'lon':100.7501}
locations['Kabul'] = {'lat':34.5609, 'lon':69.2101}
#locations['California'] = {'lat':33.6762, 'lon':-117.8675} # testing purpose
destinations = ['Kuala Lumpur', 'Brasilia', 'Tokyo', 'London', 'New York', 'Bangkok', 'Kabul']

#initialize graph
graph = MapGraph()
# for i in range(len(destinations)):
#     for j in range(i+1, len(destinations)):
#         distance = calculate(locations[destinations[i]]['lat'], locations[destinations[i]]['lon'], locations[destinations[j]]['lat'], locations[destinations[j]]['lon'])
#         graph.add_edge(destinations[i], destinations[j], cost=distance)


class MainScreen(BoxLayout):

    def choose_destination(self, instance):
        self.destination = instance.text
        
        # graph.remove_edge('Kuala Lumpur', instance.text)
        # p = graph.dijkstra('Kuala Lumpur', instance.text)
        # graph.add_edge('Kuala Lumpur', instance.text, cost=calculate(locations['Kuala Lumpur']['lat'], locations['Kuala Lumpur']['lon'], locations[instance.text]['lat'], locations[instance.text]['lon']))
        paths = graph.getPaths(instance.text)
        cities = {}
        for path in paths:
            l = list(path.path)
            for i in range(1, len(l)-1):
                cities[l[i]] = True
        print(str(len(paths)) + ' paths prepared')
        p = paths[0].path

        self.path = ""
        while len(p) > 0:
            self.path += str(p.popleft())+','
        print(self.path)
        self.path = self.path[0:-1]
        self.path = self.path.replace(' ', '+')
        print(self.path)
        #self.line.coordinates=[[2.7456, 101.7072], [locations[instance.text]['lat'], locations[instance.text]['lon']]]
        self.left_label.text = 'From Kuala Lumpur\nTo {}'.format(self.destination)
        self.webview.url = "https://waixiong.github.io/AlgoAssisgnmentMap/map.html?path="+self.path+"&id=1234"
        #self.webview.reload()
        self.right_layout.remove_widget(self.probabilityGraph)
        self.right_layout.remove_widget(self.wordGraph)

        self.probabilityGraph = probability(paths).canvas
        self.wordGraph = BoxLayout()
        for c in cities:
            f1, f2 = city[c].graph()
            b = BoxLayout(orientation = 'vertical')
            b.add_widget(f1.canvas)
            b.add_widget(f2.canvas)
            self.wordGraph.add_widget(b)

        self.right_layout.add_widget(self.probabilityGraph)
        self.right_layout.add_widget(self.wordGraph)

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.destination = 'London'
        paths = graph.getPaths('London')
        self.path = "Kuala+Lumpur,Kabul,London"
        
        left_layout = BoxLayout(orientation = 'vertical')
        self.left_label = Label(text='From Kuala Lumpur\nTo {}'.format(self.destination))
        left_layout.add_widget(self.left_label)
        for d in destinations:
            btn = Button(text=d)
            #btn.bind(state=self.choose_destination)
            btn.bind(on_press=self.choose_destination)
            left_layout.add_widget(btn)
        self.add_widget(left_layout)
        
        # "./map.html?path=Kuala+Lumpur,Tokyo,New+York&id=1234"
        self.webview = CEFBrowser(url="https://waixiong.github.io/AlgoAssisgnmentMap/map.html?path="+self.path+"&id=1234", size_hint=(3, 1))
        self.add_widget(self.webview)
        
        self.right_layout = BoxLayout(orientation = 'vertical', size_hint=(2, 1))
        self.probabilityGraph = probability(paths).canvas
        self.right_layout.add_widget(self.probabilityGraph)
        self.wordGraph = BoxLayout()
        self.right_layout.add_widget(self.wordGraph)

        f1, f2 = city['London'].graph()
        b = BoxLayout(orientation = 'vertical')
        b.add_widget(f1.canvas)
        b.add_widget(f2.canvas)
        self.wordGraph.add_widget(b)

        self.add_widget(self.right_layout)


class MyApp(App):

    def build(self):
        return MainScreen()


if __name__ == '__main__':
    MyApp().run()
    #MapViewApp().run()

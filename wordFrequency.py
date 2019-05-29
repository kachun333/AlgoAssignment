import os
from article import article
import json

from distance import MapGraph

import matplotlib
#matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

import multiprocessing.dummy as mp 


# Brasilia  0.26865990756894953
# New York  0.24862244449322582
# London    0.2585793889667123
# Bangkok   0
# Kabul     0
# Tokyo     0

class CitySentiment:

    # cityName is Bangkok, New York, London, Kabul, Tokyo, Brasilia
    def __init__(self, cityName):
        self.city = cityName
        self.path = os.path.dirname(os.path.abspath(__file__))+"/Webpage_txt/"+cityName
        self.files = os.listdir(self.path)
        self.articles = []
        self.data = None
        try:
            with open(cityName+'.json') as json_file:  
                self.data = json.load(json_file)
        except:
            pass
    
    def MPsentiment(self, i):
        filename = self.path+"/"+self.files[i]
        print(filename)
        a = article(filename, self.city, self.files[i])
        self.articles.append(a)
        if a.data == None:
            a.calculateWords()

    def sentiment(self):
        
        if len(self.articles) == 0:
            # if didn't scan articles yet then scan else skip this 
            i = 0
            # for x in self.files:
            #     p = mp.Pool(5)
            #     p.map(self.MPsentiment,range(0,5)) # range(0,1000) if you want to replicate your example
            #     p.close()
            #     p.join()
            #     #print("Article " + str(i) + ": " + str(self.articles[i].getNoStopTotal())+ " FROM " + str(self.articles[i].getOriTotal()))
            #     #print("article pos word is " + str(self.articles[i].getPosCount()))
            #     #print("article neg word is " + str(self.articles[i].getNegCount()))
            #     #print("polarity is " + str(self.articles[i].getPolarity()))
            #     i += 1
            p = mp.Pool(5)
            p.map(self.MPsentiment,range(0,5)) # range(0,1000) if you want to replicate your example
            p.close()
            p.join()
        
        sum = 0
        for j in self.articles:
            sum += j.getPolarity()
        return sum/5
    
    def graph(self):

        if len(self.articles) == 0:
            # if didn't scan articles yet then scan else skip this 
            p = mp.Pool(5)
            p.map(self.MPsentiment,range(0,5)) # range(0,1000) if you want to replicate your example
            p.close()
            p.join()

        N=5
        ori_word = (int(self.articles[0].getOriTotal()), int(self.articles[1].getOriTotal()),int(self.articles[2].getOriTotal()),int(self.articles[3].getOriTotal()),int(self.articles[4].getOriTotal()))
        stop_word = (int(self.articles[0].getNoStopTotal()), int(self.articles[1].getNoStopTotal()),int(self.articles[2].getNoStopTotal()), int(self.articles[3].getNoStopTotal()), int(self.articles[4].getNoStopTotal()))

        pos_word = (int(self.articles[0].getPosCount()),int(self.articles[1].getPosCount()),int(self.articles[2].getPosCount()),int(self.articles[3].getPosCount()),int(self.articles[4].getPosCount()))
        neg_word = (int(self.articles[0].getNegCount()),int(self.articles[1].getNegCount()),int(self.articles[2].getNegCount()),int(self.articles[3].getNegCount()),int(self.articles[4].getNegCount()))

        index = np.arange(N)
        width=0.35
        fig, ax = plt.subplots()
        ax.bar(index,ori_word,width,label="Original Word Count")
        ax.bar(index + width, stop_word,width,label="Stop Word Count")
        ax.set_ylabel("Word")
        ax.set_title(str(self.city) + " - Number of Word")
        ax.set_xticks(index + width / 2, ('Article 1', 'Article 2', 'Article 3', 'Article 4', 'Article 5'))
        ax.legend(loc='best')

        fig2, ax2 = plt.subplots()
        ax2.bar(index,pos_word,width,label="Positive Word Count")
        ax2.bar(index + width, neg_word,width,label="Negative Word Count")
        ax2.set_ylabel("Word")
        #plt.title("Number of Word")
        ax2.set_xticks(index + width / 2, ('Article 1', 'Article 2', 'Article 3', 'Article 4', 'Article 5'))
        ax2.legend(loc='best')
        return fig, fig2
    
    def graphStandalone(self):

        # if len(self.articles) == 0:
        #     # if didn't scan articles yet then scan else skip this 
        #     p = mp.Pool(5)
        #     p.map(self.MPsentiment,range(0,5)) # range(0,1000) if you want to replicate your example
        #     p.close()
        #     p.join()
        
        for i in range(0, 5):
            self.MPsentiment(i)

        N=5
        ori_word = (int(self.articles[0].getOriTotal()), int(self.articles[1].getOriTotal()),int(self.articles[2].getOriTotal()),int(self.articles[3].getOriTotal()),int(self.articles[4].getOriTotal()))
        stop_word = (int(self.articles[0].getNoStopTotal()), int(self.articles[1].getNoStopTotal()),int(self.articles[2].getNoStopTotal()), int(self.articles[3].getNoStopTotal()), int(self.articles[4].getNoStopTotal()))
        
        pos_word = (int(self.articles[0].getPosCount()),int(self.articles[1].getPosCount()),int(self.articles[2].getPosCount()),int(self.articles[3].getPosCount()),int(self.articles[4].getPosCount()))
        neg_word = (int(self.articles[0].getNegCount()),int(self.articles[1].getNegCount()),int(self.articles[2].getNegCount()),int(self.articles[3].getNegCount()),int(self.articles[4].getNegCount()))

        index = np.arange(N)
        width=0.35
        plt.subplot(2, 1, 1)
        plt.bar(index,ori_word,width,label="Original Word Count")
        plt.bar(index + width, stop_word,width,label="Stop Word Count")
        plt.ylabel("Word")
        plt.title(str(self.city) + " - Number of Word")
        plt.xticks(index + width / 2, ('Article 1', 'Article 2', 'Article 3', 'Article 4', 'Article 5'))
        plt.legend(loc='best')

        plt.subplot(2, 1, 2)
        plt.bar(index,pos_word,width,label="Positive Word Count")
        plt.bar(index + width, neg_word,width,label="Negative Word Count")
        plt.ylabel("Word")
        #plt.title("Number of Word")
        plt.xticks(index + width / 2, ('Article 1', 'Article 2', 'Article 3', 'Article 4', 'Article 5'))
        plt.legend(loc='best')
        
        plt.show()


city = {}
city['Brasilia'] = CitySentiment('Brasilia')
city['New York'] = CitySentiment('New York')
city['Bangkok'] = CitySentiment('Bangkok')
city['Kabul'] = CitySentiment('Kabul')
city['London'] = CitySentiment('London')
city['Tokyo'] = CitySentiment('Tokyo')


if __name__ == "__main__":
    #user input
    
    #print(city)
    # city_chosen = int(input("Choose a city by key in its number"))

    # for i in []:
        
    #     # call citySentiment object, pass in city name
    #     theCity = city.get(i) 

    #     # call .sentiment() to get the sentiment result of the city
    #     print(city.get(i) + ' is ' + str(theCity.sentiment()) + ' of sentiment')
    #     print(city.get(i) + ' is ' + str(theCity.sentiment()) + ' of sentiment')
    #     print(city.get(i) + ' is ' + str(theCity.sentiment()) + ' of sentiment\t')
    
    listOfCities = {1:"Brasilia", 2:"New York", 3:"London", 4:"Bangkok", 5:"Kabul", 6:"Tokyo"}
    print(listOfCities)
    city_chosen = int(input("Choose a city according to its number: "))

    city[listOfCities[city_chosen]].graphStandalone()

    # g  = MapGraph()
    # paths = g.getPaths(listOfCities[city_chosen])

    # for path in paths:
    #     print('For path ' + str(path.path))
    #     pathL = list(path.path)
    #     for l in range(1, len(pathL)-1):
    #         city[pathL[l]].graphStandalone()

    print(city[listOfCities[city_chosen]].sentiment())


# Brasilia  0.004814841674599791
# New York  0.01791518618874715
# London    0.02853958549118011
# Bangkok   0.005699998964845554
# Kabul     0.0057077767401467255
# Tokyo     0.022458310532577082

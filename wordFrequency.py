import os
from article import article
import json

from distance import MapGraph

import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
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
    
    g  = MapGraph()
    f1, f2 = city['London'].graph()
    
    import datetime
    t = datetime.datetime.now()
    print(type(city['London'].graph()))
    print(datetime.datetime.now() - t)
    paths = g.getPaths('Brasilia')

    totalDistanceP = 0 # ignore this line use ur totalPath
    totalPoli = 0

    # calculate for sentiment for every path in paths
    for path in paths:
        print(path.path)
        print(path.distance)
        pathSentiment = 0
        pathList = list(path.path)
        # for i in range(1, len(pathList)-1):
        #    pathSentiment += city.get(pathList[i]).sentiment()
        # pathSentiment /= len(pathList) - 2 
        # print('The sentiment of the path is ' + str(pathSentiment) + '\n')
        path.pathSentiment = pathSentiment

        totalDistanceP += 1 / (path.distance * (paths.index(path)+1)) 
        totalPoli += path.pathSentiment
    
    # calculate probability
    for path in paths:
        pathProb = (1/(path.distance * (paths.index(path)+1))) / totalDistanceP
        #sentimentProb = path.pathSentiment / totalPoli
        
        #prob = (pathProb + sentimentProb) / 2

        print('for path '+str(path.path))
        print(path.distance)
        print('the probability is ' + str(pathProb)+'\n')



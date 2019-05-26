import os
from article import article
from distance import MapGraph
import multiprocessing.dummy as mp 
t1 = 0
final = 0

from wordFrequency import CitySentiment, city
import matplotlib
#matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

def totalPath(paths):
    t1 = 0.0
    for path in paths:
        t1 += 1 / (path.distance * (paths.index(path)+1))
    return t1

def totalPoli(paths):
    t1 = 0.0
    for path in paths:
        t1 += path.pathSentiment
    return t1

def probability(paths):
    # Calculation
    for path in paths:
        # Political sentiment
        pathSentiment = 0
        pathList = list(path.path)

        for i in range(1, len(pathList)-1):
            pathSentiment += city.get(pathList[i]).sentiment()
        
        pathSentiment /= len(pathList) - 2 
        path.pathSentiment = pathSentiment

    for path in paths:
        print(path.path)

        # Shortest distance
        path.pathProb = 1 / (path.distance * (paths.index(path)+1)) / float(totalPath(paths))

        # Sentiment
        path.sentimentProb = path.pathSentiment / float(totalPoli(paths))
    
        # Shortest path + Political sentiment
        path.probability = (path.pathProb + path.sentimentProb) / 2
        print("Total probability of this route: " + str(path.probability) + "\n")
    
    probabilityList = (paths[0].probability, paths[1].probability, paths[2].probability, paths[3].probability, paths[4].probability)
    index = np.arange(5)
    width=0.35
    xLabel = []
    for path in paths:
        s = ''
        for l in list(path.path):
            s += l + '\n'
        xLabel.append(s)
    fig, ax = plt.subplots()
    b = ax.bar(index,probabilityList,width, label="Probability", tick_label=xLabel)
    ax.set_ylabel("Probability")
    ax.set_title("Probability of Paths")
    ax.set_xticks(index + width / 2, ['Path 1', 'Path 2', 'Path 3', 'Path 4', 'Path 5'])
    ax.legend(loc='best')

    return fig


if __name__ == "__main__":
    # User input
    listOfCities = {1:"Brasilia", 2:"New York", 3:"London", 4:"Bangkok", 5:"Kabul", 6:"Tokyo"}
    print(listOfCities)
    city_chosen = int(input("Choose a city according to its number: "))

    g = MapGraph()
    paths = g.getPaths(listOfCities[city_chosen])
    probability(paths)
    p = 0
    for path in paths:
        p += path.probability
    print('\n\n' + str(p))

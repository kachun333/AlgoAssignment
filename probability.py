import os
from article import article
from distance import MapGraph
import multiprocessing.dummy as mp 
t1 = 0
final = 0

def totalPath():
    t1 = (1/paths[0].distance) + (1/paths[1].distance) + (1/paths[2].distance) + (1/paths[3].distance) + (1/paths[4].distance)
    return t1

class CitySentiment:
    # cityName: Bangkok, New York, London, Kabul, Tokyo, Brasilia
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
            # If articles are not scanned yet then scan, else skip
            p = mp.Pool(5)
            p.map(self.MPsentiment,range(0,5))
            p.close()
            p.join()
        
        sum = 0
        for j in self.articles:
            sum += j.getPolarity()
        return sum/5


# To avoid repetitive creation of object
city = {}
city['Brasilia'] = CitySentiment('Brasilia')
city['New York'] = CitySentiment('New York')
city['Bangkok'] = CitySentiment('Bangkok')
city['Kabul'] = CitySentiment('Kabul')
city['London'] = CitySentiment('London')
city['Tokyo'] = CitySentiment('Tokyo')
    

# User input
listOfCities = {1:"Brasilia", 2:"New York", 3:"London", 4:"Bangkok", 5:"Kabul", 6:"Tokyo"}
print(listOfCities)
city_chosen = int(input("Choose a city according to its number: "))

if(city_chosen == 1):
    g = MapGraph()
    paths = g.getPaths('Brasilia')

    # Calculation
    for path in paths:
        print(path.path)

        # Shortest distance
        totalDistance = 0
        totalDistance += 1 / (path.distance * (paths.index(path)+1))
        pathProb = (1/path.distance) / float(totalPath())

        # Political sentiment
        totalPoli = 0
        pathSentiment = 0
        pathList = list(path.path)

        for i in range(1, len(pathList)-1):
            pathSentiment += city.get(pathList[i]).sentiment()
        
        pathSentiment /= len(pathList) - 2 
        path.pathSentiment = pathSentiment

        totalPoli += path.pathSentiment
        sentimentProb = path.pathSentiment / totalPoli
    
        # Shortest path + Political sentiment
        final = (pathProb + pathSentiment) / 2
        print("Total probability of this route: " + str(final) + "\n")

elif(city_chosen == 2):
    g = MapGraph()
    paths = g.getPaths('New York')

    # Calculation
    for path in paths:
        print(path.path)

        # Shortest distance
        totalDistance = 0
        totalDistance += 1 / (path.distance * (paths.index(path)+1))
        pathProb = (1/path.distance) / float(totalPath())

        # Political sentiment
        totalPoli = 0
        pathSentiment = 0
        pathList = list(path.path)

        for i in range(1, len(pathList)-1):
            pathSentiment += city.get(pathList[i]).sentiment()
        
        pathSentiment /= len(pathList) - 2 
        path.pathSentiment = pathSentiment

        totalPoli += path.pathSentiment
        sentimentProb = path.pathSentiment / totalPoli
    
        # Shortest path + Political sentiment
        final = (pathProb + pathSentiment) / 2
        print("Total probability of this route: " + str(final) + "\n")

elif(city_chosen == 3):
    g = MapGraph()
    paths = g.getPaths('London')

    # Calculation
    for path in paths:
        print(path.path)

        # Shortest distance
        totalDistance = 0
        totalDistance += 1 / (path.distance * (paths.index(path)+1))
        pathProb = (1/path.distance) / float(totalPath())

        # Political sentiment
        totalPoli = 0
        pathSentiment = 0
        pathList = list(path.path)

        for i in range(1, len(pathList)-1):
            pathSentiment += city.get(pathList[i]).sentiment()
        
        pathSentiment /= len(pathList) - 2 
        path.pathSentiment = pathSentiment

        totalPoli += path.pathSentiment
        sentimentProb = path.pathSentiment / totalPoli
    
        # Shortest path + Political sentiment
        final = (pathProb + pathSentiment) / 2
        print("Total probability of this route: " + str(final) + "\n")

elif(city_chosen == 4):
    g = MapGraph()
    paths = g.getPaths('Bangkok')

    # Calculation
    for path in paths:
        print(path.path)

        # Shortest distance
        totalDistance = 0
        totalDistance += 1 / (path.distance * (paths.index(path)+1))
        pathProb = (1/path.distance) / float(totalPath())

        # Political sentiment
        totalPoli = 0
        pathSentiment = 0
        pathList = list(path.path)

        for i in range(1, len(pathList)-1):
            pathSentiment += city.get(pathList[i]).sentiment()
        
        pathSentiment /= len(pathList) - 2 
        path.pathSentiment = pathSentiment

        totalPoli += path.pathSentiment
        sentimentProb = path.pathSentiment / totalPoli
    
        # Shortest path + Political sentiment
        final = (pathProb + pathSentiment) / 2
        print("Total probability of this route: " + str(final) + "\n")

elif(city_chosen == 5):
    g = MapGraph()
    paths = g.getPaths('Kabul')

    # Calculation
    for path in paths:
        print(path.path)

        # Shortest distance
        totalDistance = 0
        totalDistance += 1 / (path.distance * (paths.index(path)+1))
        pathProb = (1/path.distance) / float(totalPath())

        # Political sentiment
        totalPoli = 0
        pathSentiment = 0
        pathList = list(path.path)

        for i in range(1, len(pathList)-1):
            pathSentiment += city.get(pathList[i]).sentiment()
        
        pathSentiment /= len(pathList) - 2 
        path.pathSentiment = pathSentiment

        totalPoli += path.pathSentiment
        sentimentProb = path.pathSentiment / totalPoli
    
        # Shortest path + Political sentiment
        final = (pathProb + pathSentiment) / 2
        print("Total probability of this route: " + str(final) + "\n")

else:
    g = MapGraph()
    paths = g.getPaths('Tokyo')

    # Calculation
    for path in paths:
        print(path.path)

        # Shortest distance
        totalDistance = 0
        totalDistance += 1 / (path.distance * (paths.index(path)+1))
        pathProb = (1/path.distance) / float(totalPath())

        # Political sentiment
        totalPoli = 0
        pathSentiment = 0
        pathList = list(path.path)

        for i in range(1, len(pathList)-1):
            pathSentiment += city.get(pathList[i]).sentiment()
        
        pathSentiment /= len(pathList) - 2 
        path.pathSentiment = pathSentiment

        totalPoli += path.pathSentiment
        sentimentProb = path.pathSentiment / totalPoli
    
        # Shortest path + Political sentiment
        final = (pathProb + pathSentiment) / 2
        print("Total probability of this route: " + str(final) + "\n")
import os;
from article import article;

#user input
city = {1:"Brasilia", 2:"NewYork", 3:"London", 4:"Bangkok", 5:"Kabul", 6:"Tokyo"}
#print(city)
# city_chosen = int(input("Choose a city by key in its number"))
city_chosen = 1

#specify path
ROOT = os.path.dirname(os.path.abspath(__file__))
path = ROOT+"/Webpage_txt/"+city.get(city_chosen)
files = os.listdir(path)

#create obj and store in a list named articles
articles= []
i =0
for x in files:
    filename = path+"/"+files[i]
    articles.append(article(filename))
    print("Article " + str(i) + ": " + str(articles[i].getNoStopTotal())+ " FROM " + str(articles[i].getOriTotal()))
    i +=1

print("article pos word is " + str(articles[1].getPosCount()))
print("article neg word is " + str(articles[1].getNegCount()))

def sentiment():
    sentiment=0
    for j in articles:
        sentiment += j.polarity()

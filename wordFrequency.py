import os;
from article import article;
#user input
city = {1:"Brasilia", 2:"NewYork", 3:"London"}
#print(city)
# city_chosen = int(input("Choose a city by key in its number"))
city_chosen = 3;

#specify path
path = "D:/um/Semester 4/WIA2005 Algorithm Design and Analysis/Assignment";
path = path+"/Webpage_txt/"+city.get(city_chosen)
files = os.listdir(path)

#create obj and store in a list named articles
articles= []
i =0
for x in files:
    filename = path+"/"+files[i]
    articles.append(article(filename))
    print("Article " + str(i) + ": " + str(articles[i].getOriTotal()))
    i +=1

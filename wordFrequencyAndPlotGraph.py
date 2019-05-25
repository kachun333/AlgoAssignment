import os;
import numpy as np
import matplotlib.pyplot as plt
from article import article;
plt.style.use('ggplot')


def sentiment():
    sum=0
    for j in articles:
        sum += j.getPolarity()
    return sum/5

#user input
city = {1:"Brasilia", 2:"NewYork", 3:"London", 4:"Bangkok", 5:"Kabul", 6:"Tokyo"}
#print(city)
# city_chosen = int(input("Choose a city by key in its number"))
city_chosen = 2


#specify path
ROOT = os.path.dirname(os.path.abspath(__file__))
path = ROOT+"/Webpage_txt/"+city.get(city_chosen)
files = os.listdir(path)

#create obj and store in a list named articles
articles= []
i =0
for x in files:
    filename = path+"/"+files[i]
    print(filename)
    articles.append(article(filename))
    print("Article " + str(i) + ": " + str(articles[i].getNoStopTotal())+ " FROM " + str(articles[i].getOriTotal()))
    i +=1



articles[0].calculateWords()    #preprocessing for article 1
print("article pos word is " + str(articles[0].getPosCount()))
print("article neg word is " + str(articles[0].getNegCount()))
print("polarity is " + str(articles[0].getPolarity()))
articles[1].calculateWords()    #preprocessing for article 2
print("article pos word is " + str(articles[1].getPosCount()))
print("article neg word is " + str(articles[1].getNegCount()))
print("polarity is " + str(articles[1].getPolarity()))
articles[2].calculateWords()    #preprocessing for article 3
print("article pos word is " + str(articles[2].getPosCount()))
print("article neg word is " + str(articles[2].getNegCount()))
print("polarity is " + str(articles[2].getPolarity()))
articles[3].calculateWords()    #preprocessing for article 4
print("article pos word is " + str(articles[3].getPosCount()))
print("article neg word is " + str(articles[3].getNegCount()))
print("polarity is " + str(articles[3].getPolarity()))
articles[4].calculateWords()    #preprocessing for article 5
print("article pos word is " + str(articles[4].getPosCount()))
print("article neg word is " + str(articles[4].getNegCount()))
print("polarity is " + str(articles[4].getPolarity()))
print(sentiment())


N=5
ori_word = (int(articles[0].getOriTotal()), int(articles[1].getOriTotal()),int(articles[2].getOriTotal()),int(articles[3].getOriTotal()),int(articles[4].getOriTotal()))
stop_word = (int(articles[0].getNoStopTotal()), int(articles[1].getNoStopTotal()),int(articles[2].getNoStopTotal()), int(articles[3].getNoStopTotal()), int(articles[4].getNoStopTotal()))

index = np.arange(N)
width=0.35
plt.subplot(2,1,1)
plt.bar(index,ori_word,width,label="Original Word Count")
plt.bar(index + width, stop_word,width,label="Stop Word Count")
plt.ylabel("Word")
plt.title("Number of Word")
plt.xticks(index + width / 2, ('Article 1', 'Article 2', 'Article 3', 'Article 4', 'Article 5'))
plt.legend(loc='best')

pos_word = (int(articles[0].getPosCount()),int(articles[1].getPosCount()),int(articles[2].getPosCount()),int(articles[3].getPosCount()),int(articles[4].getPosCount()))
neg_word = (int(articles[0].getNegCount()),int(articles[1].getNegCount()),int(articles[2].getNegCount()),int(articles[3].getNegCount()),int(articles[4].getNegCount()))


plt.subplot(2,1,2)
plt.bar(index,pos_word,width,label="Positive Word Count")
plt.bar(index + width, neg_word,width,label="Negative Word Count")
plt.ylabel("Word")
plt.title("Number of Word")
plt.xticks(index + width / 2, ('Article 1', 'Article 2', 'Article 3', 'Article 4', 'Article 5'))
plt.legend(loc='best')
plt.show()

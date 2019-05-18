class classification:
from article import article;

Neg_path = "C:/Users/Chong Sin Mei/Desktop/UM Sem 4/Algorithm/AlgoAssignment/Webpage_txt/Negative Words Reference";
Pos_path = "C:/Users/Chong Sin Mei/Desktop/UM Sem 4/Algorithm/AlgoAssignment/Webpage_txt/Positive Words Reference";
freqN = 0
freqP = 0

    def calculateWords():
        #check all the words in the articles
        for i in words:
            if search(i, Pos_path, 3) is True
            freqP += 1
            elif search(i, Neg_path, 3) is True
            freqN += 1

    def formula():
        #find the percentage of positive/negative words in the article
        percentage = (freqP - freqN)/getWords
        return percentage

    def polarity():
        articles= []
        #store the corresponding percentage
        percent= []
        polarity=0
        i =0
        for x in files:
            filename = path+"/"+files[i]
            articles.append(article(filename))
            articles[i].calculateWords()
            percent[i] = articles[i].formula()
            i +=1
        for j in percent:
            polarity += percent[j]

import time
from RabinKarp import RabinKarp

class article:
    #read file and store each words in a list named text
    def __init__(self,filename):
        text_file=open(filename,"r")
        self.__words = text_file.read().lower()
        self.__noStopText = self.__removeStop(self.__words)
        self.__words = self.__words.split()
        self.__noStopWords = self.__noStopText.split()
        text_file.close()

    def functionA(self, text):
        return text
    #count number of words
    def getTotal(self, list):
        return len(list)

    #return dictionary
    def getWords(self, list):
        words= {}
        for x in list:
            words[x] = words.get(x,0) + 1
        return words

     #Total num of words in file b4 removing stop words
    def getOriTotal(self):
        return self.getTotal(self.__words)

    #dictionary of all words b4 removing stop Words
    def getOriWords(self):
        return self.getWords(self.__words)

     #Total num of words in file b4 removing stop words
    def getNoStopTotal(self):
        return self.getTotal(self.__noStopWords)

    #dictionary of all words b4 removing stop Words
    def getNoStopWords(self):
        return self.getWords(self.__noStopWords)

    def getNoStopText(self):
        return

    def __removeStop(self,text):
        # q = self.primeNum()
        # store a list of stop words
        stopWords = []
        path = "D:/um/Semester 4/WIA2005 Algorithm Design and Analysis/Assignment"
        text_file=open(path+"/Webpage_txt/stop_words.txt","r")
        stopWords = text_file.read().lower().split()
        text_file.close()
        #remove stop words 1 by 1
        for x in stopWords:
            self.search(x,text)
        print(text)
        return text

    #get the smallest prime num after total num of words in file
    # def primeNum(self):
    #     nextPrime = 10
    #     isPrime = False
    #     while(isPrime == False):
    #         time.sleep(0.1)
    #         isPrime = True
    #         for num in range(2,nextPrime):
    #             if (nextPrime % num == 0):
    #                 isPrime = False
    #                 break
    #         nextPrime +=1
    #     return nextPrime

    #search using Rabin-Karp Algorithm
    def search(self, pattern, text):
        text_hash = RabinKarp(text, len(text))
        pattern_hash = RabinKarp(pattern, len(pattern))

        for i in range(len(text) - len(pattern) + 1):
            if text_hash.hash == pattern_hash.hash:
                if text_hash.window_text() == pattern:
                    text[i:i+len(pattern)+1]=""

    #print all
    def output(self):
        print("Before removing stop words")
        print(self.getOriWords)
        print("The total words in the file is "+ self.getOriTotal)

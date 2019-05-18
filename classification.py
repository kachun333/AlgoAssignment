from article import article

class classification:
    ROOT = os.path.dirname(os.path.abspath(__file__))
    Neg_path = ROOT+"/Webpage_txt/Negative Words Reference";
    Pos_path = ROOT+"/Webpage_txt/Positive Words Reference";
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

                articles[i].calculateWords()

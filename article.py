
class article:
    text = []
    noStop = []

    #read file and store each words in a list named text
    def __init__(self,filename):
        text_file=open(filename,"r")
        self.text= text_file.read().lower().split()
        #self.noStop = removeStop(text_file.read().lower()).split()
        text_file.close()

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
        return self.getTotal(self.text)

    #dictionary of all words b4 removing stop Words
    def getOriWords(self):
        return self.getWords(self.text)

     #Total num of words in file b4 removing stop words
    def getNoStopTotal(self):
        return self.getTotal(self.noStop)

    #dictionary of all words b4 removing stop Words
    def getNoStopWords(self):
        return self.getWords(self.noStop)

    def removeStop(self,text):
        q = self.primeNum(getOriTotal)
        self.search(pattern, text, q)
        return text

    #get the smallest prime num after total num of words in file
    def primeNum(self, min):
        # for possiblePrime in range(2, 21):
        #     # Assume number is prime until shown it is not.
        #     isPrime = True
        #     for num in range(2, possiblePrime):
        #         if possiblePrime % num == 0:
        #             isPrime = False
        return 1511;

    #Rabin-Karp Algorithm
    def search(pat, txt, q):
        M = len(pat)
        N = len(txt)
        i = 0
        j = 0
        p = 0    # hash value for pattern
        t = 0    # hash value for txt
        h = 1

        # The value of h would be "pow(d, M-1)% q"
        for i in range(M-1):
            h = (h * d)% q

        # Calculate the hash value of pattern and first window of text
        for i in range(M):
            p = (d * p + ord(pat[i]))% q
            t = (d * t + ord(txt[i]))% q

        # Slide the pattern over text one by one
        for i in range(N-M + 1):
            # Check the hash values of current window of text and
            # pattern if the hash values match then only check
            # for characters on by one
            if p == t:
                # Check for characters one by one
                for j in range(M):
                    if txt[i + j] != pat[j]:
                        break

                j+= 1
                # if p == t and pat[0...M-1] = txt[i, i + 1, ...i + M-1]
                if j == M:
                    print("Pattern found at index " + str(i))

            # Calculate hash value for next window of text: Remove
            # leading digit, add trailing digit
            if i < N-M:
                t = (d*(t-ord(txt[i])*h) + ord(txt[i + M]))% q

                # We might get negative values of t, converting it to
                # positive
                if t < 0:
                    t = t + q

    #print all
    def output(self):
        print("Before removing stop words")
        print("Output: Words - Frequency")
        print(self.getOriWords)
        print("The total words in the file is "+ self.getOriTotal)

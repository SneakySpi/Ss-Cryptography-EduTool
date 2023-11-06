from math import log10

#the higher the value to more likely it is to be english
#the shorter the string the larger the quadgram
class ngram_score(object):
    def __init__(self,ngramfile,sep=' '):
        #load a file containing ngrams and counts, calculate log probabilities
        self.ngrams = {}
        f = open(ngramfile, "r")
        for line in f:
            key,count = line.split(sep) 
            self.ngrams[key] = int(count)
        self.L = len(key)
        self.N = sum(iter(self.ngrams.values()))
        #calculate log probabilities
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key])/self.N)
        self.floor = log10(0.01/self.N)

    def score(self,text):
        ''' compute the score of text '''
        score = 0
        ngrams = self.ngrams.__getitem__
        for i in range(len(text)-self.L+1):
            if text[i:i+self.L] in self.ngrams: score += ngrams(text[i:i+self.L])
            else: score += self.floor          
        return score
       
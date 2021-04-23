import nltk
import re 
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import codecs
import json
import os

results =[]

def process_lines(line):

    

    #converts all the characters in the string to lowercase
    line = line.lower()

    #remove all the digits from the string
    line = re.sub(r'\d+', '', line)

    #removing punctuation from the string
    line = line.translate(str.maketrans('','',string.punctuation))

    #removing leading and trailing whitespaces
    line = line.strip()

    #removing stopwords

    stop_words = set(stopwords.words('english'))

    tokens = word_tokenize(line)
    line = [i for i in tokens if not i in stop_words]

    #stemming using Porter Stemmer
    
    stemmer = PorterStemmer()
    
    
    for i in range(0,len(line)):
        line[i] = stemmer.stem(line[i])
    
    
    #lemmatization
    # lemmatizer = WordNetLemmatizer()
    
    # for i in range(0,len(line)):
    #     line[i] = lemmatizer.lemmatize(line[i])
    return line

x = input('enter the text for searching\n')

x = process_lines(x)[0]

# print(x)
with open(r'Inverted Index/inverted.json') as f:
  d = json.load(f)



for i in d:
    if x in d[i]:
        results.append((i,x,d[i][x]))


results = sorted(results, key=lambda tup: tup[2],reverse=True)


print(results)
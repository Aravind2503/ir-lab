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


d = {} #dictionary to store the inverted files

def preprocess(line,file_name):
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

    for i in line:
        if i not in d[file_name]:
            d[file_name][i]= 1
        else:
            d[file_name][i] += 1







os.chdir(r'./Inverted Index')
file_list = os.listdir()

for i in file_list:
    if i not in d:
        d[i]={}
    else:
        continue

for i in file_list:
    with codecs.open(i, 'r', encoding='utf-8',errors='ignore') as f:
        for line in f:
           preprocess(line,i)

print(d)

json_out = json.dumps(d)
f = open('inverted.json','w')
f.write(json_out)
f.close()
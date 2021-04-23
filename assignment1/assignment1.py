import nltk
import re 
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import codecs
import json

output = {}

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
    
    # stemmer = PorterStemmer()
    
    
    # for i in range(0,len(line)):
    #     line[i] = stemmer.stem(line[i])
    
    
    #lemmatization
    lemmatizer = WordNetLemmatizer()
    
    for i in range(0,len(line)):
        line[i] = lemmatizer.lemmatize(line[i])
    

    #putting all the finals list of words in a dictionary with their frequencies
    for i in line:
        if i in output:
            output[i] += 1
        else:
            output[i] = 1;


    # print(line)
    # print(output)


with codecs.open(r'./Document Preprocessing/Text3.txt', 'r', encoding='utf-8',errors='ignore') as f:
    for line in f:
        # print(line)
        
        process_lines(line)
    
#final dictionary
print(output)
json_out = json.dumps(output)
f = open('out3.json','w')
f.write(json_out)
f.close()
# process_lines('There are 3 red balls and 5 green BALLS in this box!@#!@$$#%$&&*@#$. There are several types of stemming algorithms')

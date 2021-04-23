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
import math


#query_vector
q_vec = {}

#count_dict
c_d = {}

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



def dot_product(a,b):
    product = 0 
    for i in a:
        if i in b:
            product += a[i]*b[i]
    
    return product
    
def magnitude(a):
    mag = 0
    for i in a:
        mag += a[i]**2
    
    return math.sqrt(mag)






query = input('enter the query string\n')
processed_query = process_lines(query)

# print(processed_query)


for i in processed_query:
    if i not in c_d:
        c_d[i] = 1
    else:
        c_d[i] += 1

maxi = c_d[max(c_d, key=c_d.get)]

# print(c_d)


#keeping the idf weights ready
with open(r'idf.json') as f:
  idf = json.load(f)

with open(r'tf_idf.json') as f:
  tf_idf = json.load(f)


for i in c_d:
    if i in idf:
        q_vec[i] = c_d[i]/maxi * idf[i]
    else:
        q_vec[i] = 0


# print(f'query_vector :{str(q_vec)}')
#for storing the results
result_set = []
for i in tf_idf:
    if dot_product(q_vec,tf_idf[i]) != 0.0:
        val = (dot_product(q_vec,tf_idf[i]))/(magnitude(q_vec)*magnitude(tf_idf[i]))
    else:
        val = 0.0
    result_set.append((val,i))

#sorting the result_set 
print(sorted(result_set,key = lambda tup:tup[0],reverse=True))









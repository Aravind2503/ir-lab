#probability model

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
import pandas as pd




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


#V is the set of retrieved docs N is the number of docs in the collection
def similarity(q_vec,N=10,V=5):
    tf_idf_docs={}
    with open('tf_idf.json') as f:
        tf_idf_docs = json.load(f)


    #similarity value for a query and the docs
    simi = 0

    for i in q_vec:
        vi = 0 # ki is the number of times the term ki occurs in the whole collection
        for j in tf_idf_docs:
            if i in tf_idf_docs[j]:
                vi += 1
        
        p_ki_r = (vi+0.5)(V+1)

        p_ki_not_r = (vi+0.5)(V+1)


def init_similarity(q_vec,N=10):
    tf_idf_docs={}
    with open('tf_idf.json') as f:
        tf_idf_docs = json.load(f)

    
    
    init_result=[]
    
    

    for i in tf_idf_docs:
        simi_d_q = 0 #similarity_document_query
        
        #to find how many docs have i in them
        for k in q_vec:
            ni = 0
            for kk in tf_idf_docs:
                if k in tf_idf_docs[kk]:
                    ni += 1
            ni_list.append(ni)
            
            if k in tf_idf_docs[i]:
                # print(ni,"this is ni",k,i,(ni/N)/(1-(ni/N)+0.5))
                simi_d_q += abs(q_vec[k] * tf_idf_docs[i][k] * math.log((ni/N)/(1-(ni/N)+0.5),10))
    
        init_result.append((i,simi_d_q))   
        

    #print the initial result here if you want

    init_result = sorted(init_result,key=lambda tup:tup[1],reverse=True)
       
    

    return init_result


def similarity(q_vec,result,N=10):

    tf_idf_docs={}
    with open('tf_idf.json') as f:
        tf_idf_docs = json.load(f)

    final=[]

    for i in result:
        simi_d_q = 0 #similarity_document_query
        
        #to find how many docs have i in them
        for k in q_vec:
            ni_num = 0 # for-iterating though the ni_list
            vi = 0
            for kk in result:
                if k in tf_idf_docs[kk[0]]:
                    vi += 1
            
            if k in tf_idf_docs[i[0]]:
                # print(ni,"this is ni",k,i,(ni/N)/(1-(ni/N)+0.5))
                simi_d_q += abs(q_vec[k] * tf_idf_docs[i[0]][k] * (math.log(vi+0.5/((len(result)-vi+0.5)),10)  + math.log((ni_list[ni_num]-vi+0.5)/(N-len(result)+0.5-vi+ni_list[ni_num]),10))   )
            
            ni_num += 1
            # print(i,simi_d_q)
        final.append((i[0],simi_d_q))   
        

    #print the initial result here if you want
    # print(final)    

    final = sorted(final,key=lambda tup:tup[1],reverse=True)
       
    

    return final







query = input('enter the query string\n')
processed_query = process_lines(query)

# print(processed_query)

#query vector
q_vec={}
c_d={} # count_vector for the q_vec frequency


idf={}

#ni-result-list
ni_list = []

with open('idf.json') as f:
    idf = json.load(f)

for i in processed_query:
    if i not in c_d:
        c_d[i] = 1
    else:
        c_d[i] += 1

maxi = c_d[max(c_d, key=c_d.get)]

# print(c_d)
for i in c_d:
    if i in idf:
        q_vec[i] = c_d[i]/maxi * idf[i]
    else:
        q_vec[i] = 0

#get the initial rankings
init_result = (init_similarity(q_vec)) # init_result is a list of the initial documents
# print(init_result)

init_res = pd.DataFrame(init_result,columns=['File Name','Similarity'])


init_result = [i for i in init_result if i[1]>0.0003]
# print(init_result)

final_result = similarity(q_vec,init_result,len(init_result))

# print("\n\n\n",final_result)



final_res = pd.DataFrame(final_result,columns=['File Name','Similarity'])

print(init_res,"\n\n\n\n")
print(final_res)


















#iterations ?
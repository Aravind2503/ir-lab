
# **<h1>IR LAB - 2nd Evaluation</h1>**

# # **Question 1**
# <h2>Probabilistic Model</h2>

import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import os,math,re

files = [r'../assignment1/Inverted Index/T1.txt',
         r'../assignment1/Inverted Index/T2.txt',
         r'../assignment1/Inverted Index/T3.txt',
         r'../assignment1/Inverted Index/T4.txt',
         r'../assignment1/Inverted Index/T5.txt',
         r'../assignment1/Inverted Index/T6.txt',
         r'../assignment1/Inverted Index/T7.txt',
         r'../assignment1/Inverted Index/T8.txt',
         r'../assignment1/Inverted Index/T9.txt',
         r'../assignment1/Inverted Index/T10.txt']
         
xfiles = [(i[len(i)-i[::-1].index('/'):]) for i in files ]


# Extract text from file, return text
def extract_text(fname):
    myf = open(fname,"rb")
    text = myf.read().decode(errors='replace')
    return text


#doing analysis
def uniqratio(token):
	return str(len(set(token))/len(token))

#Checking distribution of words
def freqDist(tokens,title):
  fdist1 = FreqDist(tokens)
  fdist1.plot(50, cumulative=True, title=title)

#Tokenizing the text, return token list
def preprocess(sentence):
 sentence = sentence.lower()
 tokenizer = RegexpTokenizer(r'\w+')
 tokens = tokenizer.tokenize(sentence)
 return nltk.word_tokenize(" ".join(tokens))

# Stopwords removal, return list
def sw_remove(tokens):
  stop = stopwords.words('english')
  new_tokens = [i for i in tokens if i not in stop]
  return new_tokens


#Stemming of tokens, return list
def stem_tokens(new_tokens):
    ps = PorterStemmer()
    stemmed = []
    for i in new_tokens:
        stemmed.append(ps.stem(i))
    return stemmed



inv_file = r'Inverted.csv'

def get_relevance(n,nw):
  return (n-nw+0.5)/(nw+0.5)

def get_prob_matrix(n, df, toks):
  prob_matrix = {}

  for i in toks:
    nw = df.loc[i, 'Occurences'].count(')')
    prob_matrix[i] = [nw, get_relevance(n,nw)]
  return prob_matrix

def get_query_tokens(query):
  tokens = preprocess(query.lower())
  tokens = sw_remove(tokens)
  tokens = stem_tokens(tokens)
  return tokens

def get_cond_probability(qtok, inv_file):
  prob_matrix = {}

  df = pd.read_csv(inv_file)
  toks = list(df['Tokens'])

  df.set_index('Tokens',inplace=True)

  word_matrix = get_prob_matrix(len(xfiles), df, toks)

  for i in xfiles:
    flag = False
    val = 1
    prob_matrix[i] = 0

    for j in qtok:
      if j in toks:
        if i in df.loc[j,'Occurences']:
          flag = True
          val *= word_matrix[j][1]
    prob_matrix[i] = val if flag else 0
 
  return prob_matrix

print("-:"+"Probabilistic Model :- \n -: Compute Similarity "+":-")

print("Query : ")
vect = get_cond_probability(get_query_tokens(input()),inv_file)

vect = {k: "{0:.5f}".format(v) for k, v in sorted(vect.items(), key=lambda item: item[1], reverse=True)}

print(pd.DataFrame(vect.items(),columns=['File','Relevance']))

### **-------------------------------------------------------------------------------------**

# # **Question 2**
# # <h2>Evaluation measures</h2>

# ## ***(a)*** *Calculate Recall and Precision, plot the same and calculate R-Precision*


# Rq = ['d3','d5','d9','d25','d39','d44','d56','d71','d89','d123']
# Aq = ['d123','d84','d56','d6','d8','d9','d511','d129','d187','d25','d38','d48','d250','d113','d3']

# def calrp(Rq,Aq):
#   doc_count = 0
#   rn = len(Rq)
#   recall, precision = {},{}

#   for i in range(len(Aq)):
#     if Aq[i] in Rq:
#       doc_count += 1
#       recall[Aq[i]] = (round(doc_count/rn,2))
#       precision[Aq[i]] = (round(doc_count/(i+1),2))
#     else:
#       pass
      
#   return pd.DataFrame({'Recall':pd.Series(recall),'Precision':pd.Series(precision)})

# # Recall and Precision
# rnp = calrp(Rq,Aq)
# rnp

# # Plotting Recall vs Precision curve
# x = list(rnp['Recall'])
# x.insert(0,0)
# x.extend(np.arange(x.pop(),1.1,0.1))
# x = [round(a, 1) for a in x][:-1]

# y = list(rnp['Precision'])
# y.insert(0,1.0)
# y.extend([0]*(len(x)-len(y)))

# plt.scatter(x,y,color='red')
# plt.plot(x,y)
# plt.xlabel = 'Recall'
# plt.ylabel= 'Precision'
# plt.show()

# # Calculating R-Precision
# rn = len(Rq)
# setAq = Aq[:rn]
# r_prec = len(list((Counter(Rq) & Counter(setAq)).elements()))/rn
# print ('R-Precision : ' +str(r_prec))

# """## ***(b)*** *Performance comparision of 2 IR algorithms*"""

# Rq = ['d3','d5','d9','d25','d39','d44','d56','d71','d89','d123']
# A1 = ['d123','d84','d56','d6','d8','d9','d511','d129','d187','d25','d38','d48','d250','d113','d3']
# A2 = ['d12','d39','d13','d123','d8','d9','d19','d89','d87','d25','d70','d71','d29','d44','d3']

# rnp_A1 = calrp(Rq,A1)
# rnp_A2 = calrp(Rq,A2)

# # Recall and Precision of the 2 IR models

# rnp_A1

# rnp_A2.sort_values('Recall')

# # Plotting Recall vs Precision curve

# # plotting for A1
# x = list(rnp_A1['Recall'])
# x.insert(0,0)
# x.extend(np.arange(x.pop(),1.1,0.1))
# x = [round(a, 1) for a in x][:-1]

# y1 = list(rnp_A1['Precision'])
# y1.insert(0,1.0)
# y1.extend([0]*(len(x)-len(y1)))

# plt.scatter(x,y1,color='red')
# plt.plot(x,y1,color='black')

# y2 = list(rnp_A2['Precision'])
# y2.insert(0,1.0)
# y2.extend([0]*(len(x)-len(y2)))

# plt.scatter(x,y2,color='blue')
# plt.plot(x,y2,color='black')

# plt.xlabel = 'Recall'
# plt.ylabel= 'Precision'
# plt.show()

# y = [e1-e2 for (e1, e2) in zip(y1,y2)] 
# dl = pd.DataFrame({'Recall':x, 'Precision':y})
# ax = dl.plot.bar(x='Recall', y='Precision', rot=0)
# print(ax)

# print('A1 is better' if sum(y)>=0 else 'A2 is better')

# ## ***(c)*** *Calculate Harmonic Mean and E-Measure*"""

# Rq = ['d3','d5','d9','d25','d39','d44','d56','d71','d89','d123']
# A1 = ['d123','d84','d56','d6','d8','d9','d511','d129','d187','d25','d38','d48','d250','d113','d3']

# def calhm(Rq,Aq):
#   doc_count = 0
#   rn = len(Rq)
#   recall, precision,hm, em1, em2 = {},{},{},{}, {}

#   for i in range(len(Aq)):
#     if Aq[i] in Rq:
#       doc_count += 1
#       recall[Aq[i]] = (round(doc_count/rn,2))
#       precision[Aq[i]] = (round(doc_count/(i+1),2))
#       hm[Aq[i]] = round(2/((1/recall[Aq[i]])+(1/precision[Aq[i]])),2)

#       #Set b=2 for E-Measure
#       b = 2
#       em1[Aq[i]] = round((1+(b**2))/(((b**2)/recall[Aq[i]])+(1/precision[Aq[i]])),2)

#       b=0.1
#       em2[Aq[i]] = round((1+(b**2))/(((b**2)/recall[Aq[i]])+(1/precision[Aq[i]])),2)

#     else:
#       pass
      
#   return pd.DataFrame({'Recall':pd.Series(recall),'Precision':pd.Series(precision),'Harmonic mean':pd.Series(hm),'E-Measure (b>1)':pd.Series(em1),'E-Measure (b<1)':pd.Series(em2)})

# # Harmonic Mean and E-Measure
# hne = calhm(Rq,Aq)
# hne

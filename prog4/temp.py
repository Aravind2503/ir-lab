# from __future__ import division
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
# %matplotlib inline


# Helper functions for inv_ind()
class CreateInvDict:
    def __init__(self):
        self.myd = {}
    def checkf(self, x, i):
        if i not in self.myd.keys():
            self.myd[i] = [x]
        else:
            self.myd[i].append(x)

def freq_list(str,word):
    count = str.count(word)
    mid = -1
    freq = []
    for i in range(count):
        prev = str[mid+1:].index(word)
        mid += (prev+1)
        freq.append(mid)
    return freq

def freq_count(text, word):
    return text.count(word)

#Inverted index, return dictionary
def inv_ind(stemmed_docs,doc_sizes,n):
    unq_tok = set(stemmed_docs)
    inv_table = CreateInvDict()
    for i in unq_tok:
        start = 0
        for j in range(n):
            end = doc_sizes[j]
            temp = stemmed_docs[start:(start+end)]
            if i in temp:
                x = (xfiles[j],freq_count(temp,i))
                inv_table.checkf(x,i)
            start += end
    return inv_table.myd



# nltk.download('stopwords')
# nltk.download('punkt')


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


# Data-Preprocessing

filename = "/content/drive/My Drive/Colab Notebooks/mydata/Text1.txt"

# text = extract_text(filename)

# print("\n-------- STATISTICS --------\n")
# tokens = preprocess(text)

# print("Ratio of unique words : "+uniqratio(tokens))
# freqDist(tokens, "After token creation")

# tokens = sw_remove(tokens)

# print("Ratio of unique words : "+uniqratio(tokens))
# freqDist(tokens, "After token creation")

# tokens = stem_tokens(tokens)

# print("\n-------- TOKENS -------- \n")
# print(pd.DataFrame(tokens))



#List of files
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

n = len(files)
doc_sizes = []
stemmed = []
for i in files:
    text = extract_text(i)
    tokens = preprocess(text)
    tokens = sw_remove(tokens)
    tokens = stem_tokens(tokens)
    doc_sizes.append(len(tokens))
    stemmed.extend(tokens)

table = inv_ind(stemmed,doc_sizes,n)
df = pd.DataFrame(table.items(), columns=['Tokens','Occurences'])
try:
    os.remove(r'Inverted.csv')
except:
    pass
df.to_csv(r'Inverted.csv')




















#Probabilistic Model

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
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

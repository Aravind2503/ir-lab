# get all the different words in all the documents 
# compute idf weight log2(N/ni)

import json
import pprint
import math
import os

os.chdir(r'Inverted Index')
dir_list = os.listdir()
os.chdir(r'../')

N = len(dir_list)# N for idf-weight


# stores the number of occurences of each word in the collection
idf = {}
#stores the tf of each word in each doc
tf = {}
#stores tf-idf of all docs
tf_idf = {}
#vector representation of the docs
doc_vector ={}


maxi = 0

def tf_weight(d):
    for i in d: # name of all the documents
        tf[i]={}
        maxi = d[i][max(d[i], key=d[i].get)]
        for j in d[i]: #all the words in the documents
            tf[i][j] = d[i][j]/maxi



def idf_weight(d):
    for i in d:
        for j in d[i]:
            if j  not in idf:
                idf[j] = 1
            else:
                idf[j] += 1

    for i in idf:
        idf[i] = math.log(N/idf[i],2)


def tf_idf_weight():
    for i in tf:
        tf_idf[i] = {}
        for j in tf[i]:
            tf_idf[i][j] = tf[i][j]*idf[j]

    


with open(r'Inverted Index/inverted.json') as f:
  d = json.load(f)

idf_weight(d)
tf_weight(d)
tf_idf_weight() # calculated tf_idf weight of all the documents and stored it here

json_out = json.dumps(idf)
f = open('idf.json','w')
f.write(json_out)
f.close()

json_out = json.dumps(tf)
f = open('tf.json','w')
f.write(json_out)
f.close()

# print(tf_idf)





json_out = json.dumps(tf_idf)
f = open('tf_idf.json','w')
f.write(json_out)
f.close()




import json
import numpy as np
import math
import pandas as pd

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

#reading the tf-idf weight 
with open('../assignment1/tf_idf.json','r') as f:
    tf_idf = json.load(f)
# print(tf)

cm=np.zeros((10,10))
ii=0
jj=0
l=[]
cols =[]

for i in tf_idf:
    cols.append(i)
    for j in tf_idf:
        
        
        cm[ii][jj] = dot_product(tf_idf[i], tf_idf[j])/(magnitude(tf_idf[i])*magnitude(tf_idf[j]))

        # l[ii].append(val)
        jj +=1
    jj=0
    ii+=1

# print(cm)

s = pd.DataFrame(cm,columns=cols,index=cols)
print(s)

# print(l)
        
    


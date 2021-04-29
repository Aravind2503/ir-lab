import matplotlib.pyplot as plt
# matplotlib.use("gtk")
import pandas as pd 

#set of relevant documents 
rq = [3,5,9,25,39,44,56,71,89,123]

#answer set 
aq = [123,84,56,6,8,9,511,129,187,25,38,48,250,113,3]


# #set of relevant documents 
# rq = [3,56,123]

# #answer set 
# aq = [123,84,56,6,8,9,511,129,187,25,38,48,250,113,3];


#recall
recall=[]

#precision
precision =[]


rlen = len(rq)
alen = len(aq)

recall_count =0

#to keep track of the retrieved documents
precision_count =0
# pc = 0

rr=0
pp=0

for i in aq:
    precision_count += 1
    if i in rq:
        recall_count += 1
        

        rr = recall_count/len(rq)
        pp = recall_count/precision_count

    # print(rr,pp,recall_count,precision_count)
    recall.append(rr*100)
    precision.append(pp*100)


plt.plot(recall,precision)
plt.title('recall precision curve')
plt.xlabel('recall')
plt.ylabel('precision')
plt.xlim(0,150)
plt.ylim(0,150)
plt.show()


#r-precision

algo_a =[]
algo_b =[]

def r_precision(a,b,r):
    c1 = 0
    c2 = 0
    for i in a:
        if i in r:
            c1 += 1
    for i in b:
        if i in r:
            c2 += 1 

    algo_a.append(c1/len(a))
    algo_b.append(c2/len(b))






#list of the 5 queries
r1 = [3,5,9,25,39,44,56,71,89,123]
a1 = [123,84,56,6,8,9,511,129,187,25,38,48,250,113,3]
b1 = [12,39,13,123,8,9,19,89,87,25,70,71,29,44,3]

r2 = [3,20, 5, 68, 51, 21, 27, 64, 6, 93]
a2 = [3,13,5,68,51,67,32,64,45,6,94,95,93]
b2 = [20,30,7,78,21,27,14,15,16,6,54,4,6]

r3 = [9 ,76, 78, 31, 7, 47, 30, 8, 43, 51]
a3 = [78,9,48,47,4,31,43,56,55,99,123,222]
b3 = [76,75,31,7,30,44,56,50,94,223]

r4 = [85, 95, 25, 64, 52, 12, 43, 18, 6, 66]
a4 = [52,62,64,77,12,45,18,43,6]
b4 = [95,85,25,77,123,3213,78,18,6]

r5 = [38, 65, 73, 88, 93, 74, 36, 4, 28, 30]
a5 = [56,73,65,3,2,99,146,93,76,74,4]
b5 = [66,88,45,43,23,12,188,200,34,4]

r_precision(a1, b1, r1)
r_precision(a2, b2, r2)
r_precision(a3, b3, r3)
r_precision(a4, b4, r4)
r_precision(a5, b5, r5)



print('algo_a is better' if sum(algo_a)>sum(algo_b)else 'algo_b is better')




# algo_a = [0.3,0.6,0.3,0.5,1,0.78,0.24]
# algo_b = [0.1,0.3,0.6,0.4,0,0.7,0.01]

x = map(lambda a,b:a-b,algo_a,algo_b)
x = list(x)


fig = plt.figure(figsize=(10,10))
langs = [i for i in range(1,len(x)+1)]

plt.xlabel("Query Number")
plt.ylabel("R Precision A/B")
plt.title("Precision histogram")


plt.bar(langs,list(x),color='orange',width=0.5)

plt.show()

#harmonic mean and e measure 
Rq = ['d3','d5','d9','d25','d39','d44','d56','d71','d89','d123']
A1 = ['d123','d84','d56','d6','d8','d9','d511','d129','d187','d25','d38','d48','d250','d113','d3']

def calhm(Rq,Aq):
  doc_count = 0
  rn = len(Rq)
  recall, precision,hm, em1, em2 = {},{},{},{}, {}

  for i in range(len(Aq)):
    if Aq[i] in Rq:
      doc_count += 1
      recall[Aq[i]] = (round(doc_count/rn,2))
      precision[Aq[i]] = (round(doc_count/(i+1),2))
      hm[Aq[i]] = round(2/((1/recall[Aq[i]])+(1/precision[Aq[i]])),2)

      #Set b=2 for E-Measure
      b = 2
      em1[Aq[i]] = round((1+(b**2))/(((b**2)/recall[Aq[i]])+(1/precision[Aq[i]])),2)

      b=0.1
      em2[Aq[i]] = round((1+(b**2))/(((b**2)/recall[Aq[i]])+(1/precision[Aq[i]])),2)

    else:
      pass
      
  return pd.DataFrame({'Recall':pd.Series(recall),'Precision':pd.Series(precision),'Harmonic mean':pd.Series(hm),'E-Measure (b>1)':pd.Series(em1),'E-Measure (b<1)':pd.Series(em2)})

# Harmonic Mean and E-Measure
hne = calhm(Rq,A1)
print()
print()
print(hne)






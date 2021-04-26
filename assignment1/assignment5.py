import matplotlib.pyplot as plt
# matplotlib.use("gtk")

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

    print(rr,pp,recall_count,precision_count)
    recall.append(rr*100)
    precision.append(pp*100)


plt.plot(recall,precision)
plt.title('recall precision curve')
plt.xlabel('recall')
plt.ylabel('precision')
plt.xlim(0,150)
plt.ylim(0,150)
plt.show()


algo_a = [0.3,0.6,0.3,0.5,1,0.78,0.24]
algo_b = [0.1,0.3,0.6,0.4,0,0.7,0.01]

x = map(lambda a,b:a-b,algo_a,algo_b)
x = list(x)


fig = plt.figure(figsize=(10,10))
langs = [i for i in range(1,len(x)+1)]

plt.xlabel("Query Number")
plt.ylabel("R Precision A/B")
plt.title("Precision histogram")


plt.bar(langs,list(x),color='orange',width=0.5)

plt.show()



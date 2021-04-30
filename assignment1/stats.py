
import os
import pandas as pd
import numpy as np

l = np.zeros((4,2))



l[0][0] = os.path.getsize(r'./Document Preprocessing/LargeText.txt')/1000

l[1][0] = os.path.getsize(r'./Document Preprocessing/Text1.txt')/1000

l[2][0] = os.path.getsize(r'./Document Preprocessing/Text2.txt')/1000

l[3][0] = os.path.getsize(r'./Document Preprocessing/Text3.txt')/1000


l[0][1] = os.path.getsize('out.json')/1000
l[1][1] = os.path.getsize('out1.json')/1000
l[2][1] = os.path.getsize('out2.json')/1000
l[3][1] = os.path.getsize('out3.json')/1000


df = pd.DataFrame(l,columns=['Original','Modified'],index=['LargeText.txt','Text1.txt','Text2.txt','Text3.txt'])
print(df)
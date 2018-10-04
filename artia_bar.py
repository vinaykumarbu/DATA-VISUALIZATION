import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ait=pd.read_csv("Python programs/atria_ise.csv")
ait.set_index('USN', inplace=True)
usn=input("Enter USN for result(eg:1AT15IS063):")
marks=ait.loc[usn] 
subject = ['ME','CN','ADV JAVA','DBMS','FLAT','CC','CN Lab','DBMS Lab']

colors = []
for i in marks:   
    if i < 40:
        colors.append('red')
    else:
        colors.append('blue')
        

plt.bar(range(len(marks)), marks, color = colors,width=0.50)                                
plt.xlabel('SUBJECT')
plt.ylabel('SCORE')
plt.title(usn,color='green')
plt.xticks(range(len(marks)), subject)
plt.xticks(rotation=0)
plt.ylim(0,100)
plt.legend(title='RESULT',labels=['Pass','Fail'])
plt.show()
        

 #marks.plot(kind = 'bar', color = colors)

    
    
    
    
    









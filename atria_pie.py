import matplotlib.pyplot as plt
import pandas as pd

ait=pd.read_csv("Python programs/atria_ise.csv")
subject=input("Enter the subject to check result(eg:ME,CN):")
sname=ait[subject]

failed = []
passed = []
        
for i in sname:
    failed.append(i) if  i < 40 else  passed.append(i)  #ternary operator
        
x1=len(failed)
x2=len(passed)

plt.pie([x1,x2],colors=['#ee2222','#1ec71e'],labels=['Fail','Pass'],startangle=90,shadow=True,explode=(0.1,0),autopct='%1.1f%%')
plt.title(subject,color='Blue')
plt.legend(title='Result')
plt.show()




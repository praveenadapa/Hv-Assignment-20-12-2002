import pandas as pd
num=list(map(int,input().split()))
x=pd.Series(num)
print("Series:\n",x)
print(x*x)
for j in x:
    print(j*j,end=" ")
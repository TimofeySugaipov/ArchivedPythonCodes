import numpy as np
import pandas as pd

def salary(n, s = 0.01):
    if not 1<=n<=20:
        return("Incorrect Value")
    else:
        total = 0
        L = []
        for i in range(1,n+1):
            total += s
            total = round(total,2)
            L.append([int(i),"$"+str(s),"$"+str(total)])
            s *= 2
        df = pd.DataFrame(np.array(L),columns = ['Day', 'Salary', 'Total'])
        return(df)
print(salary(10))

#!/usr/bin/env python
# coding: utf-8

# In[1]:


class nuclear_count:
    def __init__(self,loc,col_name):
        import pandas as pd
        import numpy as np
        self.data = pd.read_csv(loc)
        self.col = col_name
        self.m = np.mean(pd.read_csv(loc)[col_name])
        
        import numpy
        val = []
        for i in self.data[self.col]:
            val.append((i-self.m)**2)
        sig = sum(val)
        sig1 = sig/100
        sigma = np.sqrt(sig1)
        self.sigma = sigma
        self.val = val
        print("Sigma is ",self.sigma)
        print("mean of xi(m) is ", self.m)
        import numpy as np
        output = []
        for i in self.data[self.col]:
            rhs = np.exp((-(i-self.m)**2)/(2*self.sigma**2))
            rhs1 = 1/(self.sigma*np.sqrt(2*3.14))
            output.append(rhs*rhs1)
        self.p = output
        
    
        import pandas as pd
        #tab = self.data.copy()
        #tab[["(Xi-m)^2","P(x)"]] = self.val,self.p
        #tab = pd.DataFrame(self.val,columns=["(Xi-m)^2"])
        tab = pd.DataFrame()
        tab['Xi'] = self.data[self.col]
        tab["(Xi-m)^2"] = self.val
        tab['P(X)'] = self.p
        self.tab = tab
    def table(self):
        return self.tab
    def plot(self):
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        import seaborn as sns
        center = []
        for i in [self.m]:
            rhs = np.exp((-(i-self.m)**2)/(2*self.sigma**2))
            rhs1 = 1/(self.sigma*np.sqrt(2*3.14))
            center.append(rhs*rhs1)

        rf = []
        for i in [self.m+self.sigma]:
            rhs = np.exp((-(i-self.m)**2)/(2*self.sigma**2))
            rhs1 = 1/(self.sigma*np.sqrt(2*3.14))
            rf.append(rhs*rhs1)
        print(rf)
        plt.figure(figsize=(10,7))
        sns.lineplot("Xi","P(X)",data = self.tab)
        plt.title("Xi vs P(X)")
        plt.xlabel("Counts Xi")
        plt.ylabel("P(X)")            
        plt.plot([self.m,self.m],[0,center[0]])
        plt.annotate(text = str(self.m),xy = (self.m-7,0.0002),fontsize=11)
        plt.plot([self.m+self.sigma , self.m-self.sigma],[rf[0],rf[0]])
        plt.plot([self.m+self.sigma,self.m+self.sigma],[0,rf[0]])
        plt.plot([self.m-self.sigma,self.m-self.sigma],[0,rf[0]])
        plt.annotate(text = str(round(self.m+self.sigma,2)),xy = ((self.m+self.sigma)-10,0.0002),fontsize=11)
        plt.annotate(text = str(round(self.m-self.sigma,2)),xy = ((self.m-self.sigma)-10,0.0002),fontsize=11)
        plt.grid()


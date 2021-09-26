#!/usr/bin/env python
# coding: utf-8

# In[54]:


class particle_count:
    '''
    particle_count(loc , col_name)
    
    How to use this package??
    Ex:
    
    nuc = nuc_count.particle_count(loc = "....../nuclear count2.xlsx",col_name="Xi")
    enter location in this format : "C:/Users/something/Desktop/nuclear count2.xlsx"
    
    for table : 
    nuc.table()
    to save data in excel
    nuc.savetable(filename = "Enter file name")
    Ex:
    nuc.savetable(filename = "nc")
    
    for graph:
    nuc.plot()
    
    to save plot as image
    nuc.plot(filename = "Enter file name")
    Ex:
    nuc.plot(filename = "nc")
    
    Parameters
    ----------
    loc: location of excel
    col_name = data(counts xi) - column name
    
    ------------Credits :-  AUW4 ------------------
    '''
    def __init__(self,loc,col_name):
        import pandas as pd
        import numpy as np
        self.data = pd.read_excel(loc)
        
        self.col = col_name
        self.m = np.mean(self.data[col_name])
        
        
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
        
        output = []
        for i in self.data[self.col]:
            rhs = np.exp((-(i-self.m)**2)/(2*self.sigma**2))
            rhs1 = 1/(self.sigma*np.sqrt(2*3.14))
            output.append(rhs*rhs1)
        self.p = output
        
    
        
        #tab = self.data.copy()
        #tab[["(Xi-m)^2","P(x)"]] = self.val,self.p
        #tab = pd.DataFrame(self.val,columns=["(Xi-m)^2"])
        tab = pd.DataFrame()
        tab['Xi'] = self.data[self.col]
        tab["(Xi-m)^2"] = self.val
        tab['P(X)'] = self.p
        self.tab = tab.sort_values(by = "P(X)",ascending=True).reset_index(drop = True)
    def table(self):
        import pandas as pd
        pd.set_option("max_rows",len(self.data['Xi']))
        return self.tab
    def savetable(self,filename):
        self.tab.to_excel(filename+".xlsx",index = False)
        
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

        plt.figure(figsize=(10,7))
        sns.lineplot(x = "Xi",y = "P(X)", markers=True,data = self.tab)
        sns.scatterplot(x = "Xi",y = "P(X)", markers=True,data = self.tab)
        #plt.plot(self.tab['Xi'],self.tab["P(X)"])
        plt.title("Xi vs P(X)")
        plt.xlabel("Counts Xi")
        plt.ylabel("P(X)")            
        plt.plot([self.m,self.m],[0,center[0]])
        
        plt.plot([self.m+self.sigma , self.m-self.sigma],[rf[0],rf[0]])
        plt.plot([self.m+self.sigma,self.m+self.sigma],[0,rf[0]])
        plt.plot([self.m-self.sigma,self.m-self.sigma],[0,rf[0]])
        plt.annotate(text = str(self.m),xy = (self.m-7,0.0002),fontsize=11)
        plt.annotate(text = str(round(self.m+self.sigma,2)),xy = ((self.m+self.sigma)-10,0.0002),fontsize=11)
        plt.annotate(text = str(round(self.m-self.sigma,2)),xy = ((self.m-self.sigma)-10,0.0002),fontsize=11)
        
        plt.annotate(text = str(round(rf[0],8)),xy = (self.m+self.sigma,rf[0]),fontsize=11)
        plt.annotate(text = str(round(center[0],8)),xy = (self.m-10,center[0]+0.00009),fontsize=11)
        plt.grid()
    def saveplot(self,filename):
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

        plt.figure(figsize=(10,7))
        sns.lineplot(x = "Xi",y = "P(X)", markers=True,data = self.tab)
        sns.scatterplot(x = "Xi",y = "P(X)", markers=True,data = self.tab)
        #plt.plot(self.tab['Xi'],self.tab["P(X)"])
        plt.title("Xi vs P(X)")
        plt.xlabel("Counts Xi")
        plt.ylabel("P(X)")            
        plt.plot([self.m,self.m],[0,center[0]])
        
        plt.plot([self.m+self.sigma , self.m-self.sigma],[rf[0],rf[0]])
        plt.plot([self.m+self.sigma,self.m+self.sigma],[0,rf[0]])
        plt.plot([self.m-self.sigma,self.m-self.sigma],[0,rf[0]])
        plt.annotate(text = str(self.m),xy = (self.m-7,0.0002),fontsize=11)
        plt.annotate(text = str(round(self.m+self.sigma,2)),xy = ((self.m+self.sigma)-10,0.0002),fontsize=11)
        plt.annotate(text = str(round(self.m-self.sigma,2)),xy = ((self.m-self.sigma)-10,0.0002),fontsize=11)
        
        plt.annotate(text = str(round(rf[0],8)),xy = (self.m+self.sigma,rf[0]),fontsize=11)
        plt.annotate(text = str(round(center[0],8)),xy = (self.m-10,center[0]+0.00009),fontsize=11)
        plt.grid()
        plt.savefig(filename+".jpg",format = "jpg",dpi = 200)


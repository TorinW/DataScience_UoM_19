# DataScience_UoM_19
1. Code for intializing data and looking into the basic statitical insights

'''
import numpy as np  

import csv  

import pandas as pd  


import matplotlib.pyplot as plt  

#%matplotlib inline   

datafile = "PSID.csv"  


D1=pd.read_csv(datafile,delimiter=',')  

Atrr=D1.describe()  
'''  




Hypothesis/Question
1. "Is education level affect to keep the marriage?"
- People who have education level higher than level 10 have high probability of ended with divorce/seperated compared to the rest.


µs – Mean of education level for separated or divorced individuals    

µn- Mean of education level for married and non-separated individuals  

H0 => Null Hypothesis        µs= µn  
Ha => Alternate Hypothesis   µs ≠ µn  

 
 2. "Is working more hours increase the average income?"  
 
 µh – Mean of average icome for individuals working more than 2600 hours  
 µl- Mean ofaverage icome for individuals working less than 2600 hours  
 


H0 => Null Hypothesis        µh= µl  
Ha => Alternate Hypothesis   µh> µn 
    
    





Visualizations
*divorced/separated stats on edu level less than 11
![divorced/separated stats on edu level less than 11](https://github.com/TorinW/DataScience_UoM_19/blob/master/0-10_2-3.PNG)


*divorced/separated stats on edu level greater than 10
![divorced/separated stats on edu level greater than 11](https://github.com/TorinW/DataScience_UoM_19/blob/master/11-99_2-3.PNG)

Assumption


References

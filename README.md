# DataScience_UoM_19
1. Code for intializing data and looking into the basic statitical insights

```python
import numpy as np  

import csv  

import pandas as pd  


import matplotlib.pyplot as plt  

#%matplotlib inline   

datafile = "PSID.csv"  


D1=pd.read_csv(datafile,delimiter=',')  

Atrr=D1.describe()  
``` 
>>Sample Statistics*
![Sample Statistics](https://github.com/TorinW/DataScience_UoM_19/blob/master/descriptive_stats.png)

2. Analyzing the age distribution

```python
import csv
import pandas as pd

import matplotlib.pyplot as plt
#%matplotlib inline

datafile = "PSID.csv"

D1=pd.read_csv(datafile,delimiter=',')

D1.age.plot(kind='kde')
```
>>Age distribution*
![Sample Statistics](https://github.com/TorinW/DataScience_UoM_19/blob/master/age_destribution.png)

The age distribution of the sample is biased towards the 30-40 range.
- From the sample statistics age has shown biased to 38.46 with the standard deviation of 5.59.
- The above distribution plot for age shows that the age is not uniformly distributed. 



Hypothesis/Question
1. "Is education level affect to keep the marriage?"
- People who have education level higher than level 10 have high probability of ended with divorce/seperated compared to the rest.


µs – Mean of education level for separated or divorced individuals    

µn- Mean of education level for married and non-separated individuals  

H0 => Null Hypothesis        µs= µn  
Ha => Alternate Hypothesis   µs ≠ µn  
```python  
MarriedOnly=D1.loc[D1['married'] == 'married']
µn=MarriedOnly['educatn'].mean()       #mean education level for married 


Seperated=D1.loc[D1['married']=='separated']# mean education level for seperated/divorced 

Seperated= D1.loc[D1['married']=='divorced']

µs=Seperated['educatn'].mean()

```
µs=15.33  
µn=19.34

 
 2. "Is working more hours increase the average income?"  
 
 µh – Mean of average icome for individuals working more than 2600 hours  
 µl- Mean ofaverage icome for individuals working less than 2600 hours  
 


H0 => Null Hypothesis        µh= µl  
Ha => Alternate Hypothesis   µh> µn 
    
    





Visualizations
>>Divorced/separated stats on edu level less than 11*
![divorced/separated stats on edu level less than 11](https://github.com/TorinW/DataScience_UoM_19/blob/master/0-10_2-3.PNG)


>>divorced/separated stats on edu level greater than 10*
![divorced/separated stats on edu level greater than 11](https://github.com/TorinW/DataScience_UoM_19/blob/master/11-99_2-3.PNG)


*Graphs generated by using Power BI Tool


Assumption


References

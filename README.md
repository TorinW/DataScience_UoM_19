# DataScience_UoM_19

> Code for intializing data and looking into the basic statitical insights

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

> Analyzing the age distribution

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



**_Hypothesis/Question**   

Confidence interval is given as  
CI=statistic +- z*SE  

Where as  
z=(statistic-H0)/sigma  
SE=sigma/root(n)                                 
                                  
                                   
                                  

1. "_Is education level affect to keep the marriage?"
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

#confidence interval calculation 
statistic1=D1['educatn'].mean()
sigma1=D1['educatn'].std()
z1=(statistic1-0)/(sigma1)
SE1=sigma1/math.sqrt(D1['educatn'].count())

CI1=(statistic1+z1*SE),(statistic1-z1*SE1)

```
µs=15.33  
µn=19.34
Since µs<µn alternate hypothesis holds and data is statistically significant.  
Hence increase in education level increases seperation/ divorce :).  

Confidence Interval is (16.612,16.142)  

 2. "_Is working more hours increase the average income?"  
 
 µh – Mean of average income for individuals working more than 2600 hours  
 µl- Mean of average income for individuals working less than 2600 hours  
 


H0 => Null Hypothesis        µh= µl  
Ha => Alternate Hypothesis   µh> µl 
```python

Highworkinghours=D1.loc[D1['hours'] >= 2600]
µh=Highworkinghours['earnings'].mean()
Lowworkinghours=D1.loc[D1['hours']<2600]# or
µl=Lowworkinghours['earnings'].mean()


#confidence interval calculation
statistic2=D1['earnings'].mean()
sigma2=D1['earnings'].std()
z2=(statistic2-0)/(sigma2)
SE2=sigma2/math.sqrt(D1['earnings'].count())

CI2=(statistic2+z2*SE),(statistic2-z2*SE2)

```
µh=30955.48
µl=13564.03 

Since µl<µh alternate hypothesis holds and data is statistically significant.  
Hence increase in working hours increases earnings.    
Confidence Interval is (14244.74,14040.09)

 



**Visualizations**
>>Divorced/separated stats on edu level less than 11*
![divorced/separated stats on edu level less than 11](https://github.com/TorinW/DataScience_UoM_19/blob/master/0-10_2-3.PNG)


>>divorced/separated stats on edu level greater than 10*
![divorced/separated stats on edu level greater than 11](https://github.com/TorinW/DataScience_UoM_19/blob/master/11-99_2-3.PNG)


*Graphs generated by using Power BI Tool


**Assumption**

By going through the dataset and the initial data analysis followings are the assumptions made.

- All respondands are in the similar salary scales and have similar working conditions
- All respondands had/have similar educational opportunities
- Having kids is independant from all the other factors
- Education level 98,99 are outliers.
- No of kids 98, 99 are outliers.
- Hours stand for no of working hours per year, not the no of hours spend with family.


**References**
- Haja, J. (2016). Create Bell Curve and Histogram with Power BI Desktop using DAX. [online] Mssqltips.com. Available at: https://www.mssqltips.com/sqlservertip/4076/create-bell-curve-and-histogram-with-power-bi-desktop-using-dax/ [Accessed 17 Feb. 2019].
- Panel Study of Income Dynamics web site: https://psidonline.isr.umich.edu/  [Accessed 16 Feb. 2019].  
-https://pythonhow.com/pandas-data-analysis-functions/

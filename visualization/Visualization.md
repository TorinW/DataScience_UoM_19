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


import numpy as np
import csv
import pandas as pd

import matplotlib.pyplot as plt
#%matplotlib inline

datafile = "PSID.csv"

D1=pd.read_csv(datafile,delimiter=',')
Atrr=D1.describe()
#D1.age.plot(kind='kde')
#D1.educatn.plot(kind='kde')
#D1.hours.plot(kind='kde')

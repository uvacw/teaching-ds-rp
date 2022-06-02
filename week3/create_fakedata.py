#!/usr/bin/env python3

import numpy as np
import pandas as pd

np.random.seed(1983)

n1,n2,n3,n4 = 98, 77, 102, 88
g1 = np.random.normal(loc=3.3, scale=.7, size=n1)
g2 = np.random.normal(loc=3.0, scale=.7, size=n2)
g3 = np.random.normal(loc=3.4, scale=.7, size=n3)
g4 = np.random.normal(loc=3.8, scale=.7, size=n4)
gender = np.random.choice(['male','female'], size=n1+n2+n3+n4)
age = np.random.randint(low=18, high=28, size=n1+n2+n3+n4)

df = pd.concat([pd.DataFrame({'dv':g1,'group':1}), 
           pd.DataFrame({'dv':g2,'group':2}),
           pd.DataFrame({'dv':g3,'group':3}),
           pd.DataFrame({'dv':g4,'group':4})])
df['gender'] = gender
df['age'] = age

df.to_csv('data.csv', index=False)

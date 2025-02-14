# -*- coding: utf-8 -*-
"""Credit_Card_Fraud_Detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DrMocD7mDhyxsteRlVpacgHmLxcKZ4pG
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk

df=pd.read_csv('/content/creditcard.csv')

dataset = pd.DataFrame(df)

df

df = df.sample(n=1000, random_state=42)

df.head()

"""Checking Null Values"""

df.isnull().sum()

sns.heatmap(df.isnull())

"""Exploaratory Data Analysis"""

x = df['V5']
y = df['Amount']
plt.bar(x,y)
plt.xlabel('V5')
plt.ylabel('Amount')
plt.show()

x = df['V11']
y = df['Amount']
plt.stem(x,y)
plt.xlabel('V11')
plt.ylabel('Amount')
plt.show()

"""Train Test Split"""

from sklearn.model_selection import train_test_split

x = df.drop(['Amount'],axis=1)
y = df['Amount']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

"""Model Training Ang Testing- Linear Regression"""

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(x_train,y_train)

y_pred = regressor.predict(x_test)

pd.DataFrame({'Actual':y_test,'Predicted':y_pred})

y_pred

from sklearn.metrics import r2_score

accuracy = r2_score(y_test,y_pred)

accuracy

"""Decison Tree Regressor"""

from sklearn.tree import DecisionTreeRegressor

tree = DecisionTreeRegressor()

tree.fit(x_train,y_train)

y_pred = tree.predict(x_test)

y_pred

from sklearn.metrics import r2_score

accuracy = r2_score(y_test,y_pred)

accuracy

"""Random Forest Regressor"""

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

rand = RandomForestRegressor()

rand.fit(x_train,y_train)

y_pred = rand.predict(x_test)

y_pred

accuracy = r2_score(y_test,y_pred)

accuracy

"""Xg Boost"""

from xgboost import XGBRegressor

xgb = XGBRegressor()

xgb.fit(x_train,y_train)

y_pred = xgb.predict(x_test)

y_pred

accuracy = r2_score(y_test,y_pred)

accuracy

"""Gradient Boost"""

from sklearn.ensemble import GradientBoostingRegressor

gbr = GradientBoostingRegressor()

gbr.fit(x_train,y_train)

y_pred = gbr.predict(x_test)

accuracy = r2_score(y_test,y_pred)

accuracy

"""Classification Algorithms"""

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()

df = df.sample(n=100000, random_state=42,replace= True)

x= df.drop(['class'],axis=1)
y= df['class']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

lr.fit(x_train,y_train)

y_pred = lr.predict(x_test)

y_pred

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test,y_pred)

accuracy

df['class'].value_counts()


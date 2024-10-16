# -*- coding: utf-8 -*-
"""Stock Price Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WDoJKZ0ESmJwwV6FxgTGxxIk6H8yyAcx
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk

df=pd.read_csv('/content/all_stocks_5yr.csv')

dataset = pd.DataFrame(df)

df.head()

df = df.sample(n=10000, random_state=42)

df

df.drop('Name',axis = 1)

df.isnull().sum()

sns.heatmap(df.isnull())

"""Exploratory Data Analysis"""

x = df['low']
y = df['close']
plt.stem(x,y)
plt.xlabel('low')
plt.ylabel('close')
plt.show()

x = df['high']
y = df['close']
plt.bar(x,y)
plt.xlabel('high')
plt.ylabel('close')
plt.show()

x = df['volume']
y = df['close']
plt.scatter(x,y)
plt.xlabel('volume')
plt.ylabel('close')
plt.show()

x = df['open']
y = df['close']
plt.boxplot([x,y])
plt.xlabel('volume')
plt.ylabel('close')
plt.show()

"""Train-Test-Split"""

x=df[['open', 'high', 'low', 'volume']]
y=df['close']

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

x_train

"""Model Training and Testing-Linear Regression"""

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(x_train,y_train)

y_pred=regressor.predict(x_test)

y_pred

pd.DataFrame({'Actual':y_test,'Predicted':y_pred})

from sklearn.metrics import r2_score

accuracy = r2_score(y_test,y_pred)

accuracy

from sklearn.metrics import mean_squared_error,mean_absolute_error

mse = mean_squared_error(y_test,y_pred)

mse

mae=mean_absolute_error(y_test,y_pred)

mae

"""Random Forest Regression"""

from sklearn.ensemble import RandomForestRegressor

rp = RandomForestRegressor()

rp.fit(x_train,y_train)

y_pred = rp.predict(x_test)

y_pred

accuracy = r2_score(y_test,y_pred)

accuracy

mse = mean_squared_error(y_test,y_pred)

mse

"""To improve Overfitting-Cross Validation Score"""

from sklearn.pipeline import make_pipeline

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Create a pipeline with scaling and random forest
model = make_pipeline(StandardScaler(), RandomForestRegressor(n_estimators=100, random_state=42))

# Cross-validation to evaluate model performance
cv_scores = cross_val_score(model, x_train, y_train, cv=5)
print(f"Cross-Validation Scores: {cv_scores}")
print(f"Mean CV Score: {np.mean(cv_scores)}")

# Fit the model
model.fit(x_train, y_train)

# Predict on the test set
y_pred = model.predict(x_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"MSE: {mse}")
print(f"R-squared: {r2}")


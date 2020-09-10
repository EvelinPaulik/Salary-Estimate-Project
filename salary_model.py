# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 20:18:26 2020

@author: Visitor
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('salary_data_clean.csv')

# Choose relevent columns
df. columns
df_model = df[['AvgSalary','Rating', 'Size', 'Type of ownership', 'Industry', 'Sector', 'Revenue',
       'Hourly', 'Province', 'Age', 'Python', 'Spark', 'AWS', 'Excel', 'JobSimplified', 'Seniority', 'DescLength']]

# Get dummy data
df_dum = pd.get_dummies(df_model)

# Train test split 80/20
from sklearn.model_selection import train_test_split

X = df_dum.drop('AvgSalary', axis=1)
y = df_dum.AvgSalary.values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

import statsmodels.api as sm

X_sm = X = sm.add_constant(X)
model = sm.OLS(y,X_sm)
model.fit().summary()

# Create multiple linear regression
# Create Lasso regression
# Create random forest
# Tune models using GradsearchCV
# Test ensembles

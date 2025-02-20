# -*- coding: utf-8 -*-
"""Advertising _Logistic_ Regression _Model

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1t23eDFeGtw-TXlr8ZHwSUId7MxOiha1c

Logistic Regression Project -

In this project we will be working with a fake advertising data set, indicating whether or not a particular internet user clicked on an Advertisement on a company website. We will try to create a model that will predict whether or not they will click on an ad based off the features of that user.

This data set contains the following features:




* 'Daily Time Spent on Site': consumer time on site in minutes


* 'Age': cutomer age in years

* 'Area Income': Avg. Income of geographical area of consumer

* 'Daily Internet Usage': Avg. minutes a day consumer is on the internet

* 'Ad Topic Line': Headline of the advertisement

* 'City': City of consumer

* 'Male': Whether or not consumer was male

* 'Country': Country of consumer

* 'Timestamp': Time at which consumer clicked on Ad or closed window

* 'Clicked on Ad': 0 or 1 indicated clicking on Ad

## IMPORTING LIBRARIES
"""



#IMPORTING NECESSARY LiBRARIES
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# %matplotlib inline
#to generate train and test data
import seaborn as sns
from sklearn.model_selection import train_test_split
#library to perform logistic regression
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
#for performance test
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
#to remove warnings messagess
import warnings
warnings.filterwarnings('ignore')

"""READ THE DATA

"""



#reading the csv file
from google.colab import files
uploaded=files.upload()
df=pd.read_csv("advertising.csv")
print(df.head())
df.info()

"""DATA ANALYSIS


"""

sns.histplot(df['Age'])

"""Create a joint plot


"""

sns.jointplot(x='Age',y='Daily Internet Usage',data=df,color='red')
sns.jointplot(x='Male',y='Daily Time Spent on Site',data=df)
sns.jointplot(x='Age',y='Daily Time Spent on Site',data=df)
sns.jointplot(x='Age',y='Area Income',data=df,color='violet')

"""Create pairplot

"""

sns.pairplot(df,hue='Clicked on Ad',palette="coolwarm")

"""Split the data into Training and Testing Data

"""

x=df[['Daily Time Spent on Site','Age','Area Income','Daily Internet Usage','Male']]
y=df['Clicked on Ad']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

"""Standardise the data

"""

SC=StandardScaler()
x_train=SC.fit_transform(x_train)
x_test=SC.transform(x_test)

"""PERFORM LOGISTIC REGRESSION"""

model=LogisticRegression()
model.fit(x_train,y_train)
LogisticRegression()
print("Intercept: ",model.intercept_)
print("Coefficients: ",model.coef_)

"""Predict Values"""

y_predict=model.predict(x_test)
plt.scatter(y_test,y_predict)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.show()

"""Evaluating the Model

"""



#compute confusion matrix
print("confusion matrix: ",confusion_matrix(y_test,y_predict))
conf_matrix=confusion_matrix(y_test,y_predict)
sns.heatmap(conf_matrix,annot=True,fmt='d',cmap='Spectral',xticklabels=['Not Clicked','Clicked'],yticklabels=['Not Clicked','Clicked'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
#Evaluate the model
print("Accuracy: ",accuracy_score(y_test,y_predict))
print("Classification Report: ",classification_report(y_test,y_predict))
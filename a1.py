import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('StudentsPerformance.csv')

data.head(5)

data.isnull().sum()

data.describe()


labels = ['Gender','race/ethnicity','parental level of education','reading score','writing score']

for label in labels:

    print('Distribution of', label)
    sns.histplot(data[label])
    plt.show()

    labels = ['Gender','race/ethnicity','parental level of education','reading score','writing score']

    for label in labels:
        print('skewness of ', label)
        print(data[label].skew())
        plt.show()


sns.countplot(x='Gender', hue='parental level of education', data=data)
plt.show()
sns.countplot(x='race/ethnicity', hue='parental level of education', data=data)
plt.show()
sns.displot(data['race/ethnicity'],kde=False, bins=40)
plt.show()
sns.countplot(data['Gender'])
plt.show()

sns.countplot(x='parental level of education',hue='reading score', data=data, palette="mako")
plt.show()

sns.countplot(x='parental level of education',hue='writing score', data=data, palette="mako")
plt.show()

sns.displot(data['Fare'])
plt.show()

sns.boxplot(x='race/ethnicity',y='Gender', data=data, palette="winter")
plt.show()

sns.heatmap(data.corr())
plt.show()
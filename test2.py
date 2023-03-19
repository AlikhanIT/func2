import pandas as pd
import numpy as np

data = pd.read_csv("dataset.csv")

print(data)

columns_target = ["Survived"]
columns_train = ["Pclass", "Sex", "Age", "Fare"]

X = data[columns_train]
Y = data[columns_target]

X["Sex"].isnull().sum()
X["Pclass"].isnull().sum()
X["Age"].isnull().sum()
X["Fare"].isnull().sum()

X["Age"] = X["Age"].fillna(X["Age"].median)

X["Age"].isnull().sum()

d = {
    "male": 0,
    "female": 1,
}

X["Sex"] = X["Sex"].apply(lambda x: d[x])

print(X["Sex"])

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=42)

from sklearn import svm

premodel = svm.LinearSVC()

premodel.fit(X_train, Y_train)

premodel.predict(X_test[0:10])
print("test")
print("test")
print("test")
print("test")
print("test")
print("test")
print("test")
print("test")
print("testd")
print(premodel.score(X_test, Y_test))

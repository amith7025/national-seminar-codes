# -*- coding: utf-8 -*-
"""Iris_petal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UkRCaX4_0Ocq5bm3TIUuibwtN3m0Au-I

## Our problem is we want to find species of flower based on sepal_length,sepal_width,petal_length,petal_width. We are using a simple Machine Learning Here
"""

from google.colab import drive
drive.mount('drive')

"""# Import the Modules"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

"""# Load the file using **Pandas**"""

df = pd.read_csv('/content/drive/MyDrive/IRIS.csv')
df.head()

"""Checking Values in Species

Here Species is the value we want to predict  all others are input

"""

df.species.unique()

inputs = df.drop(['species'],axis=1)
inputs.head()

"""## PreProcessing"""

output = df['species']
output.head()

label_encoder = LabelEncoder()
encoded_output = label_encoder.fit_transform(output).reshape(len(output),1)
print(f"encoded output: {encoded_output}")

"""Converting inputs and output to numpy array"""

X,y = np.array(inputs),np.array(encoded_output)
# print(X)
# print(y)

"""## Splitting dataset into trainset and testset"""

Xtrain,Xtest,ytrain,ytest = train_test_split(X,y,test_size=0.2)

"""# Initializing the model"""

model = DecisionTreeClassifier()

"""# Training the model"""

model.fit(Xtrain,ytrain)

"""# Predicting output with test dataset"""

y_pred = model.predict(Xtest)

"""Lets evaluate the model

"""

report = classification_report(ytest,y_pred)
print(report)

"""map the encoded value back to original output

"""

label_mapping = dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_)))
print(label_mapping)
reverse_mapping = {v:k for k,v in label_mapping.items()}
print(reverse_mapping)

def predictions(sepal_length,sepal_width,petal_length,petal_width):
    input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict(input_data)
    return reverse_mapping[int(prediction)]

predictions(5.1,3.5,1.4,0.2)


#importing all the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix, roc_curve, auc
from sklearn import svm, neighbors
from sklearn.ensemble import VotingClassifier
import pickle

#Load Dataset
df_train=pd.read_csv('train.csv')

#removing null values
df_train.isnull().sum()

df_train=df_train.fillna(" ")
df_train.isnull().sum()

#removing unwanted columns
df_train.drop(columns = 'id',axis=1,inplace=True)

#merging columns
df_train['news']=df_train['author']+':'+df_train['title']


X = df_train['news'].values
Y = df_train['label'].values

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()

vectorizer.fit(X)

X=vectorizer.transform(X)

#splitting the data to train and test
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2, random_state=42)

# Create hybrid model (SVM and KNN)
svm_model = SVC(kernel='linear', C=1.0, probability=True)
knn_model = neighbors.KNeighborsClassifier(n_neighbors=5)
hybrid_model = VotingClassifier(estimators=[('svm', svm_model), ('knn', knn_model)], voting='hard')


hybrid_model.fit(X_train, Y_train)



pickle.dump(hybrid_model, open("model.pkl", "wb"))



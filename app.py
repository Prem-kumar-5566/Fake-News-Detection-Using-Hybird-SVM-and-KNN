import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix, roc_curve, auc
from sklearn import svm, neighbors
from sklearn.ensemble import VotingClassifier
from sklearn.feature_extraction.text import CountVectorizer
import pickle 

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

data = pd.read_csv('train.csv')
data.isnull().sum()
data=data.fillna(" ")
data.isnull().sum()
data.drop(columns = 'id',axis=1,inplace=True)
data['news']=data['author']+':'+data['title']

X = data['news'].values
Y = data['label'].values

vectorizer = CountVectorizer()

vectorizer.fit(X)
X=vectorizer.transform(X)
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)

def fake_news_det(text):
    
    input_data = [text]
    vectorized_input_data =vectorizer.transform(input_data)
    prediction = model.predict(vectorized_input_data)
    return prediction


@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        pred = fake_news_det(message)
        print(pred)
        return render_template('index.html', prediction=pred)
    else:
        return render_template('index.html', prediction="Something went wrong")

if __name__ == "__main__":
    flask_app.run(debug=True) 
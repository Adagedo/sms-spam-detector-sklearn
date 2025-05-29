from sklearn.naive_bayes import *
from sklearn.dummy import *
from sklearn.ensemble import *
from sklearn.neighbors import *
from sklearn.tree import *
from sklearn.feature_extraction.text import (
    CountVectorizer, 
    TfidfVectorizer, 
    HashingVectorizer
)
from sklearn.calibration import *
from sklearn.linear_model import *
from sklearn.multiclass import *
from sklearn.svm import *
import pandas as pd
import csv



data = pd.read_csv("./model/data/spam.csv", encoding='latin-1')

training_data_length = int(0.8 * len(data))

learning_data = data[:training_data_length]
test_data = data[len(learning_data):]


def model(classifier, vectorizer, learning_data, test_data):

    vectorizer.fit(learning_data["v2"])

    transformed_learning_data = vectorizer.transform(learning_data['v2'])
    transformed_testing_data = vectorizer.transform(test_data["v2"])

    learning_data_labels = learning_data["v1"]
    test_data_labels = test_data["v1"]

    classifier.fit(transformed_learning_data, learning_data_labels)
    scores = classifier.score(transformed_testing_data, test_data_labels)
    print(f"{scores * 100:.4f}%") 
    
    # making predictions 




classifier = OneVsRestClassifier(SVC(kernel='linear'))
vectorizer = TfidfVectorizer()
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
import os
from sklearn.calibration import *
from sklearn.linear_model import * 
from sklearn.multiclass import *
from sklearn.svm import *
import pandas as pd


def model_perform(
    classifiers:list, 
    vectorizers:list, 
    train_data,
    test_data
)->None:
    for classifier in classifiers:
        for vectorizer in vectorizers:
            string = ''
            string += classifier.__class__.__name__ + 'with' + vectorizer.__class__.__name__
            
            
            vectorizer.fit(train_data["v2"])
            
            transformed_train_data_v2 = vectorizer.transform(train_data["v2"])
            transformed_test_data_v2 = vectorizer.transform(test_data["v2"])

            train_labels = train_data["v1"]
            test_labels = test_data["v1"]

            classifier.fit(transformed_train_data_v2, train_labels)

            score = classifier.score(transformed_test_data_v2, test_labels)

            string += ". has a score of: " + str(score)
            print(string)



data = pd.read_csv("./model/data/spam.csv", encoding='latin-1')
print(data[:10]["v1"])
print(data[:10]["v2"])
training_data_length = int(0.8 * len(data))

learning_data = data[:training_data_length]
test_data = data[len(learning_data):]


# model_perform(
#     classifiers=[
#         DecisionTreeClassifier(),
#         CalibratedClassifierCV(),
#         DummyClassifier(),
#         PassiveAggressiveClassifier(),
#         RidgeClassifier(),
#         RidgeClassifierCV(),
#         OneVsRestClassifier(SVC(kernel='linear')),
#         OneVsRestClassifier(LogisticRegression()),
#         KNeighborsClassifier(),
#         SGDClassifier(),
#         BernoulliNB(), 
#         RandomForestClassifier(n_estimators=100, n_jobs=-1),
#         AdaBoostClassifier(), 
#         BaggingClassifier(),
#         ExtraTreesClassifier(),
#         GradientBoostingClassifier(),
#     ],
#     vectorizers=[
#         CountVectorizer(),
#         TfidfVectorizer(),
#         HashingVectorizer()
#     ]
#     , train_data=learning_data, 
#     test_data=test_data
# )
   
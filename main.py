from sklearn.naive_bayes import *
from sklearn.dummy import *
from sklearn.ensemble import *
from sklearn.neighbors import *
from sklearn.tree import *
from sklearn.feature_extraction.text import (
    CountVectorizer, 
    TfidfTransformer, 
    HashingVectorizer
)

from sklearn.calibration import *
from sklearn.linear_model import * 
from sklearn.multiclass import *
from sklearn.svm import *
import pandas


def model_perform(
    classifiers, 
    vectorizers, 
    train_data,
    test_data
):
    for classifier in classifiers:
        for vectorizer in vectorizers:
            string = ''
            string += classifier.__class__.__name__ + 'with' + vectorizer.__class__.__name__
            
            #training the model with sklearn
            
            vectorize_text = vectorizer.fit_transfrom(train_data.v2)
            classifier.fit(vectorize_text, train_data.v1)
            
            # 

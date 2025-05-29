# 📂 SMS Spam Detection
This project classifies SMS messages as spam or ham (not spam). 
It compares multiple classifiers and vectorizers to determine the best performance.

## Features
### ✅ Uses:

- DecisionTreeClassifier

- CalibratedClassifierCV

- DummyClassifier

- PassiveAggressiveClassifier

- RidgeClassifier


### ✅ Vectorization:

- CountVectorizer

- TfidfVectorizer

- HashingVectorizer

### ✅ Dataset:
- A CSV file containing SMS messages labeled as either "spam" or "ham".



## 📝 Notes
The CSV file should have at least two columns:

- v1: label (ham/spam)

- v2: message text

Results are printed to the console or just take a look at the csv file.
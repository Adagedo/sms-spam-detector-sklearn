# 📂 SMS Spam Detection
This project classifies SMS messages as spam or ham (not spam). 
It compares multiple classifiers and vectorizers to determine the best performance.

## Features
### Classifiers:

- DecisionTreeClassifier

- CalibratedClassifierCV

- DummyClassifier

- PassiveAggressiveClassifier

- RidgeClassifier


###  Vectorizers:

- CountVectorizer

- TfidfVectorizer

- HashingVectorizer

### FastApi
- fastapi is a python pacakge for building scalable backend apis
- for more info about fastapi you can my github repo on fastapi implementations

### Dataset:
- A CSV file containing SMS messages labeled as either "spam" or "ham".

## Usage
- clone this repo with `git clone https://github.com/Adagedo/sms-spam-detector-sklearn.git`
- install dependencies with `pip install requirement.txt`
- After running the model, you should see an output like this. ![the score](models_score.png)
- To run the application, `uvicorn main:app --reload`
- what you will see `INFO: Uvicorn running on http://localhost:8000 (Press CTRL+C to quit) \n INFO:Started reloader process [8976] using WatchFiles`
- api test ![input](test_in_one.png)
- api test ![output](test_in_two.png)
- api test ![sapm](text_spam_in.png)
- api test ![sapm res](text_spam_out.png)


## 📝 Notes
The CSV file should have at least two columns:

- v1: label (ham/spam)

- v2: message text

Results are printed to the console or just take a look at the csv file.
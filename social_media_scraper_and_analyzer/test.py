#
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer as vec
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
##Text preprocessing
import spacy
import preprocess_kgptalkie as ps
import re
import lxml
import spacy
import preprocess_kgptalkie as ps
import re
import lxml
def main():
    df=pd.read_csv(r'jigsaw-final.csv')
    def get_clean(x):
        x = str(x).lower().replace('\\', '').replace('_', ' ')
        x = ps.cont_exp(x)
        x = ps.remove_emails(x)
        x = ps.remove_urls(x)
        #x = ps.remove_html_tags(x)
        x = ps.remove_accented_chars(x)
        x = ps.remove_special_chars(x)
        x = re.sub("(.)\\1{2,}", "\\1", x)
        return x
    df["comment_text"]=df["comment_text"].apply(lambda x: get_clean(x))
    tfidf=vec(max_features=500000)
    X=df['comment_text']
    y=df['TOXIC']
    X=tfidf.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=0)
    clf=LinearSVC()
    clf.fit(X_train,y_train)
    y_pred=clf.predict(X_test)
    classification_report(y_test, y_pred)
    x='nigga' #last text of whatsapp sent on group
    vector=tfidf.transform([x]) 
    score=clf.predict(vector)
    score=score[-1]  

    return score

print(main())
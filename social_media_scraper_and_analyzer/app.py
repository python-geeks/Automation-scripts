from flask import Flask, render_template, redirect
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
app = Flask(__name__)
data=[]
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/watest')
def my_link():
  driver= webdriver.Chrome(executable_path="chromedriver.exe")
  driver.get("https://web.whatsapp.com/")
  bot="Sent by bot: Not Okay!!"
  name='Bot'
  time.sleep(20)
  search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
  search_box.send_keys(name)
  search_box.send_keys(Keys.ENTER)
  for i in range(1,43):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  time.sleep(20)
  last_msg=driver.find_elements_by_class_name('cvjcv _1Ilru')
  msg = driver.find_elements_by_class_name('_1Gy50')
  msg = msg[-1]
  msg_1 = msg.text
  msg_1 = msg_1.split('\n')
  #print(msg_1)
  msg_2=msg_1[-1]
  data.append(msg_2)
  
  return redirect('/codetest')

@app.route('/codetest')
def test():
    
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
    x=data[0] #last text of whatsapp sent on group
    vector=tfidf.transform([x]) 
    score=clf.predict(vector) 
    score=score[-1]
    if score==1:
             
        return redirect('/sendmsg')
    else:
        result= "This message is fine."     
        

    
    return render_template('result.html', result=result)

@app.route('/sendmsg')
def send_msg():
    driver= webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("https://web.whatsapp.com/")
    name='Bot'
    time.sleep(20)
    search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    search_box.send_keys(name)
    search_box.send_keys(Keys.ENTER)
    for i in range(1,43):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    text_box=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]')
    text='From Bot: the msg "{}" sent is not appropritate, please delete it'.format(data[0])
    text_box.send_keys(text+ Keys.ENTER)
    driver.quit()
    data.clear()
    print('Done!')
    result='Check your Whatsapp group, Thanks!!'
    return render_template('result.html', result=result)
if __name__ == '__main__':
  app.run(debug=True)
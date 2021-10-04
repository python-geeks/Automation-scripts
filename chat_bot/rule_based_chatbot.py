#!/usr/bin/env python
# coding: utf-8

#  pip install flake8

# # Rule based chatbot

# In[3]:


conda install flake8


# In[1]:


import nltk
from nltk.chat.util import Chat,reflections


# In[2]:


print(Chat)


# In[3]:


reflections


# In[4]:


set_pairs=[
    [
        r"my name is (.*)",
        ["Hello %l, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
    [
        r"(.*) your name ?",
        ["My name is beedo, but you can just call me robot and I'm a chatbot .",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*)created(.*)",
        ["XYZ created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['New Delhi, India',]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Cricket",]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["Virat Kohli"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['That is nice to hear']
    ],
]


# In[5]:


def chatbot():
    print("Hi I am a rule-based chatbot ! what can i help you with?")
chatbot()


# In[6]:


chat = Chat(set_pairs,reflections)
print(chat)


# In[7]:


chat.converse()
if __name__ == "__main__":
    chatbot()


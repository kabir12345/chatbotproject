# coding: utf-8

# In[1]:


import nltk
from random import randint
import numpy as np
import random
import string
import pickle
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chatbot', methods=['POST'])


def return_name():
    name = request.form['name']
    return name


def return_age():
    age = request.form['age']
    return age


def return_res1():
    res1 = request.form['res1']
    return res1

def return_res2():
    res2 = request.form['res2']
    return res2

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)


# In[2]:


# this function gives domain i.e 7 sub categories including gad,emotional,physical,social,etc
def check_general_classification(X):
    with open('general_classification.pkl', 'rb') as file:
        general_classification = pickle.load(file)
    return general_classification.predict(pd.Series(X))


# fuctions below this line will give sub domains on the basis of class predicted by check_general_classification
def gad(X):
    with open('GAD.pkl', 'rb') as file:
        gad = pickle.load(file)
        return gad.predict(pd.Series(X))


def emotional_change(X):
    with open('emotional_change.pkl', 'rb') as file:
        emotional_change = pickle.load(file)
    return emotional_change.predict(pd.Series(X))


def panik_attack(X):
    with open('panic attack.pkl', 'rb') as file:
        panik_attack = pickle.load(file)
    return panik_attack.predict(pd.Series(X))


def poor_performance(X):
    with open('poor_performance.pkl', 'rb') as file:
        poor_performance = pickle.load(file)
    return poor_performance.predict(pd.Series(X))


def sleep_disturbances(X):
    with open('sleep_disturbances.pkl', 'rb') as file:
        sleep_disturbances = pickle.load(file)
    return sleep_disturbances.predict(pd.Series(X))


def social_change(X):
    with open('social_change.pkl', 'rb') as file:
        social_change = pickle.load(file)
    return social_change.predict(pd.Series(X))


def physical_change(X):
    with open('physical_change.pkl', 'rb') as file:
        physical_change = pickle.load(file)
    return physical_change.predict(pd.Series(X))


def happy_side(X):
    with open('happy_sad.pkl', 'rb') as file:
        happy_sad = pickle.load(file)
    return happy_sad.predict(pd.Series(X))


# In[ ]:


flag = True  # see use of flag in while loop
d = 'DASM'  # bot's name
number_of_incoreect_attempts = 0
# GAD_types=["Future events","Past behaviors and incidents","Social acceptance","Family matters","Personal abilities","Perceived personal shortcomings","School performance","Perceived personal shortcomings",]
# exp_list_responses=["Please Elaborate more.", "Please Explain The Situation","I would like to know more"]

name_choice = return_name()

while (flag == True):
    res1 = return_res1()
    con_yn = happy_sad(res1)

    con_yn = "sad"  # using happy_sad fuunction to predict weather user is happy or not con_yn= condition sad or happyy
    #if con_yn == "happy":
        #print(d + ": I am glad that you are happy. I hope whenever you face any difficulties you will come back to me.")
        #break
    if con_yn == "sad":
        res_2 = return_res2()
        pred_class = check_general_classification(res_2)
        if pred_class == "Generalized Anxiety Disorder":
            final_content = res_2
            while True:  # to do: add if statement to check number of characters >30 in if res4==n
                res_4 = input(d + ': do you want to elaborate ' + name)
                if number_of_incoreect_attempts == 4:
                    print('sorry i was not able to understand, please try again')
                    break
                if res_4.lower()[0] == 'y':  # finished
                    res_5 = input(d + ': please elaborate ' + name)
                    final_content = final_content + ' ' + res_5
                if res_4.lower()[0] == 'n':  # add here
                    if len(final_content) < 30:
                        while len(final_content) < 30:
                            res_6 = input('content entered is not sufficient,please add more')
                            final_content = final_content + ' ' + res_6
                    elif len(final_content) > 30:
                        if check_general_classification(final_content) != pred_class:
                            c = c + 1
                            pred_class = check_general_classification(final_content)
                            print(check_general_classification(final_content))  # remove this in final code
                            print('not same')  # remove this in final code
                            break
                    else:
                        sub_domain = gad(final_content)
                        if sub_domain == 'Future events':
                            print('ooh lala')
                            break
                        if sub_domain == 'Future events':
                            print('ooh lala')
                            break
                        if sub_domain == 'Future events':
                            print('ooh lala')
                            break
                        if sub_domain == 'Future events':
                            print('ooh lala')
                            break

                    '''elif input('are you satisfied with my answer?').lower()[0]=='y':
                        flag=False
                        break'''
        if pred_class == "Generalized Anxiety Disorder":
            c = 0
            final_content = res_2
            while True:
                res_4 = input(d + ': do you want to elaborate ' + name)
                if res_4 == 'y':
                    res_5 = input(d + ': please elaborate ' + name)
                    final_content = final_content + ' ' + res_5
                if res_4.lower()[0] == 'n':
                    if check_general_classification(final_content) != pred_class:
                        c = c + 1
                        print(check_general_classification(final_content))
                        print('not same')
                        break
                    # else:
                    #   print(final_content)
                    #  break
                if c == 4:
                    print('sorry i was not able to understand, please try again')
                    break
                    '''elif input('are you satisfied with my answer?').lower()[0]=='y':
                        flag=False
                        break'''
        if pred_class == "Generalized Anxiety Disorder":
            c = 0
            final_content = res_2
            while True:
                res_4 = input(d + ': do you want to elaborate ' + name)
                if res_4 == 'y':
                    res_5 = input(d + ': please elaborate ' + name)
                    final_content = final_content + ' ' + res_5
                if res_4.lower()[0] == 'n':
                    if check_general_classification(final_content) != pred_class:
                        c = c + 1
                        print(check_general_classification(final_content))
                        print('not same')
                        break
                    # else:
                    #   print(final_content)
                    #  break
                if c == 4:
                    print('sorry i was not able to understand, please try again')
                    break
                    '''elif input('are you satisfied with my answer?').lower()[0]=='y':
                        flag=False
                        break'''
        if pred_class == "Generalized Anxiety Disorder":
            c = 0
            final_content = res_2
            while True:
                res_4 = input(d + ': do you want to elaborate ' + name)
                if res_4 == 'y':
                    res_5 = input(d + ': please elaborate ' + name)
                    final_content = final_content + ' ' + res_5
                if res_4.lower()[0] == 'n':
                    if check_general_classification(final_content) != pred_class:
                        c = c + 1
                        print(check_general_classification(final_content))
                        print('not same')
                        break
                    # else:
                    #   print(final_content)
                    #  break
                if c == 4:
                    print('sorry i was not able to understand, please try again')
                    break
                    '''elif input('are you satisfied with my answer?').lower()[0]=='y':
                        flag=False
                        break'''
        if pred_class == "Generalized Anxiety Disorder":
            c = 0
            final_content = res_2
            while True:
                res_4 = input(d + ': do you want to elaborate ' + name)
                if res_4 == 'y':
                    res_5 = input(d + ': please elaborate ' + name)
                    final_content = final_content + ' ' + res_5
                if res_4.lower()[0] == 'n':
                    if check_general_classification(final_content) != pred_class:
                        c = c + 1
                        print(check_general_classification(final_content))
                        print('not same')
                        break
                    # else:
                    #   print(final_content)
                    #  break
                if c == 4:
                    print('sorry i was not able to understand, please try again')
                    break
                    '''elif input('are you satisfied with my answer?').lower()[0]=='y':
                        flag=False
                        break'''
        if pred_class == "Generalized Anxiety Disorder":
            c = 0
            final_content = res_2
            while True:
                res_4 = input(d + ': do you want to elaborate ' + name)
                if res_4 == 'y':
                    res_5 = input(d + ': please elaborate ' + name)
                    final_content = final_content + ' ' + res_5
                if res_4.lower()[0] == 'n':
                    if check_general_classification(final_content) != pred_class:
                        c = c + 1
                        print(check_general_classification(final_content))
                        print('not same')
                        break
                    # else:
                    #   print(final_content)
                    #  break
                if c == 4:
                    print('sorry i was not able to understand, please try again')
                    break
                    '''elif input('are you satisfied with my answer?').lower()[0]=='y':
                        flag=False
                        break'''

        if pred_class == "Generalized Anxiety Disorder":
            c = 0
            final_content = res_2
            while True:
                res_4 = input(d + ': do you want to elaborate ' + name)
                if res_4 == 'y':
                    res_5 = input(d + ': please elaborate ' + name)
                    final_content = final_content + ' ' + res_5
                if res_4.lower()[0] == 'n':
                    if check_general_classification(final_content) != pred_class:
                        c = c + 1
                        print(check_general_classification(final_content))
                        print('not same')
                        break
                    # else:
                    #   print(final_content)
                    #  break
                if c == 4:
                    print('sorry i was not able to understand, please try again')
                    break
                    '''elif input('are you satisfied with my answer?').lower()[0]=='y':
                        flag=False
                        break'''

# In[49]:


import keras

# In[50]:


get_ipython().run_line_magic('pwd', '')


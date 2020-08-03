import json
import time as t
import sys
from os import listdir
from random import randint

def countdown(sec):
    '''This is a countdown timer'''
    
    print(f'Please Wait while your question loads....')
    t.sleep(2)
    while sec:
        display_form = f'{sec:02d}'
        print(display_form, end = '\r')
        t.sleep(1)
        sec -= 1
    print('GOOD LUCK!')
    t.sleep(1)

def question(q):
    '''This code takes the question and display it according to the selection made'''
    
    score = 0
    num_of_quest = len(q)
    tot_num = 20
    for i in range(tot_num):
        num = randint(0, num_of_quest-1)
        questions = q[num]['questions']
        options = q[num]['options']
        answer = q[num]['answer']
        print(f'\nQ{i+1} {questions}')
        right_answer = None
        for option in options:
            print(option)
            if option[3:] == answer[0:]:
                right_answer = option
        ans = input('answer: ').upper()
        if ans == right_answer[0] or ans == answer:
            score +=1
        num_of_quest -= 1
        if ans.lower() == 'n':
            break
        del q[num]
    print(f'\nYou score {score} out of {tot_num}')

def instruction(title):
    print(f"""
WELCOME TO THIS SECTION
-*-*-*-*-*-*-*-*-*-*-*
>> This section tests your knowledge of {title}
>> There are 20 questions available for you to answer
>> Type 'n' in answer prompt to end the test""")
    
    
def computer():
    '''This reads the json computer file and dispalys it with the question() function'''
    
    instruction('computer')
    t.sleep(5)
    with open('questionbank/computer_questions.json', 'r+') as f:
        q = json.load(f)
        q = q['questions']
    countdown(3)
    question(q)
    
def science_nature():
    '''This reads the science and nature question from its json file and display'''
    
    instruction("science and nature")
    t.sleep(5)
    with open('questionbank/science.json', 'r+') as f:
        q = json.load(f)
        q = q['questions']
    countdown(3)
    question(q)

def history():
    '''This reads the history question and display it when selected'''
    
    instruction('History')
    t.sleep(5)
    with open('questionbank/History_que.json', 'r+') as f:
        q = json.load(f)
        q = q['questions']
    countdown(3)
    question(q)
        

def total_file():
    '''It calculates the total number of questions currently available'''
    
    total_file = len(listdir('questionbank'))
    return total_file

def category():
    '''Displays the categories of questions currently available'''
    
    total = total_file()
    print(f'\nThere are currently {total} sections you can test yourself')
    print('Select a Section Below\n')
    print('1. SCIENCE AND NATURE')
    print('2. SCIENCE: COMPUTER')
    print('3. HISTORY')
    print('4. EXIT')

def choose_category():
    '''Responsible for selecting the aspect user chooses to test him/her self'''
    
    category()
    categ = input('Enter Category: ').upper()
    if categ == '1' or categ == 'SCIENCE AND NATURE':
        science_nature()
    elif categ == '2' or categ == 'SCIENCE: COMPUTER' or categ == 'COMPUTER':
        computer()
    elif categ == '3' or categ == 'HISTORY':
        history()
    elif categ == '4' or categ == 'EXIT':
        print("Thanks, we'll love to see you some other time")
        sys.exit()
    else:
        print('Error! Invalid Command')

    
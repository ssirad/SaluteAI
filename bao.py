import re
import random
import nltk
import patterns_bao_salute

tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')

'''
we have to create a chatbot that answers those three questions in general:
- SITUATION (what happend?)
- TOUGHTS (what where they thinking?)
- EMOTIONS (what where thery feeling in the moment?)
'''

def respond(input_text, name):
    for pattern, responses in patterns_bao_salute.patterns_symptoms.items():
        match = re.search(pattern, input_text.lower())
        if match:
            response = random.choice(responses)
            print(response)
            return input_text + '\n' + '*' + response + '*' + '\n' + patterns_responses(name)
            #saving the answer
    else:
        return str(input_text)


def patterns_responses(name):
        u_input = input(name + ' > ')
        return u_input

def symptoms(name):
    print("What is the symptom you want to talk about today?")
    u_input = input(name + ' > ')
    return respond(u_input, name)

def situation(name):
    print("In what situation does the symptom took place?") #change
    u_input1 = input(name + ' > ')
    print("Did it happened multiple times today? (yes or no) ")
    u_input2 = input(name + ' > ')
    if u_input2 == 'yes':
        response = u_input1 + '\n' + '- It happened multiple times during the day -'
    else:
        response = u_input1
    return response

def thought(name):
    print('How was your day? :)')
    u_input1 = input(name + ' > ')
    print('Anything that if worth remembering from today or from the past that you want to share?')
    u_input2 = input(name + ' > ')
    return '*How was your day?* ' + u_input1 + '\n' + '*Anything that if worth remembering from today or from the past that you want to share?* ' + u_input2

def emotions(name):
    print("Can you describe you emotional state today?") #please change this
    u_input = input(name + ' > ')
    return '*Can you describe you emotional state today?* ' + u_input

def bao():

    print(r'''
     (@)-----(@)      BBBBBBB      AAAAAA       OOOO        @@@   @@@
     / (_) (_) \      BB    BB    AA    AA    OO    OO     @@@@@ @@@@@
    |     O     |     BBBBBBB     AAAAAAAA    OO    OO      @@@@@@@@@
     \  \_|_/  /      BB    BB    AA    AA    OO    OO        @@@@@
      '-------'       BBBBBBB     AA    AA      OOOO            @
    ''')
    name = input("Hii, my name is BAO. \n"
                 "I'm going to be your personal assistant in the tracker application :), \n"
                 "let's fill together all that I need to track your symptoms... \n"
                 "I'm going to ask you some simple questions.\n"
                 "What's your name? ")

    log = input('Did you have any symptoms today? (yes or no) ')
    if log == 'yes':
        n = 0
        while True:
            n += 1
            q1 = symptoms(name)
            #BODY + RATING
            print('- BODY PARTS -')
            print('- PAIN RATING -')
            q2 = situation(name)
            q = input('Do you want to add another symptom? (yes or no) ')
            if q == 'no' or q != 'yes':
                break
        q3 = thought(name)
        q4 = emotions(name)
        final_q = input('Almost finished :) \nIf you want to add somthing: a thought or something that made you smile today you, can write it here below: \n')
        for _ in range(n):
            recap(q1, q2, q3, q4)
        print('* PERSONAL SPACE *', '\n', final_q)
    else:
        q3 = thought(name)
        q4 = emotions(name)
        #recap if not log symptom
        print('DA FARE ANCORA IL CAZZO DI RECAP')
        final_q = input('Almost finished :) \nIf you want to add somthing: a thought or something that made you smile today you, can write it here below: \n')
        print('* PERSONAL SPACE *', '\n', final_q)


def recap(symptoms, situations, thought, emotions):
    #i need the recap so i can know what it's saved and what not. Those are the saved data that we will put in the tracker

    print('* RECAP * \n', '* SYMPTOMS * --> ', symptoms, '\n', '\n', '* SITUATIONS * --> ', situations, '\n', '\n', '* TOUGHTS * --> ', thought, '\n', '\n', '* FEELINGS * --> ', emotions, '\n')
bao()


'''
NOTES - things to change still
- patterns symptoms not finished
- make every response .lower()
- change the headache in patterns bc it's asking the position two times; for body too; neck
- more than one symptom does not work
- hae to do the recap in the case you don't want to log a symptom inside of it
'''

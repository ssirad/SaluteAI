import re
import random
import nltk
import patterns_elissa_salute

tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')

'''
we have to create a chatbot that answers those three questions in general:
- SITUATION (what happend?)
- TOUGHTS (what where they thinking?)
- EMOTIONS (what where thery feeling in the moment?)
'''

def respond(input_text, name, topic_n):
    response_topics = [patterns_elissa_salute.patterns_symptoms, patterns_elissa_salute.patterns_situations, patterns_elissa_salute.patterns_emotions] #valori da aggiungere in modo da capire dal numero quale pattern usare
    for pattern, responses in response_topics[topic_n].items():
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
    return respond(u_input, name, topic_n=0)

def situation(name):
    print("In what situation does the symptom took place?") #change
    u_input1 = input(name + ' > ')
    print("Did it happened multiple times today? (yes or no) ")
    u_input2 = input(name + ' > ')
    if u_input2 == 'no':
        return u_input1
    elif u_input2 == 'yes':
        print('what do you think trigged the fisrt time?') #i don't know why this can be useful
        u_input3 = input(name + ' > ')
        return u_input1 + '\n' + '*It happened multiple times during the day*' +'\n' + '*what do you think trigged the fisrt time?* ' + u_input3
    #return respond(u_input, name, topic_n=1),

def thought(name):
    print("Has something been bothering you lately or do yoou feel like any situations or memory had triggered you/it/the symptom? (yes or no)")
    u_input = input(name + ' > ')
    if u_input == 'yes':
        description = input('Could you describe it?\n')
        return respond(u_input, name, topic_n=1) + '\n' + "Description of the symptom: " + description
    elif u_input == 'no':
        print('what were you thinking in the moment of the symptom?')
        u_input1 = input(name + ' > ')
        return respond(u_input, name, topic_n=1) + '\n' + u_input1
    #predict situations?
    #return respond(u_input, name, topic_n=2)

def emotions(name):
    print("What emotions were you feeling?")
    u_input = input(name + ' > ')
    return respond(u_input, name, topic_n=2)

def elissa():
    print('''
                          EEEEEE  LL      IIII    SSSSSSS    SSSSSSS    AAAAAA                       
                          EE      LL       II    SS         SS         AA    AA                      
                          EEEEE   LL       II     SSSSS      SSSSS     AAAAAAAA                      
                          EE      LL       II          SS         SS   AA    AA                      
                          EEEEEE  LLLLLL  IIII   SSSSSSS    SSSSSSS    AA    AA                      
    ''')
    name = input("Hii, my name is Elissa. \n"
                 "I'm going to be your personal assistant in the tracker application :), \n"
                 "let's fill together all that I need to track your symptoms... \n"
                 "I'm going to ask you some simple questions.\n"
                 "What's your name? ")
    n = 0
    while True:
        n += 1
        q1 = symptoms(name)
        q2 = situation(name)
        q3 = thought(name)
        q4 = emotions(name)
        q = input('Do you want to add another symptom? (yes or no) ')
        if q == 'no'or q != 'yes':
            break
    final_q = input('Almost finished :) \nIf you want to add somthing: a thought or something that made you smile today you, can write it here below: \n')
    for _ in range(n):
        recap(q1, q2, q3, q4)
    print('*PERSONAL SPACE*', '\n', final_q)

def recap(symptoms, situations, thought, emotions):
    #i need the recap so i can know what it's saved and what not. Those are the saved data that we will put in the tracker

    print('*RECAP* \n'
          '*SYMPTOMS* --> ', symptoms, '\n',
          '*SITUATIONS* --> ', situations, '\n',
          '*TOUGHTS* --> ', thought, '\n',
          '*FEELINGS* --> ', emotions, '\n')
elissa()


'''
NOTES - things to change still
- what do you think trigged the fisrt time? ---> I don't think that we need this bc you are describing it right after
- still not saving everything in recap - question in thoughts() and situations()
- emotions not finished
- patterns not nearly finished
'''

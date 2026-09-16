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
            #salvare la risposta
    else:
        return str(input_text)

#questa parte dovrebbe essere inutile perchè non ci arriva mai,
#se non trova unn pattern chiede le prossime domande... soprattutto perchè non può salvarle
'''
else:
    q = input_text.split(' ')
    for word in q:
        if word in patterns[topic_n]:
            return 'Can you describe the {}'.format(word)
            #salvare la risposta
    print('thank you for sharing your feelings about this...') #da cambiare
'''


def patterns_responses(name):
        u_input = input(name + ' > ')
        return u_input

def symptoms(name):
    print("What is the symptom you want to talk about today?")
    u_input = input(name + ' > ')
    return respond(u_input, name, topic_n=0)

def situation(name):
    print("In what situation does the symptom took place?") #da cambiare
    u_input1 = input(name + ' > ')
    print("Did it happened multiple times today?")
    u_input2 = input(name + ' > ')
    if u_input2 == 'no':
        return u_input1
    elif u_input2 == 'yes':
        print('what do you think trigged the fisrt time?')
        u_input3 = input(name + ' > ')
        return u_input1 + '\n' + u_input3
    #non serve ma se serve è per predirre situazioni
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
    #non serve ma se serve è per predirre situazioni
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
    name = input("Hii, my name is Elissa."
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
        q = input('Do you want to add another symptom? (yes or no)')
        if q == 'no':
            break
        elif q != 'yes:':
            print('You did not answer, it is an yes or no question')
    final_q = input('Almost finished :) \nIf you want to add somthing: a thought or something that made you smile today you, can write it here below: \n')
    for _ in range(n):
        recap(q1, q2, q3, q4)
    print('*PERSONAL SPACE*', '\n', final_q)

def recap(symptoms, situations, thought, emotions):
    #qua mi serve che riprendo tutte le cose ma prima devo salvarle e poi fare un recap di tutto così posso metterla a postp e salvarla da qualche parte con un return

    print('RECAP* \n'
          '*SYMPTOMS*', '\n', symptoms, '\n',
          '*SITUATIONS*', '\n', situations, '\n',
          '*TOUGHTS*', '\n', thought, '\n',
          '*FEELINGS*', '\n', emotions, '\n')
elissa()

patterns_symptoms = {
    r'.*(headache|head hurts|head hurting|head pain|tension of the head|migraine).*': [
        'Where exactly you feel the pain?'
        #others
    ],
    r'.*(stomach pain|abdominal pain|belly pain|abdominal discomfort|stomach ache).*': [
        'risposta del mal di stomaco' #da cambiare
    ],
    r'.*(neck pain|neck tension|cervical pain|neck ache).*': [
        'Can you describe better the position in the neck you feel pain? (like front, back, right, left)' #da cambiare
        #others
    ],
    r'.*(shoulder pain|shoulder tension|tight shoulders).*': [
        'How bad if the shoulder pain?' #da cambiare
        #others
    ],
    r'.*(chest pain|heart pain|chest pressure|chest tightness|heaviness in the chest).*': [
        'How would you describe the feeling in your chest (sharp, crushing, dull ache, pressure, burning)?' #da cambiare
        #others
    ],
    r'.*(muscle pain|muscle ache|muscle tension|muscular discomnfort|myalgia|body aches).*': [
        'In what body part do you feel the muscle discomfort?' #da cambiare
        #others
    ],
    r'.*(joint pain|stiffness|soreness|joint discomnfort|joint ache).*': [
        'Do you have walking problems caused by the joint discomfort?' #da cambiare
        #others
    ],
    r'.*(heart palpitations|racing heart|hearth racing|pounding heart|fluttering heart).*': [
        'How long did the heart racing last?' #da cambiare
        #others
    ],
    r'.*(sweating|perspiration|hot flush|facial flushing|sudden warmth|cold sweat).*': [
        'How long did the perspiration was?' #da cambiare
        #others
    ],
    r'.*(breathing difficulty|difficulty breathing|truble breathing|short breath|breathless|struggling to breathe|restricting breathing).*': [
        'How long did the heart racing last?' #da cambiare
        #others
    ],
    r'.*(heart palpitations|racing heart|hearth racing|pounding heart|fluttering heart).*': [
        'How long did the heart racing last?' #da cambiare
        #others
    ],

}
patterns_situations = {
    r'.*(headache).*': [
        'risposta del mal di testa' #da cambiare
    ],
    r'.*(stomach pain).*': [
        'risposta del mal di stomaco' #da cambiare
    ]} #da vedere perchè non penso che si possa fare

patterns_emotions = {
    r'.*(headache).*': [
        'risposta del mal di testa' #da cambiare
    ],
    r'.*(stomach pain).*': [
        'risposta del mal di stomaco' #da cambiare
    ]
} #da finire

def ChangeEnding():
    desiredTense = input('Please enter the desired tense: ')

    #ΕΝΕΣΤΩΤΑΣ
    #Καταληξεις οριστικη ενεστωτα
    enore1 = 'ω'
    enore2 = 'εις'
    enore3 = 'ει'
    enorp1 = 'ομεν'
    enorp2 = 'ετε'
    enorp3 = 'ουσι'

    #Καταληξεις υποτακτικη ενεστωτα
    enupe1 = 'ω'
    enupe2 = 'ης'
    enupe3 = 'η'
    enupp1 = 'ωμεν'
    enupp2 = 'ητε'
    enupp3 = 'ωσι'

    #Καταληξεις ευκτικη ενεστωτα
    enefe1 = 'οιμι'
    enefe2 = 'οις'
    enefe3 = 'οι'
    enefp1 = 'οιμεν'
    enefp2 = 'οιτε'
    enefp3 = 'οιεν'

    #Καταληξεις προστακτικη ενεστωτα
    enpre1 = ''
    enpre2 = 'ε'
    enpre3 = 'ετω'
    enprp1 = ''
    enprp2 = 'ετε'
    enprp3 = 'οντων'

    #ΜΕΛΛΟΝΤΑΣ
    #Καταληξεις οριστικη μελλοντα
    meore1 = 'σω'
    meore2 = 'σεις'
    meore3 = 'σει'
    meorp1 = 'σομεν'
    meorp2 = 'σετε'
    meorp3 = 'σουσι'

    #Καταληξεις ευκτικη μελλοντα
    meefe1 = 'σοιμι'
    meefe2 = 'σοις'
    meefe3 = 'σοι'
    meefp1 = 'σοιμεν'
    meefp2 = 'σοιτε'
    meefp3 = 'σοιεν'

    #ΑΟΡΙΣΤΟΣ
    #Καταληξεις οριστικη αοριστου
    aoore1 = 'σα'
    aoore2 = 'σας'
    aoore3 = 'σε'
    aoorp1 = 'σαμεν'
    aoorp2 = 'σατε'
    aoorp3 = 'σαν'

    #Καταληξεις υποτακτικη αοριστου
    aoupe1 = 'σω'
    aoupe2 = 'σης'
    aoupe3 = 'ση'
    aoupp1 = 'σωμεν'
    aoupp2 = 'σητε'
    aoupp3 = 'σωσι'

    #Καταληξεις ευκτικη αοριστου
    aoefe1 = 'σαιμι'
    aoefe2 = 'σαις'
    aoefe3 = 'σαι'
    aoefp1 = 'σαιμεν'
    aoefp2 = 'σαιτε'
    aoefp3 = 'σαιεν'

    #Καταληξεις προστακτικη αοριστου
    aopre1 = ''
    aopre2 = 'σον'
    aopre3 = 'σατω'
    aoprp1 = ''
    aoprp2 = 'σατε'
    aoprp3 = 'σαντων'

    #Οριστικη ενεστωτα
    if desiredTense == 'εν, ορ, ε1':
        newVerb = firstpart + enore1
        print(newVerb)
    if desiredTense == 'εν, ορ, ε2':
        newVerb = firstpart + enore2
        print(newVerb)
    if desiredTense == 'εν, ορ, ε3':
        newVerb = firstpart + enore3
        print(newVerb)
    if desiredTense == 'εν, ορ, π1':
        newVerb = firstpart + enorp1
        print(newVerb)
    if desiredTense == 'εν, ορ, π2':
        newVerb = firstpart + enorp2
        print(newVerb)
    if desiredTense == 'εν, ορ, π3':
        newVerb = firstpart + enorp3
        print(newVerb)
    
    #Υποτακτικη ενεστωτα
    if desiredTense == 'εν, υπ, ε1':
        newVerb = firstpart + enupe1
        print(newVerb)
    if desiredTense == 'εν, υπ, ε2':
        newVerb = firstpart + enupe2
        print(newVerb)
    if desiredTense == 'εν, υπ, ε3':
        newVerb = firstpart + enupe3
        print(newVerb)
    if desiredTense == 'εν, υπ, π1':
        newVerb = firstpart + enupp1
        print(newVerb)
    if desiredTense == 'εν, υπ, π2':
        newVerb = firstpart + enupp2
        print(newVerb)
    if desiredTense == 'εν, υπ, π3':
        newVerb = firstpart + enupp3
        print(newVerb)

    #Ευκτικη ενεστωτα
    if desiredTense == 'εν, ευ, ε1':
        newVerb = firstpart + enefe1
        print(newVerb)
    if desiredTense == 'εν, ευ, ε2':
        newVerb = firstpart + enefe2
        print(newVerb)
    if desiredTense == 'εν, ευ, ε3':
        newVerb = firstpart + enefe3
        print(newVerb)
    if desiredTense == 'εν, ευ, π1':
        newVerb = firstpart + enefp1
        print(newVerb)
    if desiredTense == 'εν, ευ, π2':
        newVerb = firstpart + enefp2
        print(newVerb)
    if desiredTense == 'εν, ευ, π3':
        newVerb = firstpart + enefp3
        print(newVerb)

    #Προστακτικη ενεστωτα
    if desiredTense == 'εν, πρ, ε1':
        newVerb = 'none'
        print(newVerb)
    if desiredTense == 'εν, πρ, ε2':
        newVerb = firstpart + enpre2
        print(newVerb)
    if desiredTense == 'εν, πρ, ε3':
        newVerb = firstpart + enpre3
        print(newVerb)
    if desiredTense == 'εν, πρ, π1':
        newVerb = 'none'
        print(newVerb)
    if desiredTense == 'εν, πρ, π2':
        newVerb = firstpart + enprp2
        print(newVerb)
    if desiredTense == 'εν, πρ, π3':
        newVerb = firstpart + enprp3
        print(newVerb)

    #Οριστικη μελλοντα
    if desiredTense == 'με, ορ, ε1':
        newVerb = firstpart + meore1
        print(newVerb)
    if desiredTense == 'με, ορ, ε2':
        newVerb = firstpart + meore2
        print(newVerb)
    if desiredTense == 'με, ορ, ε3':
        newVerb = firstpart + meore3
        print(newVerb)
    if desiredTense == 'με, ορ, π1':
        newVerb = firstpart + meorp1
        print(newVerb)
    if desiredTense == 'με, ορ, π2':
        newVerb = firstpart + meorp2
        print(newVerb)
    if desiredTense == 'με, ορ, π3':
        newVerb = firstpart + meorp3
        print(newVerb)

    #Υποτακτικη μελλοντα
    if desiredTense == 'με, υπ, ε1':
        newVerb = 'none'
        print(newVerb)
    if desiredTense == 'με, υπ, ε2':
        newVerb = 'none'
        print(newVerb)
    if desiredTense == 'με, υπ, ε3':
        newVerb = 'none'
        print(newVerb)
    if desiredTense == 'με, υπ, π1':
        newVerb = 'none'
        print(newVerb)
    if desiredTense == 'με, υπ, π2':
        newVerb = 'none'
        print(newVerb)
    if desiredTense == 'με, υπ, π3':
        newVerb = 'none'
        print(newVerb)

    #Ευκτικη μελλοντα
    if desiredTense == 'με, ευ, ε1':
        newVerb = firstpart + meefe1
        print(newVerb)
    if desiredTense == 'με, ευ, ε2':
        newVerb = firstpart + meefe2
        print(newVerb)
    if desiredTense == 'με, ευ, ε3':
        newVerb = firstpart + meefe3
        print(newVerb)
    if desiredTense == 'με, ευ, π1':
        newVerb = firstpart + meefp1
        print(newVerb)
    if desiredTense == 'με, ευ, π2':
        newVerb = firstpart + meefp2
        print(newVerb)
    if desiredTense == 'με, ευ, π3':
        newVerb = firstpart + meefp3
        print(newVerb)

    #Προστακτικη μελλοντα
    if desiredTense == 'με, πρ, ε1':
        newVerb = 'none'
        print(newVerb)
    if desiredTense == 'με, πρ, ε2':
        newVerb = 'none'
        print(newVerb)
    if desiredTense == 'με, πρ, ε3':
        newVerb = 'none'
        print(newVerb)
    if desiredTense == 'με, πρ, π1':
        newVerb = 'none'
        print(newVerb)
    if desiredTense == 'με, πρ, π2':
        newVerb = 'none'
        print(newVerb)
    if desiredTense == 'με, πρ, π3':
        newVerb = 'none'
        print(newVerb)

    #Οριστικη αοριστου
    if desiredTense == 'αο, ορ, ε1':
        e = 'ε'
        newVerb = e + firstpart + aoore1
        print(newVerb)
    if desiredTense == 'αο, ορ, ε2':
        e = 'ε'
        newVerb = e + firstpart + aoore2
        print(newVerb)
    if desiredTense == 'αο, ορ, ε3':
        e = 'ε'
        newVerb = e + firstpart + aoore3
        print(newVerb)
    if desiredTense == 'αο, ορ, π1':
        e = 'ε'
        newVerb = e + firstpart + aoorp1
        print(newVerb)
    if desiredTense == 'αο, ορ, π2':
        e = 'ε'
        newVerb = e + firstpart + aoorp2
        print(newVerb)
    if desiredTense == 'αο, ορ, π3':
        e = 'ε'
        newVerb = e + firstpart + aoorp3
        print(newVerb)

    #Υποτακτικη αοριστου
    if desiredTense == 'αο, υπ, ε1':
        newVerb = firstpart + aoupe1
        print(newVerb)
    if desiredTense == 'αο, υπ, ε2':
        newVerb = firstpart + aoupe2
        print(newVerb)
    if desiredTense == 'αο, υπ, ε3':
        newVerb = firstpart + aoupe3
        print(newVerb)
    if desiredTense == 'αο, υπ, π1':
        newVerb = firstpart + aoupp1
        print(newVerb)
    if desiredTense == 'αο, υπ, π2':
        newVerb = firstpart + aoupp2
        print(newVerb)
    if desiredTense == 'αο, υπ, π3':
        newVerb = firstpart + aoupp3
        print(newVerb)

    #Ευκτικη αοριστου
    if desiredTense == 'αο, ευ, ε1':
        newVerb = firstpart + aoefe1
        print(newVerb)
    if desiredTense == 'αο, ευ, ε2':
        newVerb = firstpart + aoefe2
        print(newVerb)
    if desiredTense == 'αο, ευ, ε3':
        newVerb = firstpart + aoefe3
        print(newVerb)
    if desiredTense == 'αο, ευ, π1':
        newVerb = firstpart + aoefp1
        print(newVerb)
    if desiredTense == 'αο, ευ, π2':
        newVerb = firstpart + aoefp2
        print(newVerb)
    if desiredTense == 'αο, ευ, π3':
        newVerb = firstpart + aoefp3
        print(newVerb)

    #Προστακτικη αοριστου
    if desiredTense == 'αο, πρ, ε1':
        newVerb = 'none'
        print(newVerb)
    if desiredTense == 'αο, πρ, ε2':
        newVerb = firstpart + aopre2
        print(newVerb)
    if desiredTense == 'αο, πρ, ε3':
        newVerb = firstpart + aopre3
        print(newVerb)
    if desiredTense == 'αο, πρ, π1':
        newVerb = 'none'
        print(newVerb)
    if desiredTense == 'αο, πρ, π2':
        newVerb = firstpart + aoprp2
        print(newVerb)
    if desiredTense == 'αο, πρ, π3':
        newVerb = firstpart + aoprp3
        print(newVerb)

def AskForVerb():
    global verb, firstpart, secondpart, ending
    verb = str(input('Enter any verb: '))
    firstpart, secondpart = verb[:len(verb)//2], verb[len(verb)//2:]
    ending = verb[-1:]
    if len(verb) <= 5:
        j = secondpart[:1]
        secondpart = secondpart[1:]
        firstpart = firstpart + j
        ChangeEnding()
    elif len(verb) > 5:
        j = secondpart[:2]
        secondpart = secondpart[2:]
        firstpart = firstpart + j
        ChangeEnding()
    elif len(verb) > 5 and ending == 'ω':
        j = secondpart[:3]
        secondpart = secondpart[3:]
        firstpart = firstpart + j
        ChangeEnding()

AskForVerb() 

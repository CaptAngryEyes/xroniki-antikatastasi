from endings import endings


def AskForVerb():
    verb = str(input('Enter any verb: '))
    if verb[-1:] == 'ω':
        firstpart = verb[:-1]
        #Change Ending
        desiredTense = input('Please enter the desired tense: ')

        if desiredTense in endings:
            print('First part = ' + firstpart)
            for k, i in endings.items():
                if(desiredTense) == k:
                    #If the firstpart contains a double 'τ' and if the secondpart contains 'σ'
                    if firstpart[-2:] == 'ττ' and i[:1] == 'σ': # τ + σ
                        firstpart = firstpart[:-2]    
                        i = i[1:]
                        firstpart = firstpart + 'ξ' # = ξ
                        newVerb = firstpart + i
                        print(newVerb)
                    else:
                        newVerb = firstpart + i
                        print(newVerb)
        else:
            print('none')
    else:
        print('Invali Verb')

    # #Οριστικη ενεστωτα
    # if desiredTense == 'εν, ορ, ε1':
    #     newVerb = firstpart + enore1
    #     print(newVerb)
    # if desiredTense == 'εν, ορ, ε2':
    #     newVerb = firstpart + enore2
    #     print(newVerb)
    # if desiredTense == 'εν, ορ, ε3':
    #     newVerb = firstpart + enore3
    #     print(newVerb)
    # if desiredTense == 'εν, ορ, π1':
    #     newVerb = firstpart + enorp1
    #     print(newVerb)
    # if desiredTense == 'εν, ορ, π2':
    #     newVerb = firstpart + enorp2
    #     print(newVerb)
    # if desiredTense == 'εν, ορ, π3':
    #     newVerb = firstpart + enorp3
    #     print(newVerb)
    
    # #Υποτακτικη ενεστωτα
    # if desiredTense == 'εν, υπ, ε1':
    #     newVerb = firstpart + enupe1
    #     print(newVerb)
    # if desiredTense == 'εν, υπ, ε2':
    #     newVerb = firstpart + enupe2
    #     print(newVerb)
    # if desiredTense == 'εν, υπ, ε3':
    #     newVerb = firstpart + enupe3
    #     print(newVerb)
    # if desiredTense == 'εν, υπ, π1':
    #     newVerb = firstpart + enupp1
    #     print(newVerb)
    # if desiredTense == 'εν, υπ, π2':
    #     newVerb = firstpart + enupp2
    #     print(newVerb)
    # if desiredTense == 'εν, υπ, π3':
    #     newVerb = firstpart + enupp3
    #     print(newVerb)

    # #Ευκτικη ενεστωτα
    # if desiredTense == 'εν, ευ, ε1':
    #     newVerb = firstpart + enefe1
    #     print(newVerb)
    # if desiredTense == 'εν, ευ, ε2':
    #     newVerb = firstpart + enefe2
    #     print(newVerb)
    # if desiredTense == 'εν, ευ, ε3':
    #     newVerb = firstpart + enefe3
    #     print(newVerb)
    # if desiredTense == 'εν, ευ, π1':
    #     newVerb = firstpart + enefp1
    #     print(newVerb)
    # if desiredTense == 'εν, ευ, π2':
    #     newVerb = firstpart + enefp2
    #     print(newVerb)
    # if desiredTense == 'εν, ευ, π3':
    #     newVerb = firstpart + enefp3
    #     print(newVerb)

    # #Προστακτικη ενεστωτα
    # if desiredTense == 'εν, πρ, ε1':
    #     newVerb = 'none'
    #     print(newVerb)
    # if desiredTense == 'εν, πρ, ε2':
    #     newVerb = firstpart + enpre2
    #     print(newVerb)
    # if desiredTense == 'εν, πρ, ε3':
    #     newVerb = firstpart + enpre3
    #     print(newVerb)
    # if desiredTense == 'εν, πρ, π1':
    #     newVerb = 'none'
    #     print(newVerb)
    # if desiredTense == 'εν, πρ, π2':
    #     newVerb = firstpart + enprp2
    #     print(newVerb)
    # if desiredTense == 'εν, πρ, π3':
    #     newVerb = firstpart + enprp3
    #     print(newVerb)

    # #Οριστικη μελλοντα
    # if desiredTense == 'με, ορ, ε1':
    #     newVerb = firstpart + meore1
    #     print(newVerb)
    # if desiredTense == 'με, ορ, ε2':
    #     newVerb = firstpart + meore2
    #     print(newVerb)
    # if desiredTense == 'με, ορ, ε3':
    #     newVerb = firstpart + meore3
    #     print(newVerb)
    # if desiredTense == 'με, ορ, π1':
    #     newVerb = firstpart + meorp1
    #     print(newVerb)
    # if desiredTense == 'με, ορ, π2':
    #     newVerb = firstpart + meorp2
    #     print(newVerb)
    # if desiredTense == 'με, ορ, π3':
    #     newVerb = firstpart + meorp3
    #     print(newVerb)

    # #Υποτακτικη μελλοντα
    # if desiredTense == 'με, υπ, ε1':
    #     newVerb = 'none'
    #     print(newVerb)
    # if desiredTense == 'με, υπ, ε2':
    #     newVerb = 'none'
    #     print(newVerb)
    # if desiredTense == 'με, υπ, ε3':
    #     newVerb = 'none'
    #     print(newVerb)
    # if desiredTense == 'με, υπ, π1':
    #     newVerb = 'none'
    #     print(newVerb)
    # if desiredTense == 'με, υπ, π2':
    #     newVerb = 'none'
    #     print(newVerb)
    # if desiredTense == 'με, υπ, π3':
    #     newVerb = 'none'
    #     print(newVerb)

    # #Ευκτικη μελλοντα
    # if desiredTense == 'με, ευ, ε1':
    #     newVerb = firstpart + meefe1
    #     print(newVerb)
    # if desiredTense == 'με, ευ, ε2':
    #     newVerb = firstpart + meefe2
    #     print(newVerb)
    # if desiredTense == 'με, ευ, ε3':
    #     newVerb = firstpart + meefe3
    #     print(newVerb)
    # if desiredTense == 'με, ευ, π1':
    #     newVerb = firstpart + meefp1
    #     print(newVerb)
    # if desiredTense == 'με, ευ, π2':
    #     newVerb = firstpart + meefp2
    #     print(newVerb)
    # if desiredTense == 'με, ευ, π3':
    #     newVerb = firstpart + meefp3
    #     print(newVerb)

    # #Προστακτικη μελλοντα
    # if desiredTense == 'με, πρ, ε1':
    #     newVerb = 'none'
    #     print(newVerb)
    # if desiredTense == 'με, πρ, ε2':
    #     newVerb = 'none'
    #     print(newVerb)
    # if desiredTense == 'με, πρ, ε3':
    #     newVerb = 'none'
    #     print(newVerb)
    # if desiredTense == 'με, πρ, π1':
    #     newVerb = 'none'
    #     print(newVerb)
    # if desiredTense == 'με, πρ, π2':
    #     newVerb = 'none'
    #     print(newVerb)
    # if desiredTense == 'με, πρ, π3':
    #     newVerb = 'none'
    #     print(newVerb)

    # #Οριστικη αοριστου
    # if desiredTense == 'αο, ορ, ε1':
    #     e = 'ε'
    #     newVerb = e + firstpart + aoore1
    #     print(newVerb)
    # if desiredTense == 'αο, ορ, ε2':
    #     e = 'ε'
    #     newVerb = e + firstpart + aoore2
    #     print(newVerb)
    # if desiredTense == 'αο, ορ, ε3':
    #     e = 'ε'
    #     newVerb = e + firstpart + aoore3
    #     print(newVerb)
    # if desiredTense == 'αο, ορ, π1':
    #     e = 'ε'
    #     newVerb = e + firstpart + aoorp1
    #     print(newVerb)
    # if desiredTense == 'αο, ορ, π2':
    #     e = 'ε'
    #     newVerb = e + firstpart + aoorp2
    #     print(newVerb)
    # if desiredTense == 'αο, ορ, π3':
    #     e = 'ε'
    #     newVerb = e + firstpart + aoorp3
    #     print(newVerb)

    # #Υποτακτικη αοριστου
    # if desiredTense == 'αο, υπ, ε1':
    #     newVerb = firstpart + aoupe1
    #     print(newVerb)
    # if desiredTense == 'αο, υπ, ε2':
    #     newVerb = firstpart + aoupe2
    #     print(newVerb)
    # if desiredTense == 'αο, υπ, ε3':
    #     newVerb = firstpart + aoupe3
    #     print(newVerb)
    # if desiredTense == 'αο, υπ, π1':
    #     newVerb = firstpart + aoupp1
    #     print(newVerb)
    # if desiredTense == 'αο, υπ, π2':
    #     newVerb = firstpart + aoupp2
    #     print(newVerb)
    # if desiredTense == 'αο, υπ, π3':
    #     newVerb = firstpart + aoupp3
    #     print(newVerb)

    # #Ευκτικη αοριστου
    # if desiredTense == 'αο, ευ, ε1':
    #     newVerb = firstpart + aoefe1
    #     print(newVerb)
    # if desiredTense == 'αο, ευ, ε2':
    #     newVerb = firstpart + aoefe2
    #     print(newVerb)
    # if desiredTense == 'αο, ευ, ε3':
    #     newVerb = firstpart + aoefe3
    #     print(newVerb)
    # if desiredTense == 'αο, ευ, π1':
    #     newVerb = firstpart + aoefp1
    #     print(newVerb)
    # if desiredTense == 'αο, ευ, π2':
    #     newVerb = firstpart + aoefp2
    #     print(newVerb)
    # if desiredTense == 'αο, ευ, π3':
    #     newVerb = firstpart + aoefp3
    #     print(newVerb)

    # #Προστακτικη αοριστου
    # if desiredTense == 'αο, πρ, ε1':
    #     newVerb = 'none'
    #     print(newVerb)
    # if desiredTense == 'αο, πρ, ε2':
    #     newVerb = firstpart + aopre2
    #     print(newVerb)
    # if desiredTense == 'αο, πρ, ε3':
    #     newVerb = firstpart + aopre3
    #     print(newVerb)
    # if desiredTense == 'αο, πρ, π1':
    #     newVerb = 'none'
    #     print(newVerb)
    # if desiredTense == 'αο, πρ, π2':
    #     newVerb = firstpart + aoprp2
    #     print(newVerb)
    # if desiredTense == 'αο, πρ, π3':
    #     newVerb = firstpart + aoprp3
    #     print(newVerb)


AskForVerb() 

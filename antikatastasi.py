from endings import endings #Import the endings dictionary from the endings.py file


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
                        firstpart = firstpart + 'ξ'             # = ξ
                        newVerb = firstpart + i
                        print(newVerb)
                    else:
                        newVerb = firstpart + i
                        print(newVerb)
        else:
            print('none')
    else:
        print('Invali Verb')

AskForVerb() 

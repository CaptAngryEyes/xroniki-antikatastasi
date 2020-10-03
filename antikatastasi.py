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
                    #LETTER COMBINATION
                    # -START- τ + σ = ξ
                    if (firstpart[-1:] == 'τ' and i[:1] == 'σ'):
                        firstpart = firstpart[:-1]    
                        i = i[1:]
                        firstpart = firstpart + 'ξ'
                        newVerb = firstpart + i
                        print(newVerb)
                    elif (firstpart[-2:] == 'ττ' and i[:1] == 'σ'):
                        firstpart = firstpart[:-2]    
                        i = i[1:]
                        firstpart = firstpart + 'ξ'
                        newVerb = firstpart + i
                        print(newVerb)
                    # -END- τ + σ = ξ
                    # -START- φ + σ = ψ
                    elif (firstpart[-1:] == 'φ' and i[:1] == 'σ'):
                        firstpart = firstpart[:-1]    
                        i = i[1:]
                        firstpart = firstpart + 'ψ'
                        newVerb = firstpart + i
                        print(newVerb)
                    elif (firstpart[-2:] == 'φφ' and i[:1] == 'σ'):
                        firstpart = firstpart[:-2]    
                        i = i[1:]
                        firstpart = firstpart + 'ψ'
                        newVerb = firstpart + i
                        print(newVerb)
                    else:
                        newVerb = firstpart + i
                        print(newVerb)
                    # -END- φ + σ = ψ
        else:
            print('none')
    else:
        print('Invali Verb')

AskForVerb() 

from endings import endings #Import the endings dictionary from the endings.py file


def AskForVerb():
    verb = str(input('Enter any verb: '))
    if verb[-1:] == 'ω':
        firstpart = verb[:-1]
        #Change Ending
        desiredTense = input('Please enter the desired tense: ')

        if desiredTense in endings:
            print('First part = ' + firstpart)
            symfona = ('β', 'γ', 'δ', 'ζ', 'θ', 'κ', 'λ', 'μ', 'ν', 'ξ', 'π', 'ρ', 'σ', 'τ', 'φ', 'χ', 'ψ')
            #Almost all verbs starting with one of the letters above get an 'ε' at the start when in 'Αοριστος'
            if desiredTense[:2] == 'ao' and verb[:1] == 'ρ':
                firstpart = 'ερ' + firstpart            #Verbs starting with 'ρ' get an extra 'ε' and 'ρ'
            elif desiredTense[:2] == 'ao' and verb[:1] in symfona:
                firstpart = 'ε' + firstpart
            for k, i in endings.items():
                if(desiredTense) == k:
                    #LETTER COMBINATION
                    # τ + σ = ξ
                    if (firstpart[-2:] == 'πτ' and i[:1] == 'σ'):
                        firstpart = firstpart[:-2]    
                        i = i[1:]
                        firstpart = firstpart + 'ψ'
                        newVerb = firstpart + i
                        print(newVerb)
                    elif (firstpart[-2:] == 'ττ' and i[:1] == 'σ'):
                        firstpart = firstpart[:-2]    
                        i = i[1:]
                        firstpart = firstpart + 'ξ'
                        newVerb = firstpart + i
                        print(newVerb)
                    elif (firstpart[-1:] == 'τ' and i[:1] == 'σ'):
                        firstpart = firstpart[:-1]    
                        i = i[1:]
                        firstpart = firstpart + 'ξ'
                        newVerb = firstpart + i
                        print(newVerb)
                    # φ + σ = ψ
                    elif (firstpart[-2:] == 'φφ' and i[:1] == 'σ'):
                        firstpart = firstpart[:-2]    
                        i = i[1:]
                        firstpart = firstpart + 'ψ'
                        newVerb = firstpart + i
                        print(newVerb)
                    elif (firstpart[-1:] == 'φ' and i[:1] == 'σ'):
                        firstpart = firstpart[:-1]    
                        i = i[1:]
                        firstpart = firstpart + 'ψ'
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

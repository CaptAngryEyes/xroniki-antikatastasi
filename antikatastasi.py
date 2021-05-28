from endings import endings_ener, endings_mesi #Import the endings dictionarys from the endings.py file


def AskForVerb():
    verb = str(input('Enter any verb: '))
    if verb[-1:] == 'ω':
        firstpart = verb[:-1]
        #Change Ending
        desiredTense = input('Please enter the desired tense: ')

        #ΕΝΕΡΓΗΤΙΚΗ ΦΩΝΗ

        if desiredTense in endings_ener:
            print('First part = ' + firstpart)
            symfona = ('β', 'γ', 'δ', 'ζ', 'θ', 'κ', 'λ', 'μ', 'ν', 'ξ', 'π', 'σ', 'τ', 'φ', 'χ', 'ψ')
            #Almost all verbs starting with one of the letters above get an 'ε' at the start when in 'Αοριστος' or 'Παρατατικος'
            if desiredTense[:2] == 'ao' or desiredTense[:2] == 'pa' and verb[:1] == 'ρ':
                firstpart = 'ερ' + firstpart            #Verbs starting with 'ρ' get an extra 'ε' and 'ρ'
            elif desiredTense[:2] == 'ao' or desiredTense[:2] == 'pa' and verb[:1] in symfona:
                firstpart = 'ε' + firstpart
            elif desiredTense[:2] == 'yp':
                #Duplication
                if verb[:1] != 'χ':
                    print(verb[:1])
                    firstpart = 'ε' + verb[:1] + 'ε' + firstpart
                elif verb[:1] != 'φ':
                    print(verb[:1])
                    firstpart = 'ε' + verb[:1] + 'ε' + firstpart
                elif verb[:1] != 'θ':
                    print(verb[:1])
                    firstpart = 'ε' + verb[:1] + 'ε' + firstpart
                # χ --> κ
                elif verb[:1] == 'χ':
                    firstpart = 'ε' + 'κ' + 'ε' + firstpart
                # φ --> π
                elif verb[:1] == 'φ':
                    firstpart = 'ε' + 'π' + 'ε' + firstpart
                # θ --> τ
                elif verb[:1] == 'θ':
                    firstpart = 'ε' + 'τ' + 'ε' + firstpart

            for k, i in endings_ener.items():
                if(desiredTense) == k:
                    #LETTER COMBINATION
                    #πτ + σ = ψ
                    if (firstpart[-2:] == 'πτ' and i[:1] == 'σ'):
                        firstpart = firstpart[:-2]
                        i = i[1:]
                        firstpart = firstpart + 'ψ'
                        newVerb = firstpart + i
                        print(newVerb)
                    # τ + σ = ξ
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
                    # τ + κ
                    elif (firstpart[-2:] == 'ττ' and i[:1] == 'κ'):
                        firstpart = firstpart[:-2]
                        i = i[1:]
                        firstpart = firstpart + 'χ'
                        newVerb = firstpart + i
                        print(newVerb)
                    elif (firstpart[-1:] == 'τ' and i[:1] == 'κ'):
                        firstpart = firstpart[:-1]
                        i = i[1:]
                        firstpart = firstpart + 'χ'
                        newVerb = firstpart + i
                        print(newVerb)
                    else:
                        newVerb = firstpart + i
                        print(newVerb)


        #ΜΕΣΗ ΦΩΝΗ

        elif desiredTense in endings_mesi:
            print('First part = ' + firstpart)
            symfona = ('β', 'γ', 'δ', 'ζ', 'θ', 'κ', 'λ', 'μ', 'ν', 'ξ', 'π', 'ρ', 'σ', 'τ', 'φ', 'χ', 'ψ')
            #Almost all verbs starting with one of the letters above get an 'ε' at the start when in 'Αοριστος' or 'Παρατατικος'
            if desiredTense[:2] == 'ao' or desiredTense[:2] == 'pa' and verb[:1] == 'ρ':
                firstpart = 'ερ' + firstpart            #Verbs starting with 'ρ' get an extra 'ε' and 'ρ'
            elif desiredTense[:2] == 'ao' or desiredTense[:2] == 'pa' and verb[:1] in symfona:
                firstpart = 'ε' + firstpart

            for k, i in endings_mesi.items():
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

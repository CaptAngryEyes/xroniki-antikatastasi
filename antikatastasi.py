from endings import endings_ener, endings_mesi
import re

def ask_verb_info():
    verb = input("Verb: ")
    tense = input("Tense: ")
    eglisi = input("Eglisi")

    return verb, tense, eglisi

def get_preverb(verb):
    if (verb[-1:] != "ω") and (verb[-4:] != "ομαι"):
        return False
    
    if verb[-1:] == "ω":
        preverb = verb[:-1]
    elif verb[-4:] == "ομαι":
        preverb = verb[:-4]
    else:
        preverb = None

    return preverb

def add_afksisi(verb, tense, eglisi):
    # Source: https://filologikaek.blogspot.com/2019/02/7.html

    symfona = ["β", "γ", "δ", "ζ", "θ", "κ", "λ", "μ", "ν", "ξ", "π", "ρ", "σ", "τ", "φ", "χ", "ψ"]
    fonienta = ["α", "ε", "η", "ι", "ο", "υ", "ω"]
    prothesis = ["απο", "αντι", "εκ", "εξ", "προ", 
                 "εν", "εγ", "συν", "εισ", "εσ", "ανα", "δια", 
                 "κατα", "υπερ", "αμφι", "επι", "μετα", 
                 "παρα", "περι", "προσ", "υπο", "ωσ"]

    prothesi_regex = re.compile(r'(απο|αντι|εκ|εξ|προ|εν|εγ|συν|εισ|εσ|ανα|δια|κατα|υπερ|αμφι|επι|μετα|παρα|περι|προσ|υπο|ωσ){1}(\w+)')
    mo = prothesi_regex.search(verb)

    new_verb = verb

    if eglisi == "oristiki":
        if (tense == "paratatikos") or (tense == "aoristos"):
            try:
                prothema = str(mo.group(1))
                main_part = str(mo.group(2))

                if main_part[0] in symfona:
                    new_verb = prothema + "ε" + main_part
                elif main_part[0] in fonienta:
                    if main_part[0] == "α":
                        new_verb = prothema + "η" + main_part[1:]
                    elif main_part[0] == "ε":
                        new_verb = prothema + "η" + main_part[1:]
                    elif main_part[0] == "ο":
                        new_verb = prothema + "ω" + main_part[1:]
                    elif main_part[:2] == "αι":
                        new_verb = prothema + "η" + main_part[1:]
                    elif main_part[:2] == "ει":
                        new_verb = prothema + "η" + main_part[1:]
                    elif main_part[:2] == "αυ":
                        new_verb = prothema + "ηυ" + main_part[1:]
                    elif main_part[:2] == "ευ":
                        new_verb = prothema + "ηυ" + main_part[1:]
                    elif main_part[:2] == "οι":
                        new_verb = prothema + "ω" + main_part[1:]

            except(AttributeError):
                if verb[1] in symfona:
                    new_verb = "ε" + verb
                elif verb[1] in fonienta:
                    if verb[1] == "α":
                        new_verb = "η" + verb[1:]
                    elif verb[1] == "ε":
                        new_verb = "η" + verb[1:]
                    elif verb[1] == "ο":
                        new_verb = "ω" + verb[1:]
                    elif verb[:2] == "αι":
                        new_verb = "η" + verb[1:]
                    elif verb[:2] == "ει":
                        new_verb = "η" + verb[1:]
                    elif verb[:2] == "αυ":
                        new_verb = "ηυ" + verb[1:]
                    elif verb[:2] == "ευ":
                        new_verb = "ηυ" + verb[1:]
                    elif verb[:2] == "οι":
                        new_verb = "ω" + verb[1:]
    
    return new_verb

def replace(verb, tense, eglisi):
    
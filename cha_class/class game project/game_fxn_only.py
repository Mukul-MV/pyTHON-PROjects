import json
import random
import time

letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
vowels = "AEIOU"
vowel_cost = 250

def getNumberBetween(prompt,min,max) :  #is fxn ka use pta nahi chala kya h?

    '''ask user number between max / min with prompt'''
    userip = input(prompt)
    
    while True :
        
        try :
            n = int(userip)
            
            if n<min:
                errmsg = "Must be at least {}".format(min)
            elif n>max:
                errmsg = "Must be at most {}".format(max)
            else:
                return n
        except ValueError :
            errmsg = "{} is not a number".format(userip)
            
        userip = input("{}\n{}".format(errmsg,prompt))

def spinWheel():  # isme doubt ye h ki ye dictonary ese kyo banai h ? 
    '''spinning the wheel and return a dictionary with random prize'''
    '''Example :-
                    {"type":"cash","text":"$950","value":950,"prize":"A trip to taj Mahal"}
                    {"type":"bankrupt","text":"Bankrupt","prize":Fasle}
                    {"type":"loseturn","text":"Lose a turn","prize":Fasle}'''
    with open("wheel.json","r") as f:
        wheel = json.loads(f.read())
        return random.choice(wheel)

def getRandomCategoryAndPhrase():   #haan ye smjh agaya pura
    '''return a tuple with a random category and phrase for player to guess'''
    '''("Artisit and Song" : "full song ")'''
    with open("phrases.json","r") as f:
        phrases = json.loads(f.read())
        category = random.choice(list(phrases.keys()))
        phrase = random.choice(phrases[category])
        
        return (category,phrase.upper())

#isme ekto logic dekhle , apne khud wala lga skta h ki ni , or letter variable use na kare to chlega ?
 # jaha tak mujhe lgra h ye pura phrase check kr re h to time jada lgega
def obscurePhase(phrase,guessed):
    '''return obscure phrase for user to predict next letter or full phrase'''
    '''Example :-
                    guessed : ['L','K','J','H','G','F','D','S','A']
                    phrase :  "GLACIER NATIONAL PARK"
                    return  : "GLA____ _A____AL _A_K"'''
    rv = ""
    for s in phrase :
        if(s in letters) and (s not in guessd):
            rv = rv+"_"
        else:
            rv = rv+s
    return rv
 
def showBoard(category,obscuredPhrase,guessed): #pehle ye ki ye fxn kam ka h ki ni ,
                                                #dusra ki iska return kuch alag hi h
    '''return string representing current status of game'''
    return """
           Category : {}
           Phrase : {}
           Guessed : {}
           """.format(category,obscuredPhrase,''.join(sorted(guessed)))

'''changes'''

import game_fxn_only as f
import random

class WOFPlayer:
    '''all players starts from here '''
    
    def __init__(self,name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
        
    def addMoney(self,amt):
        '''this fxn add wining amount to existing value'''
        self.prizeMoney += amt
        
    def goBankkrupt(self):
        '''this fxn will nulify all the wining amount'''
        self.prizeMoney = 0
        
    def addPrize(self,prize):
        self.prizes.append(prize)
        
    def __str__(self):
        
        frmt = "name == '{}' and prizeMoney == {} ".format(self.name,self.prizeMoney)


class WOFHumanPlayer(WOFPlayer):  #isme fxn me logic na lga k main me lgaya h esa kyo ?
                                    #or isme class common krdi name ,prize k liye , jese mene do alag ki thi

    '''in this all the data from players class
        and ask user for input'''
    def getMove(self,category,obscuredPhrase,guesses):
        '''ask user for input and display all the data'''
        print("{} has $ {}".format(self.name,self.prizeMoney))
        f.showBoard()
        get_move = input("Guess a letter,phrase ,or type 'exit', 'pass'")
        
        return get_move

class WOFComputerPlayer(WOFPlayer): #yaha WOFHumanPlayer class pass kyo ni ki ?
    '''tHIS class is decribing all computer players move and its diffulty levl  '''
    
    SORTED_FREQUENENCIES = "ZQXJKVBPYGFWMUCLDRSHNIOATE" # English letter frequency from least (Z) to most(E)
    
    def __init__(self,name,difficulty):
        super().__init__(name)
        self.difficulty = difficulty
        
    def smartCoinFlip(self):
        '''this fxn used to choose difficulty level of computer '''
        #player_lvl = getNumberBetween("Choose computer level from 1 to 10",1,10)
        
        if random.randint(1,10) > self.difficulty:
            return True
        else :
            return False
        
    def getPossibleLetters(self,guessed):
        '''this fsn return list of possible letters that can be gussed'''
        
        can_gussed = []
        
        for i in f.letter:
            if i not in guessed and self.prizeMoney >= 250:
                can_gussed.append(i)
                self.prizeMoney -= f.vowel_cost
            elif i not in guessed and i not in f.vowels:
                can_gussed.append(i)
            else:
                continue
        return can_gussed
                
    def getMove(self,category,obscuredPhrase,guessed):
        '''this fxn return possible letter from computer side'''
        possible_char = self.getPossibleLetters(guessed)
        
        f.showBoard(category,obscuredPhrase,guessed) #why this fxn is being used
        
        if len(possible_char)==0:
            return 'pass'
        elif self.smartCoinFlip():
            for i in self.SORTED_FREQUENENCIES:
                if i in possible_char:
                    return i
                else:
                    continue
        else:
            return random.choice(possible_char)

           
        
        
        
        
        
        
        
        
        
    



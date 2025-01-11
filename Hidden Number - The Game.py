#!/usr/bin/env python
# coding: utf-8

# In[43]:


# HIDDEN NUMBER - THE GAME #

#Defining functions
def invalid_input():
    text = ('Invalid input. Restart the game.')
    print(text)

def no_problem():
    text = ("\nNo problem at all!. See you when you're ready " + name.title() + '!')
    print(text)

def rules_expl():
    text = ("\nLet's play the game. You'll be given a range of numbers between 1 and 10 in which an hidden_number must be found.")
    print(text)

def attempts():
    text = ("\nYou have 3 attempts total. Use them wisely. \n\nInsert a number between 1 and 10")
    print(text)

def first_attempt_wrong():
    text = ('\nYou guessed it wrong! Try again. You have 2 attempts left. You can do it!')
    print(text)

def second_attempt_wrong():
    text = ("\nYou guessed it wrong! Try again. You have 1 attempt left. Choose wisely!")
    print(text)

def you_won():
    text = ('\nYou guessed it right! The hidden_number is ' + str(hidden_number) + '. \n\n 🎉🎉🎉🎉🎉🎉🎉 YOU WON! 🎉🎉🎉🎉🎉🎉🎉')
    print(text)

def you_lost():
    text = ("\nYou guessed it wrong! You don't have any attempt left. \n\n🤡🤡🤡🤡🤡🤡🤡 YOU LOST!🤡🤡🤡🤡🤡🤡🤡 \n\nThe hidden_number is " + str(hidden_number) + '.')
    print(text)

def thanks_for_playing():
    text = ('\n\nThanks for playing! See you next time')
    print(text)
    

#Welcoming the player
import random

while True:
    while True:
        name = input('\nHello new_player. Insert your name: ')
        if name.isdigit():
            invalid_input()
            continue        
        
        welcome_message = print('\nHi ' + name.title() + '. Welcome to HIDDEN NUMBERS - THE GAME!')
    
        wanna_play = input('\nWanna play?? (yes/no): ')
        if wanna_play.isdigit():
            invalid_input()
            continue
        elif wanna_play.lower() in ('no', 'nope', 'n'):
             no_problem()
             continue
    
        
#Rules   
        rules_expl()        
        rules = input('\nType OK to continue otherwise NO to restart the game: ')
        if rules.isdigit():
            invalid_input()
            continue
        elif rules.lower() in ('no','nope','n'):
            no_problem()
            continue
                
            
    
#Playing the game
        attempts()    
        hidden_number = random.randint(1,10)
    
        first_attempt = input('\nFirst attempt: ')
        if first_attempt != str(hidden_number):
            first_attempt_wrong()
        else:
            you_won()
            break
            
    
        second_attempt = input('\nSecond attempt: ')
        if second_attempt != str(hidden_number):
            second_attempt_wrong()
        else:
            you_won()
            break
            
    
        third_attempt = input('\nThird attempt: ')
        if third_attempt != str(hidden_number):
            you_lost()
            break        
        else:
            you_won()
            break
            
    
#New_challenge
    new_challenge = input('\nWanna try again?? (yes/no): ')
    if new_challenge.lower() in ('no', 'nope', 'n'):
        thanks_for_playing()
        break




# In[ ]:





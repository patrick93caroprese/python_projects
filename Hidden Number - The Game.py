#!/usr/bin/env python
# coding: utf-8

# In[1]:


#MY VERSION OF THE GAME

#Rules of the game:
#1️⃣ Players have 3 attempts to guess the hidden number.
#2️⃣ If a player guesses correctly, the game should congratulate them and end immediately. 🎉
#3️⃣ If the player fails to guess the number after 3 attempts, the game will reveal the hidden number and end. 🚫

#💡 Your Challenge:
#Write a Python program to implement this game! 🐍

#The hidden_number is RANDOM#


#Welcoming the player
import random

while True:
    while True:
        name = input('\nHello new_player. Insert your name: ')
        if name.isdigit():
            print('Invalid input. Try again')
            continue
        
        
        welcome_message = print('\nHi ' + name.title() + '. Welcome to HIDDEN NUMBERS - THE GAME!')
    
        wanna_play = input('\nWanna play?? (yes/no): ')
        if wanna_play.isdigit():
            print('Invalid input. Restart the game.')
            continue
        elif wanna_play.lower() in ('no', 'nope', 'n'):
             print("\nNo problem at all!. See you when you're ready " + name.title() + '!')
             continue
    
        
#Rules   
        rules = input("\nLet's play the game. You'll be given a range of number between 1 and 10 in which an hidden_number must be found. \n\nType OK to continue otherwise NO to restart the game: ")
        if rules.isdigit():
            print('Invalid input. Restart the game.')
            continue
        elif rules.lower() in ('no'):
            print("\nNo problem at all!. See you when you're ready " + name.title() + '!')
            continue
                
            
    
#Playing the game
        attempts = print('\nYou have 3 attempts total. Use them wisely.  \n\nInsert a number between 1 and 10')
    
        hidden_number = random.randint(1,10)
    
        first_attempt = input('\nFirst attempt: ')
        if first_attempt != str(hidden_number):
            print("\nYou guessed it wrong! Try again. You have 2 attempts left. You can do it!")
        else:
            print('\nYou guessed it right! The hidden_number is ' + str(hidden_number) + '. \n\n 🎉🎉🎉🎉🎉🎉🎉 YOU WON! 🎉🎉🎉🎉🎉🎉🎉')
            break
            
    
        second_attempt = input('\nSecond attempt: ')
        if second_attempt != str(hidden_number):
            print("\nYou guessed it wrong! Try again. You have 1 attempt left. Choose wisely!")
        else:
            print('\nYou guessed it right! The hidden_number is ' + str(hidden_number) + '. \n\n 🎉🎉🎉🎉🎉🎉🎉 YOU WON! 🎉🎉🎉🎉🎉🎉🎉')
            break
            
    
        third_attempt = input('\nThird attempt: ')
        if third_attempt != str(hidden_number):
            print("\nYou guessed it wrong! You don't have any attempt left. \n\n🤡🤡🤡🤡🤡🤡🤡 YOU LOST!🤡🤡🤡🤡🤡🤡🤡 \n\nThe hidden_number is " + str(hidden_number) + '.')
            break        
        else:
            print('\nYou guessed it right! The hidden_number is ' + str(hidden_number) + '. \n\n 🎉🎉🎉🎉🎉🎉🎉 YOU WON! 🎉🎉🎉🎉🎉🎉🎉')
            break
            
    
#New_challenge
    new_challenge = input('\nWanna try again?? (yes/no):')
    if new_challenge in ('no', 'nope', 'n'):
        break




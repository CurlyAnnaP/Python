#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 12:09:05 2018

@author: a.podolskaya

Docstring:
"""

"""

    Welcome to the Russian Adventure game! You will  be a part of travelling 
    game to Russia, where you need to choose next steps to move forward.
    There will be some tricky questions, loops and failed options.
    Bugs: waiting fucntion is not perfect, you should press enter button every
    time to count down.
    
"""    
    
    
    
print("\f")



### Enter the name and start game, moving to next stage ####

from sys import exit

def start():
    global name_1
    print("\nHello, player! What is your name?", end = ' ')
    name_1 = input("> ")
    print(f"""
      Hello {name_1} ! Welcome to our adventure in Russia. Are you ready 
      to make an important decission?
      """)
    input("\n <Press enter to see your story >\n")
    print("\f")
    
    city_decision()

### define next function with first option choice with next steps, loop or fail

def city_decision():
    print(f"""
      Perfect, you are in! You are in SFO, but there is no direct flight to 
      Moscow, which city should be your layover for faster trip 
      (choose a number):
    """)
    print("1) London ")
    print("2) Dallas  ") 
    print("3) Los Angeles  ")
    print("4) Berlin ")
    city_choice = input("Which city you will choose: ")
    
    if "1" in city_choice or "ondon" in city_choice :
        print("It will take more time, but you can make it", end= '')
        print("\f")
        visa()
        
    elif "2" in city_choice or "allas" in city_choice :
        print(f"""
              It will take forever,  Texas cowbow found out you as his 
              whiskey buddy and you DIE"
              """)
        print("\f")
        fail()
    
    elif  "3" in city_choice or "geles" in city_choice or "LA"in city_choice:
        print("It is correct, let's start our crazy journey\n")
        visa()
    elif  "4" in city_choice or "erlin" in city_choice :
        print(f"""
              It will take few more stops and you decided to join 
              Octoberfest, where you DIE after crazy amount of beer! 
              Let's try again \n
              """)
        city_decision()
    else:
        print(f"""
              Please, try again
              """)
        city_decision()
        
        
### define next stage, plus wait function with loop  
        
def visa(): 
    print(f"""
          We are on the way to Moscow, but what about your visa? 
          Did you remeber that KGB will check you?
          Which country your passport? 
    """)
    print("1) North, Central, South America ")
    print("2) European Union  ") 
    print("3) Asian region  ")
    visa_choice = input("Which passport do you have? ")
    if "1" in visa_choice or "USA" in visa_choice or "Ame" in visa_choice :
        print("Russia is open for travelling, but you need to get visa\n")
        print("\f")
        wait()
        bear()
    
    elif "2" in visa_choice or "EU" in visa_choice or "urop" in visa_choice : 
        print(f"""Are you sure you are ready?! It will take some time. 
              Let's explore Moscow "
              """)
        print("\f")
        wait()
        bear()        
        
    else:
        print("You are ready to go! Let's explore Moscow ", end = '')
        print("\f")
        bear()
#define next stage plus failure options

def bear():
    print(f"""
          Look around: Red Square, matreshka, cafes, vodka, everything 
          so beautiful, cheap and so tasty. Where is a bear?
          """)
    print("1) We forgot to check on the Red Square")
    print("2) Bullshit, there is no bears in Moscow. Probably... ")
    print("3)  Where am i? ")
    
    moscow_view= input("What do you think: ")
    if "1" in moscow_view or "ed"in moscow_view :
        print("We forgot to check on the Red Square, but ...")
        print("\f")
        party()
    elif "2" in moscow_view or "shit" in moscow_view :
        print("Bullshit, there is no bears in Moscow")
        print("\f")
        party()
    elif "3" in moscow_view or "here" in moscow_view:
        print("Looks like someone lost!")
        fail()

def party():
    print(f"""
          You are in the club and Moscow Never Sleep, if you survive you
          will be able to join afterparty at 5am,
          but becareful with your passport or ID. 
          """)
    print("1) You are still alive, wanna some extra vodka + cola shot?")
    print("2) Drunk as ... ")
    print("3) Where am I?  ")
    party_choice =input("What do you think? ")
    
    if "1" in party_choice or "live" in party_choice or "vodka" in party_choice:
        print("You made it! Sightseeing time! ")
        print("\f")
        vocabluary()
        
    elif "2" in party_choice or "runk" in party_choice:
        print("Oops..")
        print("\f")
        fail()
    else:
        print("\f")
        bear()
def vocabluary():
    print(f"""
          Time to explore more interesting places in Moscow,
          but let's check your Russian vocabluary. 
          What does mean Borcsh?
          """)
    print("a) Monster")
    print("b) Tasty beet root soup ")
    print("c) Grandmother ")
    print("d) Part of the body")
    voca_choice= input("Choose the letter, please:  ")
    
    if "a" in voca_choice or "c" in voca_choice or "d" in voca_choice:
        print("Wrong! Wrong! Wrong! ")
        vocabluary()
    elif "b" in voca_choice:
        print("Good job! ")
        print("\f")
        final()
        
# define final note before game end plus using global variable        

def final():
    print(f"""
          Made it!  
          Moscow is a beautiful city, no doubts. Kremlin, Red Square , 
          The Cathedral of Vasily the Blessed, and parks! But it is time 
          to go home. And you made it!
          """)
    print(f"""
          Thank you {name_1}. You survived in the most interesting 
          journey of your life!
          """)
    input('<Press any key to exit>\n')
    print("\f")
    exit(0)
### wait function  (loop) , could be debug without print out number and pressing
###    enter button
    
def wait():
    
    count = 5
    print("\f")
    while count > 0:
          print(count)
          count -= 1
          input("< Processing your visa. Press ENTER to continue. >\n")

    print("All set!") 
   
# define fail function , which we using in the wrong answers 
    
def fail():
    print("Sorry, adventure is over!")
    input('<Press any key to exit>\n')
    print("\f")
    exit(0)
start()

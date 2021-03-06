"""
ASSIGNMENT 3: QUIZ
Program by Kevin and Steven
Search module by Kevin
"""

import time
from userChoice import *

def findLine ():

    """
       this function searches through a file for any matching lines.
       it will then go through these questions in order until a match
       is chosen. Once a match is chosen, it is re-confirmed by the
       user, and is returned from the function to be used for deletion.
       Kevin K.
    """
    
    while True:
        root = open("questions.txt","r")
        results = []

        print (" Type a keyword to find your question. It will then find any ")
        print (" matching question(s) in the database that contain that phrase.")
        print (" The matching line(s) will then be displayed in order of ")
        print (" appearance, and you will be asked if the displayed question ")
        print (" is the one you want removed. once you find the question, there")
        print (" will be a confirmation message, to remove accidental deletion.")
        print (" if your question is not found, please refine your search term ")
        print (" and run the search again. If you cannot find it, the question ")
        print (" may not have been added, and we recommend you re-enter it in ")
        print ("create.\n")
        
        keywords = input("Enter your Search Term: ")
        
        for line in root:
            if keywords in line:
                results.append(line) #added functionality. returns all matches
                                     #rather than first
        root.close()
        
        print ("searching",end="")
        time.sleep(0.5)
        print (".",end="")
        time.sleep(0.5)
        print (".",end="")
        time.sleep(0.5)
        print (".")
        
        if results:
            
            for question in results:
                print ("Match Found!\n",question)

                correct = userChoice("yn","is this the question you want deleted? y/n: ")
                if correct == True:
                    return question
            
        print ("There are no matching results. Try refining your Search Terms.")
        exits = userChoice("yn","Do you want to try again? y/n: ")
        if exits == False:
            print ("Returning to menu...")
            time.sleep(1)
            break

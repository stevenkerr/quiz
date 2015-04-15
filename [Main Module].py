"""
ASSIGNMENT 3: QUIZ
Program by Kevin and Steven
"""
import random,time
from Add_and_Delete_Line import *
from search_Module import *
from userChoice import *

def optionCheck(low,hi):
    """checks that selected option is between low and hi"""
    while True:
        try:
            choice = int(input("\nPlease choose an Option:\n"))
            if choice>=low and choice<=hi:
                break
            else:
                print ("Error 1: Integer value does not meet parameters.")
        except:
            print ("Error 2: User input is not an integer.")
    return int(choice)

def main ():
    '''main function of program, contains the main menu'''
    while True:
        print ("\tMAIN MENU")
        print ("")
        print ("1.PLAY RANDOM QUIZ")
        print ("2.ADD/DELETE QUESTIONS")
        print ("3.EXIT")
        choice = optionCheck(1,3)
        if choice == 1:
            print("starting in:",end="")
            time.sleep(0.25)
            print(" 3",end="")
            time.sleep(1)
            print(" 2",end="")
            time.sleep(1)
            print(" 1")
            time.sleep(1)
            print("######################################QUIZ",end="")
            print("######################################\n")
            play()
        elif choice == 2:
            editMenu()
        else:
            break
        
def play ():
    '''collects data from file and asks users 10 random questions'''
    quizlist = []
    score = 0
    count = 1
    
    qn = open("questions.txt","r")
    
    for line in qn:
        string = line.split("\t")
        quizlist.append(string)
    qn.close
    
    random.shuffle(quizlist)

    for count in range (10):
        qn=count+1
        print("Question #",qn,sep="")
        if len(quizlist[count])>1:#prevents blank line from being chosen
            question = quizlist[count]
            
        for i in range (5):
            print (question[i])
            time.sleep(1)
        time.sleep(1)
        userAnswer = userChoice("multi","your answer: ")
        answer = str(question [5])
        answer = answer.split() #needed as a space is mysteriously added to input
        if userAnswer == answer[0]:
            print ("correct!\n")
            
            score+=1
            time.sleep(.5)
        else:
            print ("incorrect!")
            print ("the correct answer is",answer[0],"\n")
            time.sleep(1)
    print ("you got ",score,"0%!",sep="")
    time.sleep(3)
def editMenu ():
    '''MENU TO ACCESS ADD/DELETE PROCEDURES'''
    while True:
        print ("\n\tEDITING MENU")
        print ("")
        print ("1.ADD A QUESTION")
        print ("2.DELETE A QUESTION")
        print ("3.EXIT")
        choice = optionCheck(1,3)
        if choice == 1:
            new_question()
        elif choice == 2:
            line=findLine ()
            line_delete(line)
        else:
            break

main()

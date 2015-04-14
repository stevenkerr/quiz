'''
File Name: add_delete.py
Made By: Steven Kerr
Date: 08/09 Apr 2015
Purpose: Add new question to list - delete question from list
FILES REQUIRED: user_choice.py
'''
import time
from userChoice import *
#ADDING QUESTION


'''
get question, check for \n, \t, etc, remove it add \t, add to new question
variable, get 4 choice answers, check for \n, \t, etc, remove if so, add \t,
add to new question variable
get answer, check for \n, \t, etc, remove it if so, add \t, add to new ques var

check if for sure user wants to add to list

open file, append new info, close file
'''


def file_append(filename, newline):
    '''
    takes in the new line, checks if user wants to add it,
    adds to file
    '''
    newques = newline
    
    while True:
        add = userChoice("yn", "are you sure you want to add this?")
        if add == False:
            break
        else:
            with open(filename, "a") as file:
                file.write(newques)
                file.close()
                break
        


def new_question(): 
    
    newquestion = input("Enter your new question: ")
    newquestion = newquestion + "\t"
    choice_a = input("Choice A): ")
    choice_a = "(A): " + choice_a + "\t"
    
    choice_b = input("Choice B): ")
    choice_b = "(B): " + choice_b + "\t"
    
    choice_c = input("Choice C): ")
    choice_c = "(C): " + choice_c + "\t"
    
    choice_d = input("Choice D): ")
    choice_d = "(D): " + choice_d + "\t"

    answer = userChoice("multi", "What is the correct answer?")
    answer = answer + "\n"
    
        
    time.sleep (0.5)
    print("processing",end="")
    time.sleep (0.5)
    print(".",end="")
    time.sleep (0.5)
    print(".",end="")
    time.sleep (0.5)
    print(".")
        
                       
    newline = newquestion + choice_a + choice_b + choice_c + choice_d + answer + "\n"
    
    file_append("questions.txt", newline) 
    print("question added!")




#DELETING QUESTION

'''
Purpose: delete a specific line within a list and determine if it is true
that the user wants to delete that line.

EXPECTATION: linedel is full string of line to be deleted, not position in list,
including \t's and \n's
'''

def line_delete(linedel):
    ''' determine deletion = true
        open and read file, get all info
        write to file all lines from last original file
        except the one to be deleted
    '''
    
    
    file = open("questions.txt", "r")
    fullfile = file.readlines()
    file.close

    file = open("questions.txt", "w")
    for line in fullfile:
        if line != linedel:
            file.write(line)



"""
# TEST CASES

if __name__ == '__main__':
                        
    '''line_delete test'''
    '''ONLY WORKS WITH ORIGINAL TEST FILE'''
    '''
    filenam = "testing123.txt"
    linetodel = "4\n"

    oldfile = open(filenam, "r")
    oldlines = oldfile.readlines()
    oldfile.close()

    print(oldlines)


    line_delete(filenam, linetodel)

    newfile = open(filenam, "r")
    newlines = newfile.readlines()
    newfile.close

    print(newlines)


    filenam = "testing123.txt"
    linetodel = "\t7\n"

    oldfile = open(filenam, "r")
    oldlines = oldfile.readlines()
    oldfile.close()

    print(oldlines)

    line_delete(filenam, linetodel)

    newfile = open(filenam, "r")
    newlines = newfile.readlines()
    newfile.close

    print(newlines)
    '''
    
    '''ADD LINES TEST'''

    new_question("testing123.txt")

    '''
    newfile = open("testing123.txt", "r")
    newlines = newfile.readlines()
    newfile.close()
    print (newlines)
    '''
"""

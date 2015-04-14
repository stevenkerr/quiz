'''
Made By: Steven Kerr
File Name: user_choice.py
Date: 08/09 Apr 2015
Purpose: Takes in question to be asked, if true false, initiates tf mode, else,
    begins multiple choice mode, clarifies user answer, returns answer

    EXPECTATION: question is list with choices included in list
    multiple choice mode must have 4 choices to select from 
'''
def userChoice(tf_multi_yn, question):


    if tf_multi_yn == "yn":
        while True:
            
            userPick = input(question)
            if userPick == "y" or userPick == "Y":
                return True
            
            elif userPick == "n" or userPick == "N":
                return False
            
            else:
                print ("Invalid Entry")

    elif tf_multi_yn == "tf":
        while True:
            
            userPick = input(question)
            if userPick == "t" or userPick == "T":
                choice = True
                return choice
            elif userPick == "f" or userPick == "F":
                choice = False
                return choice
            else:
                print ("Invalid Entry")

    
    elif tf_multi_yn == "multi":
        
        while True:
            choice = input(question)
            
            if choice == "a" or choice == "A":
                choice = "A"
                return choice
            elif choice == "b" or choice == "B":
                choice = "B"
                return choice
            elif choice == "c" or choice == "C":
                choice = "C"
                return choice
            elif choice == "d" or choice == "D":
                choice = "D"
                return choice
            else:
                print("Invalid Entry")


'''TEST CASES'''

if __name__ == '__main__':
    
    f = userChoice("yn", "Whats the right answer?")
    print (f)

    g = userChoice("tf", "true or false\n are you\t smart\t ?")
    print (g)

    h = userChoice("multi", "a b d or d?")
    print (h)

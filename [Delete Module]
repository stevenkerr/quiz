'''
File Name: linedelete.py
Made by: Steven Kerr (unless otherwise noted)
Date: 08 Apr 2015
Purpose: delete a specific line within a list and determine if it is true
that the user wants to delete that line.
'''

def line_delete(filename, linedel):
    ''' determine deletion = true
        open and read file, get all info
        write to file all lines from last original file
        except the one to be deleted
    '''
    
    while True:
        delete = check_pos_delete()
        if delete == False:
            break
        elif delete == True:
            file = open(filename, "r")
            fullfile = file.readlines()
            file.close

            file = open(filename, "w")
            for line in fullfile:
                if line != linedel:
                    file.write(line)
            break


def check_pos_delete():
    '''this function made by Kevin K.'''

    while True:
        print ("Do you want to delete this question? y/n:")
        choice = input("")
        if choice == "y" or choice == "Y":
            delete=True
            break
        elif choice == "n" or choice == "N":
            delete=False
            break
        else:
            print ("Please enter a valid choice.")

    return delete






'''line_delete test'''

filenam = "testing123.txt"
linetodel = "c\n"

oldfile = open(filenam, "r")
oldlines = oldfile.readlines()
oldfile.close()

print(oldlines)


line_delete(filenam, linetodel)

newfile = open(filenam, "r")
newlines = newfile.readlines()
newfile.close

print(newlines)
        

import os
import sys
from inspect import getsourcefile

nvarb = 'f'
i = ''

def nxtLine(nl):
    if nl[1] == 'P':
        a = [nl[0], nl[1], nl[3]]
        rdLine(a)
        

def rdLine(spaces):
    print(spaces[1])
    print(spaces[2])
    #print(spaces[3])
    if spaces[1] == "INT":
        if spaces[2] != None or spaces[2] !="":
            nvarb == 't'
            try:
                i == spaces[3]
                print(spaces[3])
                print(nvarb)
                print(i)
                ss = int(spaces[3])
                #print(ss)
                if isinstance(ss, int):
                    #print("INT " + spaces[2] + " " + spaces[3])
                    pass
                else:
                    print("Please enter a valid number")
            except:
                print("Please enter a valid number")
    else:
        if spaces[1] == 'P':
            print("test")

            print(i)

def interpreter(file):
    #print(os.path.dirname(getsourcefile(lambda:0)))
    f = open(file, "r+")
    count = sum(1 for _ in f)
    if count == 0:
        print("No commands in file " + file)
        sys.exit()
    # Open a file: file
    f = open(file ,mode='r')
 
    # read all lines at once
    all_of_it = f.read()
    spaces = all_of_it.split(" ")
    #print(spaces)
    rdLine(spaces)
    nl = all_of_it.split("\n")
    #print(nl)
    nxtLine(nl[1])
    
    #print(spaces[0])
    #print(spaces[1])
    #print(spaces[2])
    #print(spaces[3])

    


    # close the file
    f.close()

def langcheck(args):
    arrayargs = args.split(".")
    if arrayargs[-1] == "tlang":
        print("Decompiling")
        interpreter(args)
    else:
        print("Unknow language " + arrayargs[-1])


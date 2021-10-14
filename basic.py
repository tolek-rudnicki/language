import sys

def numOperation():
    a = input("Please separate numbers from the operation with spaces \n")
    b = a.split(" ")
    
    if b[1] == "+":
        print(int(b[0]) + int(b[2]))
    if b[1] == "-":
        print(int(b[0]) - int(b[2]))
    if b[1] == "*":
        print(int(b[0]) * int(b[2]))
    if b[1] == "/":
        if b[2] == "0":
            print("can't devide by zero!")
        else :
            print(int(b[0]) / int(b[2]))

def listen():
    cmd = input("basic > ")
    if cmd == "math":
        numOperation()
    else: 
        if cmd == "exit()":
            sys.exit()
    

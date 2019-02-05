# Logic Gate
# Aaron Poclington
# 5/2/2019

# imports
import time

# Main Code

def Main():

    logic = (input("Enter the logic gate type:\n>> ")).lower()
    input1 = input("Enter First input:\n>> ")
    input2 = input("Enter Second input:\n>> ")
    if (logic == "and"):
        if (input1 == "1" and input2 == "1"):
           print("Result: 1")
        else:
           print("Result: 0")
    if (logic == "or"):
        if (input1 == "0" and input2 == "0"):
            print("Result: 0")
        else:
            print("Result: 1")
    if (logic == "xor"):
        if ((input1 == "0" and input2 == "0") or (input1 == "1" and input2 == "1")):
            print("Result: 0")
        else:
            print("Result: 1")
    if (logic == "nand"):
        if ((input1 == "0" and input2 == "0") or (input1 == "1" and input2 == "0") or (input1 == "0" and input2 == "1")):
            print("Result: 1")
        else:
            print("Result: 0")
    if (logic == "nor"):
        if (input1 == "0" and input2 == "0"):
            print("Result: 1")
        else:
            print("Result: 0")


#Runs Main

if __name__ == "__main__":
    Main()

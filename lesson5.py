import math
secretNumber = 0
computerGuess = 50
low = 1
high = 100
guessCorrect = False
higher = False
invalid = True
median = 0
answer = "N"

secretNumber = input("Pick a number 1-100 ")

def findMedian():
    global low, high, computerGuess 
    if computerGuess == 2:
        return 1
    else:
        return math.ceil((low + high)/2)
    
def changeRange():
    global low, high, computerGuess
    if higher==True:
       low = computerGuess
    elif higher==False:
       high = computerGuess
    
if int(secretNumber) > 100 or int(secretNumber) < 1:
    print("Invalid Number.")
else:
    while guessCorrect==False:
        print(computerGuess) 
        answer = input("Is the number correct? Y or N ")
        if answer == "Y":
            print("Yeah I was correct!")
            guessCorrect = True
        else:
            higher = input("Is the number higher or lower? ")
            if higher == "higher":
                higher = True
                changeRange()
                computerGuess = findMedian()
                
            elif higher == "lower":
                higher = False 
                changeRange()
                computerGuess = findMedian() 
            else:
                higher = input("Is the number higher or lower? ")
                changeRange()
                computerGuess = findMedian()
            
        
        
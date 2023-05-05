import random

Right = False
AnswerGiven = 0
Number = random.randint(1,100)
Good = round(Number)
Tries = 0
Truth = str(Good)


while Right == False:

    AnswerGiven = input("Guess a random number from 1 to 100!")

    if AnswerGiven < Truth:
        
        Tries = Tries + 1
        print("Higher!")

    if AnswerGiven > Truth:

        print("Lower!")
        Tries = Tries + 1

    if AnswerGiven == Truth:

        Right == True
        Tries = Tries + 1
        print("Congratualations! You got it! The number was", Truth,"You guessed it in", Tries,"tries")
        break
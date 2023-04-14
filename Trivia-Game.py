import random
import time

questions = {
    "What is the capital of France?": "Paris",
    "Who invented the telephone?": "Alexander Graham Bell",
    "What is the largest continent by land area?": "Asia",
    "What is the smallest country in the world?": "Vatican City",
    "What is the highest mountain in the world?": "Mount Everest"
}

def play_game(questions):
    score = 0
    for question in questions:
        print(question)
        answer = input("Enter your answer: ")
        if answer.lower() == questions[question].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print("Game over. You scored", score, "out of", len(questions), "questions.")

import random
import time

while True:

    DieType = input("What kind of die do you want to roll? (4, 6, 8, 10, 12, 20 or 100)")

    if DieType == "4":
        Answer = random.randint(1, 4)
    
    if DieType == "6":
        Answer = random.randint(1, 6)

    if DieType == "8":
        Answer = random.randint(1, 8)

    if DieType == "10":
        Answer = random.randint(1, 10)

    if DieType == "12":
        Answer = random.randint(1, 12)

    if DieType == "20":
        Answer = random.randint(1, 20)

    if DieType == "100":
        Answer = random.randint(1, 100)

    print(Answer)
    Answer = 0
    time.sleep(1)

import time
import random

questions = ['No', 'Yes', 'Maybe', 'Doubtful', 'My sources say yes', 'My sources say no', 'Probably', 'Possible', 'Absolutely!', 'Absolutely not!']
random_item = random.choice(questions)

while True:
    
    random_item = random.choice(questions)
    question = input('Ask your question out loud')
    time.sleep(1)
    print(random_item)
    time.sleep(5)
    print('Ready to ask another question?')
    time.sleep(5)
import time
import random

questions = ['No', 'Yes', 'Maybe', 'Doubtful', 'My sources say yes', 'My sources say no', 'Probably', 'Possible', 'Absolutely!', 'Absolutely not!']
random_item = random.choice(questions)

while True:
    
    random_item = random.choice(questions)
    print('Ask your question out loud')
    time.sleep(7)
    print(random_item)
    time.sleep(4)
    print('Ready to ask another question?')
    time.sleep(4)
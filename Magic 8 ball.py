import time
import random

questions = ['No', 'Yes', 'Maybe', 'Doubtful', 'My sources say yes', 'My sources say no', 'Probably', 'Possible', 'Absolutely!', 'Absolutely not!']

while True:
    
    random_item = random.choice(questions)
    question = input('Write down your question.')
    print(question)
    time.sleep(1.5)
    print(random_item)
    time.sleep(1.5)
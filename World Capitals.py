print("Welcome to my world capitals quiz game!")
print("NOTE: if your spelling is incorrect, then it is considered as a wrong answer.")
print("Let's get started!")

score = 0
question_no = 0

playing = input('Do you want to play? ').lower()

if playing == 'yes':

    question_no += 1

    ques = input(f'\n{question_no}. What is the capital of Canada? ').lower()

    if ques == 'ottawa':

        score +=1
        print('correct! you got 1 point')
        
    else:

        print('Incorrect!')
        print(f'current answer is --> ottawa')

# ------1

    question_no += 1

    ques = input(f'\n{question_no}. What is the capital of the UK? ').lower()
    
    if ques == 'london':

        score +=1
        print('correct! you got 1 point')
        
    else:

        print('Incorrect!')
        print(f'current answer is --> london')

# -----2

    question_no += 1
    ques = input(f'\n{question_no}. What is the capital of Brazil? ').lower()
    
    if ques == 'brasilia':

        score +=1
        print('correct! you got 1 point')
        
    else:

        print('Incorrect!')
        print(f'current answer is --> brasilia')

# -----3

    question_no += 1
    ques = input(f'\n{question_no}. What is the capital of North Korea? ').lower()
    
    if ques == 'pyongyang':

        score +=1
        print('correct! you got 1 point')
        
    else:

        print('Incorrect!')
        print(f'current answer is --> pyonyang')


# -----4

    question_no += 1
    ques = input(f'\n{question_no}. What is the capital of Bulgaria? ').lower()
    
    if ques == 'sofia':

        score +=1
        print('correct! you got 1 point')
        
    else:

        print('Incorrect!')
        print(f'current answer is --> sofia')


# ------5 

    question_no += 1
    ques = input(f'\n{question_no}. What is the capital of Chile? ').lower()
    
    if ques == 'santiago':

        score +=1
        print('correct! you got 1 point')
        
    else:

        print('Incorrect!')
        print(f'current answer is --> santiago')


# ------6

 question_no += 1
    ques = input(f'\n{question_no}. What is the capital of Russia? ').lower()
    
    if ques == 'moscow':

        score +=1
        print('correct! you got 1 point')
        
    else:

        print('Incorrect!')
        print(f'current answer is --> moscow')


# ------7

else:

    print('So sad to see you go!')
    print('Have a nice day!')

    quit()

print(f'\nthe number of question is {question_no}')
print(f'your score is {score}')

try:
    percentage = (score *100)/question_no

except ZeroDivisionError:
    print('0% quetions are correct')

print(f'{percentage}% questions are correct.')

# Python quiz game

questions = ("What is the output of this code?:\n[print(2 + 2 * 3)]",
            "Which of the following is not a Python built-in data type?:",
            "What is the correct way to create an empty list in Python?:",
            "What is the output of the following code?: \n numbers = [1, 2, 3, 4, 5] \n print(numbers[2:4])",
            "Which of the following is the correct syntax for a for loop in Python?:")

options = (("A. 8", "B. 10", "C. 14", "D. 16"),
            ("A. List", "B. Tuple", "C. Set", "D. Array"),
            ("A. empty_list = []", "B. empty_list = list()", "C. empty_list = {}", "D. empty_list = list([])"),
            ("A. [3, 4]", "B. [1, 2, 3]", "C. [2, 3]", "D. [2, 3, 4]"),
            ("A. for i in range(10):", "B. for i = 0 to 10:", "C. for i from 0 to 10:", "D. for i in 10:"))

answers = ("C", "D", "A", "A", "A")
guesses = []
score = 0
question_num = 0

print('\t >>> WELCOME TO THE QUIZ <<<')
print(
    '''
                        88            
                        ""            
                                      
 ,adPPYb,d8 88       88 88 888888888  
a8"    `Y88 88       88 88      a8P"  
8b       88 88       88 88   ,d8P'    
"8a    ,d88 "8a,   ,a88 88 ,d8"       
 `"YbbdP'88  `"YbbdP'Y8 88 888888888  
         88                           
         88
    '''
)
for question in questions:
    print('--------------------')
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input('Enter (A, B, C, D): ').upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print('CORRECT!')
    else:
        print('INCORRECT!')
        print(f'The correct answer is {answers[question_num]}')
    question_num += 1
    
print('\t --------------------')
print('\t   >>> RESULTS <<<')
print('\t --------------------')
print('answers:', end="")
for answer in answers:
    print(answer, end=" ")
print()

print('guess:', end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score/len(questions) * 100)
print(f'Your score is {score}%')
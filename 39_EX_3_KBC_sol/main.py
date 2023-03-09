quizData = [
    {
        'question': 'Who developed Python Programming Language? ',
        'A':  'Wick van Rossum',
        'B': 'Rasmus Lerdorf',
        'C': 'Guido van Rossum',
        'D': 'Niene Stom',
        'correct': 'C'
    },
    {
        'question': 'Which type of Programming does Python support? ',
        'A':  'object-oriented programming',
        'B': 'structured programming',
        'C': 'functional programming',
        'D': 'all of the mentioned',
        'correct': 'D'
    },
    {
        'question': 'Which of the following is the correct extension of the Python file? ',
        'A':  '.python',
        'B': '.pl',
        'C': '.py',
        'D': '.p',
        'correct': 'C'
    },
    {
        'question': 'All keywords in Python are in _________ ',
        'A':  'Capitalized',
        'B': ' lower case',
        'C': 'UPPER CASE',
        'D': 'None of the mentioned',
        'correct': 'D'
    },
    {
        'question': 'Which of the following is used to define a block of code in Python language?',
        'A':  'Indentation',
        'B': 'Key',
        'C': 'Brackets',
        'D': 'All of the mentioned',
        'correct': 'A'
    },
]

score = 0
num = 0

while(num<5):
  for i in range(0,5):
    print(f"{i+1}:{quizData[i]['question']}")
    print(f"A:{quizData[i]['A']}")
    print(f"B:{quizData[i]['B']}")
    print(f"C:{quizData[i]['C']}")
    print(f"D:{quizData[i]['D']}")
    answer = input('Type your option in capitalcase(A,B,C,D) ')
    if(answer == quizData[i]['correct']):
      score =score + 1;
    
    print('\n')
    num=num+1

print(f'score:{score}/5')

if(score ) :
   print(f'{10000*score} is your total winning price')

      
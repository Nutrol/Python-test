import random



questions = {
    "That is the keyword to define a function in python?": "def",
    "Which data type is used to store True or False values?": "booleans",
    "What is the corect file extention for python files?": " .py",
    "Which symbol is used to comment in python?": "#",
    "What function is used to get input from the user?": "input",
    "How do you start a for loop in python?": "for",
    "What is the output of 2**3 in python?": "8",
    "What key word is used to import a module in python?": "import",
    "What,does the len() function return?": "length",
    "What is the result of 10//3 in python?": "3"
}

def python_test():
    question_list = list(questions.keys())
    total_questions = 5
    score = 0
    selected_questions = random.sample(question_list, total_questions)

    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input("Your answer: ").lower().strip() #strip removes spaces on user input
        correct_answer = questions[question]
        if user_answer == correct_answer.lower():
            print("correct 👌\n")
            score += 1
        else:
            print(f"Wrong😒, The correct answer is: {correct_answer}\n")

    print(f"Game over! Your final score is: {score}/{total_questions}")



python_test()

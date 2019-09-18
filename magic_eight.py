def question():
    question_asked = input("What is your question: ")
    print(question_asked)
    check_question(question_asked)

def check_question(question):
    if question.endswith('?'):
        print("WOO THATS A QUESTION")
    else:
        while True:
            new_input = input("I am sorry, I can only answer questions. ")
            if new_input == "quit":
                break

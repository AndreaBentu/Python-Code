# code that checks the user's answers againsta a text douments and prints how many correct answers the user gave.

questions = open('questions.txt', 'r')
print_question=questions.read().splitlines()
m=len(print_question)
n=0
for i in print_question:
    Question_is = i.partition("=")[0]
    Answer_is= i.partition("=")[2]
    user_Answer =  input (Question_is + '?')
    if user_Answer==Answer_is:
        n=n+1
print('You have '+ str(n) +'/' + str(m) +' good answers.')
questions.close()

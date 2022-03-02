import random

list_number_question=[0,1,2,3,4]

dict_question_and_answer = \
{
    "The capital city of the United Kingdom?": {
        "A": "London",
        "B": "Cardiff",
        "C": "Edinburgh",
        "D": "Belfast"
    },
    "What are the colors of the flag of the Spain": {
        "A": "Green and White",
        "B": "Black and Yellow",
        "C": "Red and Yellow",
        "D": "Blue and White"
    },
    "How many letters are there in the alphabet": {
        "A": "23",
        "B": "24",
        "C": "25",
        "D": "26"
    },
    "Below are the presidents of the USA, except?": {
        "A": "George W. Bush",
        "B": "Dustin Trudeau",
        "C": "Barack Obama",
        "D": "Donald Trump"
    },
    "What is the taste of a regular candy?": {
        "A": "Bitter",
        "B": "Spicy",
        "C": "Sour",
        "D": "Sweet"
    }
}

print("\nPython Multiple Choice Example\n=================================\n")
list_correct_answer = ['A', 'C', 'D', 'B', 'D']
score = 0

random.shuffle(list_number_question)

list_question = list(dict_question_and_answer)

for soal in list_question:

    index_question_asked =list_number_question.pop()
    print(list_question[index_question_asked])
    for choice, answer in dict_question_and_answer[list_question[index_question_asked]].items():
        print(choice, ":", answer)
    input_answer = str(input("\nanswer : "))
    print("--------------------------------------------")
    if input_answer.upper() == list_correct_answer[index_question_asked]:
        score = score + 1

print("Congratulations, your score : ",score)



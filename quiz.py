print("I will give you some questions You have to tell its correct answer . Your total marks are 6 :")

quiz_questions=[{"question" : "What is name of file?" , "answer": "quiz.py"},
{"question" : "What is name of folder?" , "answer": "day20"},
{"question" : "how many files of days?" , "answer": "22"}]

score=0

for q in  quiz_questions:
    answer= input(q["question"] + "").strip()

    if answer.lower() == q ["answer"] .lower():
        print("Correct")
        score=score+2
    else:
        print("Wrong . The correct answer is " , q["answer"])


print(f"Your final result is {score}")



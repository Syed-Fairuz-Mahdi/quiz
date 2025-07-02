questions= [("How many elements are there in a periodic table ?"),
            ("Which animal lays the largest egg ?"),
            ("What is the most abandunt gas in  Earth's atmosphere"),
            ("How many bones are in human body ?"),
            ("Which panet in the solar system is the hottest ?")]

options= [("A. 116","B. 117","C. 118","D. 119"),
          ("A. Crocodile","B. Elephant","C. Whale","D. Ostrich"),
          ("A. Nitrogen","B. Oxygen","C. Hydrogen","D. None"),
          ("A. 233","B. 206","C. 288","D. 205"),
          ("A. Earth","B. Mars","C. Venus","D. Mercury")]

answers= ("C","D","A","B","C")
guesses=[]
num=0
score=0

for question in questions:
    print("--------------------------------------------")
    print(question)             # print(questions[num]) is also correct
    for option in options[num]:
        print(option)

    while True:
        guess=input("Choose an option (A,B,C,D): ").upper()
        if guess in ("A","B","C","D"):
            pass
            break
        else:
            print(f"{guess} is not in the option")

    guesses.append(guess)
    if guesses[num]==answers[num]:       # "if guess==answers[num]  -is also correct
        print("Correct 🥳🥳🥳")
        score=score+1
    else:
        print("Wrong 😔😔😔")
        print(f"Correct answer is {answers[num]}")


    num+=1

print("----------------RESULT-------------------")
print(f"Your guesses {guesses}")
print(f"Answers      {answers}")
Total=(score/len(questions))*100
print(f"Your score is {Total}%")
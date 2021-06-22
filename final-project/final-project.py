#Ask the player name and store
player_name = input('What is your name?')

#This is a list made up of questions and answers dictionaries 
questions = [
        {"question": "What is the capital of Germany? ", 
        "answer": "Berlin"},
        {"question": "What is the capital of Spain? ", 
        "answer": "Madrid"},
        {"question": "What is the capital of Colombia? ", 
        "answer": "Bogota"}, 
        {"question": "What is the capital of England,UK? ", 
        "answer": "London"}
]

#Start with a scoor of 0
score = 0

#Loop through all the questions - a dictionary in a list
for question in questions: 
    player_ans = input(question["question"])
    if player_ans == question["answer"]:
        print("Correct!")
        score += 1
    else: 
            print("Incorrect")

    print(f"Your score was {score}")

#Print the final score
print(f"{player_name} Your final score was {score} out of 5")
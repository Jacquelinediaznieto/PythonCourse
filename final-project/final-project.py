#Ask tJhe player name and store
player_name = input('What is your name? ')


#This is a list made up of questions and answers dictionaries 
questions = [
        {"question": "What is the capital of Germany? ", 
        "answer": "berlin"},
        {"question": "What is the capital of Spain? ", 
        "answer": "madrid"},
        {"question": "What is the capital of Colombia? ", 
        "answer": "bogota"}, 
        {"question": "What is the capital of England,UK? ", 
        "answer": "london"}, 
        {"question": "What is the capital of Portugal? ", 
        "answer": "lisbon"}
]




#Welcome the player
print(f"Hello {player_name}, let's start. There are five questions. Good luck!")

def runquiz():
    #Start with a scoor of 0
    score = 0
    #Loop through all the questions - a dictionary in a list
    for question in questions: 
        player_ans = input(question["question"])
        player_ans_lower = player_ans.lower()
        if player_ans_lower == question["answer"]:
            print("Correct!")
            score += 1
        else: 
                print("Incorrect")

        print(f"Your score is {score}")

    #Print the final score
    print(f"{player_name} Your final score was {score} out of 5")

while True:
      
    runquiz()


    #Ask user if they want to play again? 
    play_again = input("Would you like to play again? y/n ")

    if play_again == "y":
        print("runs the function to play again")
    else:
        print("Thanks for playing, see you again soon")
        break
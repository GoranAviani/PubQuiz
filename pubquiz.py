
def main_menu():
    userCommand = input("\n\n       ***Wellcome to Pub Quiz MAIN MENU!***\n\n-------------------------------------------------------\n* If you want to add new questions to enter [N]\n* IF you want to list all questions and answers enter [L]"
                        "\n* If you want to start the new game enter [G]\n* Enter [X] to exit game*\n-------------------------------------------------------"
                        "\n\nYour command: ")
    return userCommand

quizQuestions = [
{
    "Question": "What is the name of capital of Sweden?",
    "a": "Oslo",
    "b": "Stockholm",
    "c": "Helsinki",
    "d": "Malmo",
    "answer": "b"
},
{
    "Question": "test?",
    "a": "test1",
    "b": "test2",
    "c": "test3",
    "d": "test4",
    "answer": "b"
}
]

def do_question():
    


def main():

    while True:
        userCommand = main_menu()

        #add new questions
        if userCommand.upper() == "N":
            print("adding new questions")

        elif userCommand.upper() == "L":
            print("listing all questions")

        elif userCommand.upper() == "X":
            print("Good bye!")
            break

            # start game
        elif userCommand.upper() == "G":
            do_question()

        else:
            print("I don't understand that command.")


if __name__ == '__main__':
    main()
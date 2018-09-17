import process_questions


def main_menu():
    userCommand = input("\n\n       ***Wellcome to Pub Quiz MAIN MENU!***\n\n-------------------------------------------------------\n* If you want to add new questions to enter [N]\n* IF you want to list all questions and answers enter [L]"
                        "\n* If you want to start the new game enter [G]\n* Enter [X] to exit game*\n-------------------------------------------------------"
                        "\n\nYour command: ")
    return userCommand



def load_from_file():
    quizQuestions = [
        {
            "id": 1,
            "category": 1,
            "Question": "What is the name of capital of Sweden?",
            "a": "Oslo",
            "b": "Stockholm",
            "c": "Helsinki",
            "d": "Malmo",
            "answer": "b"
        },
        {
            "id": 2,
            "category": 1,
            "Question": "test?",
            "a": "test1",
            "b": "test2",
            "c": "test3",
            "d": "test4",
            "answer": "b"
        },
        {
            "id": 3,
            "category": 2,
            "Question": "test2222?",
            "a": "test1",
            "b": "test2",
            "c": "test3",
            "d": "test4",
            "answer": "d"
        },
        {
            "id": 4,
            "category": 3,
            "Question": "test3333?",
            "a": "test1",
            "b": "test2",
            "c": "test3",
            "d": "test4",
            "answer": "c"
        }
    ]
    return quizQuestions




def choose_game_options(quizQuestions):
    #TODO categorese questions
    #option 1: how many guestions
    #option 2: what categories
    print("Game options. 2 questions. category 1. SKIP.")
    go_noOfQuestions = 2
    go_noOfCategory = [1, 2]


    process_questonsMessage, process_questonsStatus, gameQuestionsPreselectedFinal = process_questions.process_questions(quizQuestions, go_noOfQuestions, go_noOfCategory)

    print(process_questonsMessage)
    print(process_questonsStatus)
    print(gameQuestionsPreselectedFinal)

def main():
    quizQuestions = (load_from_file())

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
            choose_game_options(quizQuestions)


        else:
            print("I don't understand that command.")


if __name__ == '__main__':
    main()
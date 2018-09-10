
def main_menu():
    userCommand = input("\n\n       ***Wellcome to Pub Quiz MAIN MENU!***\n\n-------------------------------------------------------\n* If you want to add new questions to enter [N]\n* IF you want to list all questions and answers enter [L]"
                        "\n* If you want to start the new game enter [G]\n* Enter [X] to exit game*\n-------------------------------------------------------"
                        "\n\nYour command: ")
    return userCommand



def load_from_file():
    quizQuestions = [
        {
            "id": 1,
            "Question": "What is the name of capital of Sweden?",
            "a": "Oslo",
            "b": "Stockholm",
            "c": "Helsinki",
            "d": "Malmo",
            "answer": "b"
        },
        {
            "id": 2,
            "Question": "test?",
            "a": "test1",
            "b": "test2",
            "c": "test3",
            "d": "test4",
            "answer": "b"
        }
    ]
    return quizQuestions


def process_questions(quizQuestions):
    #idea is to process questions by number of needed questions for this quiz,
    #  and taht questions dont repeat in a single quiz (thats why id).
    #TODO categorise questions
    print("quiz questions are being processed..")
    pass

def choose_game_options(quizQuestions):
    #TODO categorese questions
    #option 1: how many guestions
    #option 2: what categories
    process_questions(quizQuestions)


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
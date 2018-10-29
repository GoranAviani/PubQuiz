import game_options
import load


def pub_quiz():
    quizQuestions = (load.load_from_file())


    while True:
        userCommand = input("\n\n       ***Wellcome to Pub Quiz MAIN MENU!***\n\n-------------------------------------------------------\n* If you want to add new questions to enter [N]\n* IF you want to list all questions and answers enter [L]"
                        "\n* If you want to start the new game enter [G]\n* Enter [X] to exit game*\n-------------------------------------------------------"
                        "\n\nYour command: ")
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
            game_options.choose_game_options(quizQuestions)


        else:
            print("I don't understand that command.")


if __name__ == '__main__':
    pub_quiz()
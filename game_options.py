import process_questions

def choose_game_options(quizQuestions):
    #TODO categorese questions
    #option 1: how many guestions
    #option 2: what categories

    # go_noOfQuestions = input("")
    go_selectableCategories = ["1","2","3","4","5","6","7","8"]
    go_noOfQuestions = 2
    go_noOfCategory = []

    while True:
        print("Type in a number of a category you want to play with, or type D when [D]one selecting:\n"
              "1 - History\n"
              "2 - Nature\n"
              "3 - Sport\n"
              "4 - Books\n"
              "6 - Movies\n"
              "7 - Medicine\n"
              "8 - Science\n")
        userInputCategory = input(" ")

        if userInputCategory.lower() == "d":
            for x in go_noOfCategory:
                print("You have selected {} category".format(x))
            print("Proceeding to game building... Please wait..\n")
            break
        elif userInputCategory in go_selectableCategories:
            print("it is ")
            go_noOfCategory.append(userInputCategory)
        else:
            print("That is not a known command")


    process_questonsMessage, process_questonsStatus, gameQuestionsPreselectedFinal = process_questions.process_questions(quizQuestions, go_noOfQuestions, go_noOfCategory)

    print(process_questonsMessage)
    print(process_questonsStatus)
    print(gameQuestionsPreselectedFinal)
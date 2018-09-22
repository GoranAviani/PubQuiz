import process_questions

def input_questions_category_and_numbers():
    userInputCategory = input("Type in a number of a category you want to play with, or type D when [D]one selecting.\n"
                              "Selectable categories:\n\n"
                              "1 - History, 2 - Nature, 3 - Sport,  4 - Books,  6 - Movies, 7 - Medicine,   8 - Science\n")
    userInputCategotyQuestNums = input(
        "Type in how many questions do you want to pick from category {}:".format(userInputCategory))

    return userInputCategory, userInputCategotyQuestNums

def choose_game_options(quizQuestions):
    #Hardcodes settings:
    go_selectableCategories = ["1", "2", "3", "4", "5", "6", "7", "8"]
    go_noOfQuestions = 2
    go_noOfCategory = []

    #TODO categorese questions
    #option 1: how many guestions
    #option 2: what categories

    # 3 TODO how many questions from every category
        #it would be best if ther was pre known number of questions from every category
    quizQuestions, numsOfQuestionsByCategory = process_questions.get_num_of_questions_by_category(quizQuestions)



    while True:
        userInputCategory, userInputCategotyQuestNums = input_questions_category_and_numbers()

        if userInputCategory.lower() == "d":
            print("-----------------------------------------------------------------------------------------------------\n")
            for x in go_noOfCategory:
                print("You have selected {} category".format(x))
            print("Proceeding to game building... Please wait..\n")
            print("-----------------------------------------------------------------------------------------------------\n")
            break
        elif userInputCategory in go_selectableCategories:
            if userInputCategory not in go_noOfCategory:
                print("You have sucesfully selected {0}".format(userInputCategory))
                go_noOfCategory.append(userInputCategory)
            else: #check that category is not already selected
                print("You cannot select category {}, because you have already selected it".format(userInputCategory))
        else:
            print("That is not a known command")


    process_questonsMessage, process_questonsStatus, gameQuestionsPreselectedFinal = process_questions.process_questions(quizQuestions, go_noOfQuestions, go_noOfCategory)

    print(process_questonsMessage)
    print(process_questonsStatus)
    print(gameQuestionsPreselectedFinal)
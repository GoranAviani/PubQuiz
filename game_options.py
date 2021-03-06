import process_questions

def input_questions_category_and_numbers(go_selectableCategories, selectedCategotyQuestionsbyNums, numsOfQuestionsByCategory):
    userInputCategotyNumsOfQustions = "0"

    while True:
        #TODO it would be good if the question number went down for the number of selected questions by the user
        print("\n\n----------------------------------------------------------------------------------\nTotal number of Questions By Category {}"
            "\n----------------------------------------------------------------------------------".format(numsOfQuestionsByCategory))

        userInputCategory = input("------------------------------------------------------------------------------------------------\n"
                                  "Type in a number of a category you want to play with, or type D when [D]one selecting.\n"
                                  "Selectable categories:\n\n"
                                  "1 - History, 2 - Nature, 3 - Sport,  4 - Books,  6 - Movies, 7 - Medicine,   8 - Science\n")

        if userInputCategory.lower() == "d":
            break

        if userInputCategory in numsOfQuestionsByCategory:

            if userInputCategory in go_selectableCategories:
                if userInputCategory not in selectedCategotyQuestionsbyNums:
                    userInputCategotyNumsOfQustions = input(
                        "Type in how many questions do you want to pick from category {}:".format(userInputCategory))

                    if userInputCategotyNumsOfQustions.lower() == "d":
                        break

                    if userInputCategotyNumsOfQustions.isdigit():
                        if int(userInputCategotyNumsOfQustions) <= numsOfQuestionsByCategory[userInputCategory]: #if the number of question does actually exist
                            #print('ok')
                            if userInputCategotyNumsOfQustions.isdigit():
                                selectedCategotyQuestionsbyNums[userInputCategory] = userInputCategotyNumsOfQustions
                                print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n"
                                      "You have sucesfully selected category {0} with {1} questions"
                                      "\n/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/".format(userInputCategory, userInputCategotyNumsOfQustions))
                        else:
                            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nThat category does not have that many quesions in it!\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                    else:
                        print("That is not a number")
                else:  # check that category is not already selected
                    print("You cannot select category {}, because you have already selected it".format(userInputCategory))
            else:
                print("That is not a selectable category.")
        else:
            print("That category does not exist! Try again.")

    return selectedCategotyQuestionsbyNums  # TODO treba checkat negdi koliko se kategorija vratilo i oda odg odgovarajuce


def choose_game_options(quizQuestions):
    #Hardcoded settings:
    go_selectableCategories = ["1", "2", "3", "4", "5", "6", "7", "8"]
    selectedCategotyQuestionsbyNums = {}


    #option 1: how many guestions
    number_of_questions = len(quizQuestions)
    #option 2: what categories
    quiz_categories = process_questions.process_category(quizQuestions)

        #it would be best if ther was pre known number of questions from every category
    numsOfQuestionsByCategory = process_questions.get_num_of_questions_by_category(quizQuestions)


    selectedCategotyQuestionsbyNums = input_questions_category_and_numbers(go_selectableCategories, selectedCategotyQuestionsbyNums, numsOfQuestionsByCategory)
    for k, v in selectedCategotyQuestionsbyNums.items():
        print("Selected category key {}".format(k))
        print("Selected number of questions value {}".format(v))


    # process_questonsMessage, process_questonsStatus, gameQuestionsPreselectedFinal = process_questions.process_questions(quizQuestions, selectedCategotyQuestionsbyNums)

   #print(process_questonsMessage)
    # print(process_questonsStatus)
    # print(gameQuestionsPreselectedFinal)
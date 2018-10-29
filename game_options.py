import process_questions

def input_questions_category_and_numbers(go_selectableCategories, selectedCategotyQuestionsbyNums, numsOfQuestionsByCategory):
    userInputCategotyNumsOfQustions = "0"

    while True:
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
                    #TODO need to check if its numeric input, and message if not
                    if userInputCategotyNumsOfQustions.lower() == "d":
                        break

                    if userInputCategotyNumsOfQustions.isdigit():
                        if int(userInputCategotyNumsOfQustions) <= numsOfQuestionsByCategory[userInputCategory]:
                            print('ok')
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

    #TODO categorese questions
    #option 1: how many guestions
    #option 2: what categories

    # 3 TODO how many questions from every category
        #it would be best if ther was pre known number of questions from every category
    numsOfQuestionsByCategory = process_questions.get_num_of_questions_by_category(quizQuestions)

    print("quizQuestions {}".format(quizQuestions)) #not needed to be printed
    print("numsOfQuestionsByCategory {}".format(numsOfQuestionsByCategory))


    selectedCategotyQuestionsbyNums = input_questions_category_and_numbers(go_selectableCategories, selectedCategotyQuestionsbyNums, numsOfQuestionsByCategory)
    for k, v in selectedCategotyQuestionsbyNums.items():
        print("category key {}".format(k))
        print("number of questions value {}".format(v))


    # process_questonsMessage, process_questonsStatus, gameQuestionsPreselectedFinal = process_questions.process_questions(quizQuestions, selectedCategotyQuestionsbyNums)

   # print(process_questonsMessage)
    # print(process_questonsStatus)
    # print(gameQuestionsPreselectedFinal)
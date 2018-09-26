import process_questions

def input_questions_category_and_numbers(go_selectableCategories, selectedCategotyQuestionsbyNums):
    userInputCategotyNumsOfQustions = "0"

    while True:
        userInputCategory = input("Type in a number of a category you want to play with, or type D when [D]one selecting.\n"
                                  "Selectable categories:\n\n"
                                  "1 - History, 2 - Nature, 3 - Sport,  4 - Books,  6 - Movies, 7 - Medicine,   8 - Science\n")

        if userInputCategory.lower() == "d":
            break
        elif userInputCategory in go_selectableCategories:
            if userInputCategory not in selectedCategotyQuestionsbyNums:
                userInputCategotyNumsOfQustions = input(
                    "Type in how many questions do you want to pick from category {}:".format(userInputCategory))
                #TODO need to check if its numeric input, and message if not
                if userInputCategotyNumsOfQustions.lower() == "d":
                    break
                elif userInputCategotyNumsOfQustions.isdigit():
                    print("i to jeeeeeeeeeeeeeeee" + userInputCategotyNumsOfQustions)
                    selectedCategotyQuestionsbyNums[userInputCategory] = userInputCategotyNumsOfQustions
                    print("You have sucesfully selected category {0} with {1} questions".format(userInputCategory, userInputCategotyNumsOfQustions))
                else:
                    print("That is not a number")
            else:  # check that category is not already selected
                print("You cannot select category {}, because you have already selected it".format(userInputCategory))
        else:
            print("That is not a selectable category.")


    return selectedCategotyQuestionsbyNums  # TODO treba checkat negdi koliko se kategorija vratilo i oda odg odgovarajuce


def choose_game_options(quizQuestions):
    #Hardcoded settings:
    go_selectableCategories = ["1", "2", "3", "4", "5", "6", "7", "8"]
    go_noOfQuestions = 1
    selectedCategotyQuestionsbyNums = {}

    #TODO categorese questions
    #option 1: how many guestions
    #option 2: what categories

    # 3 TODO how many questions from every category
        #it would be best if ther was pre known number of questions from every category
    quizQuestions, numsOfQuestionsByCategory = process_questions.get_num_of_questions_by_category(quizQuestions)




    selectedCategotyQuestionsbyNums = input_questions_category_and_numbers(go_selectableCategories, selectedCategotyQuestionsbyNums)
    for k, v in selectedCategotyQuestionsbyNums.items():
        print("key {}".format(k))
        print("value {}".format(v))

"""
        if userInputCategory.lower() == "d":
            print("-----------------------------------------------------------------------------------------------------\n")
            for x in go_noOfCategory:
                print("You have selected {} category".format(x))
            print("Proceeding to game building... Please wait..\n")
            print("-----------------------------------------------------------------------------------------------------\n")
            break
        else:
            print("That is not a known command")

"""
    #process_questonsMessage, process_questonsStatus, gameQuestionsPreselectedFinal = process_questions.process_questions(quizQuestions, go_noOfQuestions, go_noOfCategory)

    #print(process_questonsMessage)
    #print(process_questonsStatus)
    #print(gameQuestionsPreselectedFinal)
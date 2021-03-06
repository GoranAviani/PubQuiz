def get_num_of_questions_by_category(quizQuestions):
    numsOfQuestionsByCategory = {}

    for question in quizQuestions:
        if question["category"] not in numsOfQuestionsByCategory:
            numsOfQuestionsByCategory[question["category"]] = 1
        else:
            numsOfQuestionsByCategory[question["category"]] += 1
    return numsOfQuestionsByCategory


#TODO this is not used - still
def process_questions(quizQuestions, selectedCategotyQuestionsbyNums):
    #idea is to process questions by number of needed questions for this quiz,
    #  and taht questions dont repeat in a single quiz (thats why id).

    gameQuestionsCounter = 0
    gameQuestionsPreselectedIDs = []
    gameQuestionsPreselected = []
    gameQuestionsPreselectedFinal = []
    process_questionsMessage = "Error"
    process_questionsStatus = "Error"

    gameQuestionsSelected = []
    print("quiz questions are being processed..")

    #first get all questions of selected categories
    for question in quizQuestions:
        if question["category"] in go_noOfCategory:
            gameQuestionsPreselected.append(question)


    #TODO not needed as there is a chech fo that in
    #TODO here: if int(userInputCategotyNumsOfQustions) <= numsOfQuestionsByCategory[userInputCategory]: #if the number of question does actually exist
    #if there are no questions in selected categories
    if len(gameQuestionsPreselected) == 0:
        process_questonsMessage = "There were no questions in selected categories!"
        process_questonsStatus = "NO"
    else:
        for questionPreselected in gameQuestionsPreselected:
            # if num of selected questions is num of asked questions then end
            if gameQuestionsCounter == go_noOfQuestions:
                process_questonsMessage = "Questions succesfully selected!"
                process_questonsStatus = "YES"
                break
            else:
                if questionPreselected["id"] not in gameQuestionsPreselectedIDs: #make sure not to repeat questions, for future idea
                    gameQuestionsPreselectedFinal.append(questionPreselected)
                    gameQuestionsCounter += 1
                    gameQuestionsPreselectedIDs.append(questionPreselected["id"])
        #print(gameQuestionsPreselectedFinal)



    #if there are less questions selected in gameQuestionsPreselectedFinal than it was wanted
    #-send appropriate message about it and give questions that were found
    #TODO if there were less questions offer some questions from some other categories.
    if gameQuestionsCounter < go_noOfQuestions:
        process_questonsMessage = "Questions selected, but not in the number you wanted, there arent any more!"
        process_questonsStatus = "YES"


    return (process_questonsMessage, process_questonsStatus, gameQuestionsPreselectedFinal)

def process_category(quizQuestions):
    categories = []
    for question in quizQuestions:
        if question["category"] not in categories:
            categories.append(question["category"])
    return categories
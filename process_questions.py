def process_questions(quizQuestions, go_noOfQuestions, go_noOfCategory):
    #idea is to process questions by number of needed questions for this quiz,
    #  and taht questions dont repeat in a single quiz (thats why id).
    #TODO categorise questions, there can be more categories for 1 quiz

    gameQuestionsCounter = 0
    gameQuestionsPreselectedIDs = []
    gameQuestionsPreselected = []
    gameQuestionsPreselectedFinal = []
    process_questonsMessage = "Error"
    process_questonsStatus = "Error"
    print("quiz questions are being processed..")

    #first get all questions of selected categories
    for question in quizQuestions:
        if question["category"] in go_noOfCategory:
            gameQuestionsPreselected.append(question)

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
                if questionPreselected["id"] not in gameQuestionsPreselectedIDs: #make sure we dont repeat questions
                    gameQuestionsPreselectedFinal.append(questionPreselected)
                    gameQuestionsCounter += 1
                    gameQuestionsPreselectedIDs.append(questionPreselected["id"])
        #print(gameQuestionsPreselectedFinal)

    return (process_questonsMessage, process_questonsStatus, gameQuestionsPreselectedFinal  )
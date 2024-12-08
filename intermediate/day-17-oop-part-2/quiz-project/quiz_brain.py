class QuizBrain :

    def __init__(self, quizList):
        self.questionNumber = 0
        self.questionList = quizList
        self.score = 0

    def nextQuestion(self):
        currentQuestion = self.questionList[self.questionNumber] #The specific question based on the index (questionNumber), has text and answer.
        self.questionNumber += 1

        answer = input(f"Q.{self.questionNumber} : {currentQuestion.text} (True/False) : ")
        self.checkAnswer(answer.lower(), currentQuestion.answer.lower()) #for checking of answer

    def hasNextQuestion(self):
        return self.questionNumber < len(self.questionList) #Returns true if this expression is correct.

    def checkAnswer(self, input, answer):

        if input == answer :
            self.score += 1
            print("You got it right!")
            print(f"Current Score : {self.score}/{self.questionNumber}")
        else :
            print("That's wrong!")
            print(f"Current Score : {self.score}/{self.questionNumber}")

        print(f"The correct answer is : {answer}")
        print("\n")

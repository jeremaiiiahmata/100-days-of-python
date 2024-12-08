from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank = []

for question in question_data:
    newQuestion = Question(question["text"], question["answer"]) #Construct objects, passing the parameters of text and answers
    questionBank.append(newQuestion) #Appends it to the questionBank list

quiz = QuizBrain(questionBank) #Create a new Quizbrain object

while quiz.hasNextQuestion(): #Returns true if questions length is still greater than the current question number
    quiz.nextQuestion()

print("You have completed the quiz!")
print(f"Your final score is : {quiz.score}/{quiz.questionNumber}")




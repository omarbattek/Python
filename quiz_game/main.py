from question_model import Quastuion
from data import question_data
from quiz_brain import QuizBrain


quastion_bank = []
for q in question_data:
    quastion_text = q["text"]
    quastion_answer = q["answer"]
    new_quastion = Quastuion(quastion_text,quastion_answer)
    quastion_bank.append(new_quastion)

quiz = QuizBrain(quastion_bank)

while quiz.still_has_quastion():
    quiz.next_quastion()
print("You've completed the quiz")
print(f"You final score was {quiz.score}/{quiz.quastion_number}")
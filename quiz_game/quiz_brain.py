class QuizBrain:
    def __init__(self, quastion_list):
        self.quastion_number = 0
        self.quastion_list = quastion_list
        self.score = 0
    def still_has_quastion(self):
        return self.quastion_number < len(self.quastion_list)

    def next_quastion(self):
        current_quastion = self.quastion_list[self.quastion_number]
        self.quastion_number += 1
        user_answer = input(f"Q. {self.quastion_number}: {current_quastion.text} (True/False)")
        self.check_answer(user_answer, current_quastion.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.quastion_number}")
        print("")
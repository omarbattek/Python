import random
from logo import logo

def play(level):
  difficult = level
  result = False

  while not result and difficult > 0:
    print(f"You have {difficult} attempts remaining to guess the number.")
    guss_player = int(input("make a guss "))
    if guss_player == guss_num:
      result = True
      print(f"gussin number is {guss_num} You win")
    elif guss_player > guss_num:
      difficult -=1
      print("Too high")
      if difficult > 0:
        print("Guss again")
    else:
      difficult -=1
      print("Too Low")
      if difficult > 0:
        print("Guss again")
  if not result:
    print("You've run out of guesses, you lose.")

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
guss_num = random.randint(1,100)
select_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if select_level =="easy":
  play(10)
else:
  play(5)
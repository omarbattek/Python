from art import logo,vs
from game_data import data
import random


game_over = True
score = 0

while game_over:
  choice1 = random.choice(data)
  choice2 = random.choice(data)
  print(logo)
  if choice1 == choice2:
    continue
  if score !=  0:
    print(f"you are right, your score current {score}")
  print (f"Compare A : {choice1['name']},{choice1['description']}, from {choice1['country']}")
  print(vs)
  print(f"Against B : {choice2['name']},{choice2['description']}, from {choice2['country']}")

  result = input("Who has more followers? Type 'A' or 'B':").lower()

  follower1 = choice1['follower_count']
  follower2 = choice2['follower_count']
  if follower1 >= follower2 and result == 'a':
    score += 1

  elif  follower1 <= follower2 and result == 'b':
    score += 1

  else:

    print("sorry you are lose")
    break
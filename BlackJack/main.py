import random

paper = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def take_paper():
    taken_paper = random.choice(paper)
    return taken_paper


def result():
    paper_computer_sum = sum(paper_computer)
    paper_player_sum = sum(paper_player)

    if A in paper_computer and paper_computer_sum > 21:
        paper_computer_sum -= 10
    # if A in paper_player and paper_player_sum > 21:
    #   paper_player_sum -=10
    if paper_player_sum > 21:
        return "Your paper grater than 21 BUSS computer win "
    elif paper_computer_sum > 21:
        return "Computer paper is more than 21 BUSS you win"
    elif paper_player_sum > paper_computer_sum:
        return f"you total is {paper_player_sum} computer total {paper_computer_sum} You win maaaaan"
    elif paper_computer_sum > paper_player_sum:
        return f"you total is {paper_player_sum} computer total {paper_computer_sum} You Loss Man"
    else:
        return f"you total is {paper_player_sum} computer total {paper_computer_sum} Draw"


playing = input("if you want play game press 'y' to start or 'n' to cancel ").lower()
paper_player = []
paper_computer = []
A = 11
from art import logo

if playing == "y":
    print(logo)
while playing == "y":
    paper_player = [take_paper(), take_paper()]
    paper_computer = [take_paper(), take_paper()]
    print(f"your paper is {paper_player} and your total is {sum(paper_player)}")
    print(f"computer's one of paper is {paper_computer[0]} ")
    paper_computer_sum = sum(paper_computer)

    while paper_computer_sum < 17:
        paper_computer.append(take_paper())
        paper_computer_sum = sum(paper_computer)
    hit_stand = input("press 'h' to hit or press 's' to stand ")
    paper_player_sum = sum(paper_player)

    while hit_stand == "h" and paper_player_sum < 22:
        print()
        paper_player.append(take_paper())

        paper_player_sum = sum(paper_player)

        if A in paper_player and paper_player_sum > 21:
            index = paper_player.index(A)
            paper_player[index] = 1
            paper_player_sum = sum(paper_player)

        print(f"your paper is {paper_player} and your total is {sum(paper_player)}")

        if paper_player_sum < 22:
            hit_stand = input("press 'h' to hit or press 's' to stand ")



    print(result())
    playing = input("if you want play game press 'y' to start or 'n' to cancel ").lower()
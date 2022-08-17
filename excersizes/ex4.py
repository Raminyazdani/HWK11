import argparse
import random


def guess_game(start, end, test, score):
    guess = test
    while True:
        if start < guess < end:
            if guess == score:
                print("you won")
                return 0
            elif guess > score:
                print("your number is higher than the goal")
                return 1
            else:
                print("your number is lower than the goal")
                return 2
        else:
            print(f"number most between {start} and {end}")
            guess = input("number : ")


parser = argparse.ArgumentParser(description="python script for calculating averages")
parser.add_argument("-s", "--start", type=int, required=True, default=0)
parser.add_argument("-e", "--end", type=int, required=True, default=100)
parser.add_argument("-g", "--guess", type=int, required=True)

args = vars(parser.parse_args())
score = random.randint(args["start"], args["end"])
lives = 5

while lives >= 1:
    print(score)
    cond = guess_game(args["start"], args["end"], args["guess"], score)

    if cond == 0:
        break
    lives -= 1
    print("lives : ", lives)
    args["guess"] = int(input("your number : "))

if cond!=0:
    print("you lose")

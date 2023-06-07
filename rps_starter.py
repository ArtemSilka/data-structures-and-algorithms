from random import randint

#1
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

#2
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

#3
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1,3)

# Turn that random number into the computer's RPS move
if num == 1:
    comp_move = rock
    comp_value = "rock"
elif num == 2:
    comp_move = paper
    comp_value = "paper"
else:
    comp_move = scissors
    comp_value = "scissors"

# Ask a user to enter their move
your_move = input("enter your move: ").lower()

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
print("YOUR MOVE: ")

if your_move == "rock":
    print(rock)
elif your_move == "paper":
    print(paper)
elif your_move == "scissors":
    print(scissors)
else:
    print("Ops! Start over!")

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
print(f"""COMPUTER's MOVE: 
{comp_move}
""")

# Figure out who wins and print the result!
if comp_value == your_move:
    print("Draw!")
elif (comp_value == "rock" and your_move == "scissors") or (comp_value == "scissors" and your_move == "paper") or (comp_value == "paper" and your_move == "rock"):
    print("You lose!")
else:
    print("You win!")
import random
import collections

name = input("Enter your name: ")
print(f"Hello, {name}")
my_rating = 0
with open("rating.txt", "r") as rating:
    for r in rating:
        nr = r.split()
        if nr[0] == name:
            my_rating = int(nr[1])

avail_options = ("rock", "paper", "scissors")
chosen_options = input()
if len(chosen_options) > 0:
    avail_options = chosen_options.split(",")

options = dict()
for i in range(len(avail_options)):
    options[avail_options[i]] = i

win_arr = collections.deque([False if i <= len(avail_options) // 2 else True for i in range(len(avail_options))])
win_matrix = []
for o in range(len(options)):
    tmp = win_arr.copy()
    tmp.rotate(o)
    win_matrix.append(tmp)

print("Okay, let's start")

while True:
    user_input = input()
    if user_input == "!exit":
        print("Bye!")
        break
    elif user_input == "!rating":
        print(f"Your rating: {my_rating}")
        continue
    elif user_input not in avail_options:
        print("Invalid input")
        continue
    comp_input = random.choice(avail_options)
    c_option = options[comp_input]
    u_option = options[user_input]
    if win_matrix[c_option][u_option]:
        print(f"Sorry, but computer chose {comp_input}")
    elif win_matrix[u_option][c_option]:
        print(f"Well done. Computer chose {comp_input} and failed")
        my_rating += 100
    else:
        print(f"There is a draw ({comp_input})")
        my_rating += 50

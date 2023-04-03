import random
import getpass

# ZAD. 1

user_numbers = input("Insert numbers separated with ',' symbol: \n")

numbers_list = [int(number.strip()) for number in user_numbers.split(",")]

minIndex = 0
maxIndex = 1

if len(numbers_list) < 2:
    maxIndex = 0

for i in range(len(numbers_list)):
    if numbers_list[i] < numbers_list[minIndex]:
        minIndex = i
    elif numbers_list[i] > numbers_list[maxIndex]:
        maxIndex = i

print(f"MIN VALUE: {numbers_list[minIndex]}")
print(f"MAX VALUE: {numbers_list[maxIndex]}")

# ZAD. 2

polish_cities = [
    "Wroclaw",
    "Poznan",
    "Gdansk",
    "Krakow",
    "Zakopane",
    "Szczecin",
    "Lodz",
    "Bialystok",
    "Lublin",
    "Torun"
]

tour = []
for i in range(len(polish_cities)):
    tour.append(polish_cities.pop(random.randint(0, len(polish_cities) - 1)))

print(f"RANDOM TOUR: {tour}")

# ZAD. 3

rounds_quantity = int(input("INSERT NUMBER OF ROUNDS: "))
print("CHOOSE GAME MODE:")
game_mode = input("C -> COMPUTER | H -> HOT SEATS \n")

player1_name = input("PLAYER1 NAME: ")
player2_name = "COMPUTER"

if game_mode.upper() == "H" or game_mode.upper() == "HOT SEATS":
    player2_name = input("PLAYER2 NAME: ")

def choose_winner(name1, name2, choice1, choice2):
    choice1 = choice1.upper()
    choice2 = choice2.upper()

    if choice1 == "R" and choice2 == "R":
        return "draw"
    elif choice1 == "R" and choice2 == "P":
        return name2
    elif choice1 == "R" and choice2 == "S":
        return name1
    elif choice1 == "P" and choice2 == "R":
        return name1
    elif choice1 == "P" and choice2 == "P":
        return "draw"
    elif choice1 == "P" and choice2 == "S":
        return name2
    elif choice1 == "S" and choice2 == "R":
        return name2
    elif choice1 == "S" and choice2 == "P":
        return name1
    elif choice1 == "S" and choice2 == "S":
        return "draw"

round_counter = 1
match_history = {}

for i in range(rounds_quantity):
    print("R -> ROCK | P -> PAPER | S -> SCISSORS")
    player1_choice = getpass.getpass("PLAYER1 CHOICE: ")
    if game_mode.upper() == "C" or game_mode.upper() == "COMPUTER":
        rand_number = random.randrange(3)
        if rand_number == 0:
            player2_choice = "R"
        elif rand_number == 1:
            player2_choice = "P"
        elif rand_number == 2:
            player2_choice = "S"
    else:
        player2_choice = getpass.getpass("PLAYER2 CHOICE: ")

    match_history[round_counter] = {
        player1_name: player1_choice,
        player2_name: player2_choice,
        "winner": choose_winner(player1_name, player2_name, player1_choice, player2_choice)
    }
    round_counter += 1

player1_score = 0
player2_score = 0
for key in match_history:
    winner = match_history[key]["winner"]
    if winner == player1_name:
        player1_score += 1
    elif winner == player2_name:
        player2_score += 1

winner = "draw"
if player1_score > player2_score:
    winner = player1_name
elif player2_score > player1_score:
    winner = player2_name

print (f"\n THE WINNER IS: {winner} \n")
for key in match_history:
    print(f"ROUND {key}")
    print(f"{player1_name} -> {match_history[key][player1_name]}")
    print(f"{player2_name} -> {match_history[key][player2_name]}")
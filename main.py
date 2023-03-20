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

for i in range(int(rounds_quantity)):
    player1_choice = getpass.getpass("PLAYER1 CHOICE: ")
    player2_choice = getpass.getpass("PLAYER2 CHOICE: ")
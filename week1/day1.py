welcome = "Welcome to CodeNation"

def even_length(str):
     str_len = len(str)
     if str_len % 2 == 0:
         print(welcome)
         print("The amount of letters and spaces is even")
     else:
         print(welcome)
         print("The amount of letters and spaces not even")

even_length(welcome)


##################################

alphabet = [
    "a","b",
    "c","d",
    "e","f",
    "g","h",
    "i","j",
    "k","l",
    "m","n",
    "o","p",
    "q","r",
    "s","t",
    "u","v",
    "w","x",
    "y","z"
]

for letter in alphabet:
    print(letter)

number_choice = int(input("enter number here and you will be shown that letter "))-1
print(alphabet[number_choice])


##############################



import random as r
cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def print_board():
    print(f"|{cells[0]}|{cells[1]}|{cells[2]}|\n")
    print(f"|{cells[3]}|{cells[4]}|{cells[5]}|\n")
    print(f"|{cells[6]}|{cells[7]}|{cells[8]}|\n")


def make_move(p, c):
    while True:
        cell = int(input("Pick a cell 0-8\n"))
        if (cells[cell] == " "):
            cells[cell] = p
            break

    while True:
        cell = r.randint(0, 8)
        if (cells[cell] == " "):
            cells[cell] = c
            break


def check_for_three(c):
    if cells[0] == c and cells[1] == c and cells[2] == c:
        return True
    if cells[3] == c and cells[4] == c and cells[5] == c:
        return True
    if cells[6] == c and cells[7] == c and cells[8] == c:
        return True
    if cells[0] == c and cells[3] == c and cells[6] == c:
        return True
    if cells[1] == c and cells[4] == c and cells[7] == c:
        return True
    if cells[2] == c and cells[5] == c and cells[8] == c:
        return True
    if cells[0] == c and cells[4] == c and cells[8] == c:
        return True
    if cells[2] == c and cells[4] == c and cells[6] == c:
        return True
    return False


def game_end_check():
    if check_for_three("0") or check_for_three("X"):
        return True
    else:
        return False


def start_game():
    player = input("Choose 0 or X\n")
    if player == "0":
        cpu = "X"
    else:
        cpu = "0"
    print_board()
    while game_end_check() == False:
        make_move(player, cpu)
        print_board()

start_game()

#################################
int(54)
int(5.4)
int("54")

str(54)
str(5.4)
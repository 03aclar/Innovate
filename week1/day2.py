def add_up():
       num1 = input("what is the first number you'd like to add up? /n")
       num2 = input("what is the second number you'd like to add up? /n")

    try:
        if (num1 + num2).isnumeric():
            
    except:
        print("there is an error")







light = False

def light_switch():
    global: light
    if light:
        print("whoa! it's bright in here")
        light = False

    else:
        print("who turned out the lights")
        light = True

light_switch()
light_switch()

######################


# import random
# from models import User, add_up
# # from random import randint, choice, shuffle
# new_user = models.User("Jay", 30, "jay@jay.jay")

# num1 = random.randint(1, 50)

# result = models.add_up(2, 2)
# def example_func():
#     pass

greeting = "Hello World"
print(greeting)


def add_up(num1, num2):
    return num1 + num2


print(add_up(1, 2))

variable_one = None

if variable_one == True:
    print(variable_one)
else:
    print("nothing")

example_string = "   Once upon a midnight dreary...    "

# i want some functionality to strip the whitespace from my strings

# print(example_string.strip())

# example_string = example_string.replace("midnight", "sunshine")

# print(example_string)


variable_one = 10

variable_one = "cat"
print(variable_one)


def function_example():
    # do stuff
    pass


name = "Will"
age = 31
email = "will@will.com"
profession = "Developer / Instructor"
shoe_size = 10.5
hair_colour = "black"


email = "will.oc@googlemail.com"

print(email)

# num = 10

# result = num % 2

# print(result)

# if num % 2 == 0:
#     print("this is an even number")
# else:
#     print("this is an odd number")

# num2 = 10

# num2 *= 3

# num2 -= 4

# print(num2)

# x = input("What is the first number you would like to add?")
# y = input("What is the second number you would like to add?")

# x = int(x)
# y = int(y)
# print(add_up(x, y))

# music = "Death Metal"
# music_list = [
#     "Metal",
#     "Rock",
#     "Samba",
#     "Jazz"
# ]

# music_tuple = ("Rap", "Grindcore")

# if "Metal" in music_list or music == "Shoegaze":
#     print("Will is happy")
# elif music == "samba":
#     print("Peter's up and dancing!")
# elif music != "k-pop":
#     print("Everybody is happy")

# from models import var

# if var:
#     print(var)
# else:
#     print("empty")

# def function_one(name):
#     return f"hello {name}!"

# print(function_one("Brian"))

# def string_test(str1, str2):
#     return f"{str1} is my favourite book, and {str2} is my favourite film."    

# print(string_test("The Dark Tower", "Blues Brothers"))

# w_amount = 100
# account_num = 12345678

# def cash_withdrawal(amount, accnum):
#     print(f"Withdrawal {amount} from account {accnum}!")

# cash_withdrawal(w_amount, account_num)
# cash_withdrawal(300, 50449921)
# cash_withdrawal(30, 50449921)

# list_of_players = [
#     "Kane",
#     "Son",
#     "Emerson"
# ]

# first_entry = list_of_players.pop(0)

# list_of_players.append("Lloris")

# print(list_of_players)

# print(first_entry)

# for i in range(0, 10, 1):
#     print(i)

# for x in range(0, 21, 2):
#     print(x)

# for j in range(0, 31, 3):
#     print(j)

# from random import randint

# num = randint(0, 50)

# while num != 31:
#     num = randint(0, 50)
#     print(num)
# alphabet = [
#     "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" 
# ]

# def get_usernum():
#     usernum = input("Please choose a number between 1 & 26!")
#     usernum = int(usernum) - 1
#     # print(alphabet[usernum].upper())
#     print(alphabet[usernum])

# print(int(5.999999999))
# print(int("54"))

# print(float(54))
# print(float("54"))

# str1 = str(54)
# str2 = str(54)

# variable_one = bool("0")

# if variable_one:
#     print(f"this is truthy: {variable_one}")
# else:
#     print(f"This is falsy: {variable_one}")


# list_of_cards = [
#     "Jack",
#     "Queen",
#     "King",
# ]

# if "Ace" not in list_of_cards:
#     print("The Ace is missing")
# elif "2" not in list_of_cards and "3" not in list_of_cards:
#     print("The list has positive equity")

# if "ten" not in list_of_cards:
#     print("Ten is missing")
#     list_of_cards.append("Ten")
    
# if 4.0 == 4:
#     print("the same?")

# if type(4.0) != type(4):
#     print("not the same")
#     print(type(4.0))
#     print(type(4))

# if "4" in "404":
#     print("is in")

# def add_up():
#     num1 = input("What is the first number you'd like to add up? \n")
#     num2 = input("What is the second number you'd like to add up? \n")
    
#     try:
#         if (num1 + num2).isnumeric():
#             print(num1 + num2)
#     except:
#         print("There is an error somewhere!")
#     else:
#         print("This error is getting weird...")
#     finally:
#         print("It's over")
    
#     print(num1 + num2)

# add_up()

# print(" this is a \"quote\"! ")

# print( '''
# you can write anythign in here and its not interpreted!
# you can write anythign in here and its not interpreted!
# you can write anythign in here and its not interpreted!
# you can write anythign in here and its not interpreted!

# """""""""""
# def fucntion_name():
#     global scope \
# ''')

# lisrt_of_hats = [
#     1, 2, 3, "hat", 3, 4, True
# ]

# def show_num():
#     num = 13
#     return num 

# def add_num(x):
#     x = x % 3
#     print(x)

# add_num(show_num())

even_nums = [2, 4, 6, 8, 10] #! Mutable
odd_nums = (1, 3, 5, 7, 9)   #! Immutable

even_nums[-1] = "ten"

#? odd_nums[-1] = "nine" --> Throws an error.

array_example = [1, 2, 6, 7, 8, 4]
final_score = []
for num in odd_nums:
    final_score.append(num)

for i in final_score:
    print(i)



# print(type((3, 4)))

# # class Tuple():
# #     #constructor

# #     #methods

# print(type([3, 4]))

# class List():
#     #constructor

#     #method - append

#     #method2 #.pop

############################################


def program():
    user_input = input("please enter number")
    try:
        user_input = int(user_input)
        print(f"{user_input}",type(user_input))
    
    except:
        print("try again")
        program()

program()


#########################################

from random import randint as r
​
ghost_chars = [
    'Peter Venkman', 'Raymond Stantz', 'Egon Spengler',
    'Winston Zeddemore', 'Dana Barrett', 'Lenny Clotch',
    'Janine Melnitz', 'Louis Tully', 'Walter Peck',
    'Joanne Phillips', 'Sammy Kipper', 'George Washington',
    'Frank Joslin', 'Meryl Campbell', 'John Plisken',
    'John Conner', 'Kyle Reece', 'Sarah Connor'
]
hscore = 0
​
def ghost_game(char_list):
    p_lives = 3
    p_score = 0
    print('You have 3 lives, would you like to begin? Press enter to continue')
    input()
    while p_lives > 0:
        question = r(0, 17)
        pressed_question = char_list[question]
        print(f'is {pressed_question} in the Ghostbusters film? [Y/N]\n')
        user_answer = input()
        if question <= 8:
            match user_answer.capitalize():
                case 'Y' | "YES":
                    print(f'{pressed_question} is indeed a charater in the movie!')
                    p_score += 1
                case 'N' | "NO":
                    print(f'{pressed_question} is not a charater in the movie!')
                    p_lives -= 1
        else:
            match user_answer.capitalize():
                case 'Y' | "YES":
                    print(f'{pressed_question} is not a charater in the movie!')
                    p_lives -= 1
                case 'N' | "NO":
                    print(f'{pressed_question} is indeed a charater in the movie!')
                    p_score += 1
    print('You have run out of lives! GAME OVER!!!!')
    return p_score
​
    while True:

        score = ghost_game(ghost_chars)
    if score > hscore:
        print(f'New High Score!! {score} Points!')
        hscore = score
    else:
        print(f'High Score remains at {previous_score} Points!')
    p_continue = input('Play again? Y | N')
    match p_continue.capitalize():
        
        case 'Y' | 'N':
            print('Starting a new game')
        case 'N' | 'NO':
            print('Have a good day!')
    break
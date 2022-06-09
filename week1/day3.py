weapons_sword = {
    'name' : 'Short Sword',
    'length' : 5,
    'damage' : 10,
    'weight' : 10.5,
    'value' : 500
}

weapons_spear = {
    'name' : 'Spear',
    'length' : 15,
    'damage' : 15,
    'weight' : 15.0,
    'value' : 1500
}

def player_inspect(item:dict):
    print('#######################')
    for x in item:
        print(f'|{x :6} > {item[x]:12}|')
    print('#######################')

def item_select():
    pcontinue = True
    while pcontinue == True: 
        pchoice = input('Please choose (1)sword or (2)spear: ')
        match pchoice.capitalize():
            case '1':
                player_inspect(weapons_sword)
            case '2': 
                player_inspect(weapons_spear)
            case _: 
                print(f'{pchoice} Not found try again')
        pchoice = input('Select another item? Y/N')
        match pchoice.capitalize():
            case 'Y' | 'YES': pcontinue = True
            case 'N' | 'NO': pcontinue = False
            case _: print(f'{pchoice} Not found returning to item select...')

item_select()
########################

cat_1 = [
    "Salem", "Black", "Moody"
]

cat_2 = {
    "name":"Azrael", "colour":"tabby", "mood":"playful"
}

cat_2["colour"] = "grey"

# dict_of_players = {
#     1:"Will", 
#     2:"Jay", 
#     3:"Jakub", 
#     "Four": True
# }
# print(cat_1[0])

name = cat_2["name"]

print(f"My cat is called {name}")

print("MY cat is " + cat_2["colour"] + " and he is very " + cat_2["mood"] + "!")

# for x in cat_2.items():
#     print(x)

# for x in cat_2.keys():
#     print(x)

# for x in cat_2.values():
#     print(x)

complex_dict = {
    "one" : {
        "name": "Will",
        "age": 31,
        "instructor": True,
        "course?" : {
            "courses": "Innovate",
            "available": "No"
        }
    },
    "two" : {
        "name": "Jay",
        "age": 30,
        "instructor": True
    },
    "three" : {
        "name": "Keira",
        "age": 30,
        "instructor": True
    },
    "four" :{
        "name": "Liam",
        "age": 30,
        "instructor": False
    }
}

# print("Will's availablity is: " + complex_dict["one"]["course?"]["available"])

# if complex_dict["one"]["name"] == "Will":
#     complex_dict["one"]["course?"]["available"] = "Yes"

# print("Will's availablity is: " + complex_dict["one"]["course?"]["available"])

print(list(complex_dict.get("one").items()))

complex_dict["one"]["name"] = "Brian"

print(list(complex_dict.get("one").values()))

example_dict = {
    "one":1,
    "two":2,
    "three":3
}

popped_entry = example_dict.pop("one")

print(popped_entry)

del example_dict["three"]

print(example_dict)
################################################
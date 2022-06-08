weapons_sword = {
    'name' : 'Short Sword',
    'length' : 5,
    'damage' : 10,
    'weight' : 10.5,
    'value' : 500
}
​
weapons_spear = {
    'name' : 'Spear',
    'length' : 15,
    'damage' : 15,
    'weight' : 15.0,
    'value' : 1500
}
​
def player_inspect(item:dict):
    print('#######################')
    for x in item:
        print(f'|{x :6} > {item[x]:12}|')
    print('#######################')
​
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
​
item_select()
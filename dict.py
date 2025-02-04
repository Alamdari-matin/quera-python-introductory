my_dic = {
    '1 En' : 'One',
    '1 Fr' : 'Un',
    '2 En' : 'Two',
    '2 Fr' : 'Deux',
    '3 En' : 'Three',
    '3 Fr' : 'Trois',
    '4 En' : 'Four',
    '4 Fr' : 'Quatre',
    '5 En' : 'Five',
    '5 Fr' : 'Cinq',
}

while True :
    x = input()
    if x == 'End' :
        break
    else :
        print(my_dic.get(x,))
#Создайте программу для игры с конфетами человек против человека.Условие задачи:
# На столе лежит 2021(или сколько вы скажете) конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28(или сколько вы зададите в начале)
# конфет. Все конфеты оппонента достаются сделавшему последний ход. Сделайте эту игру.
from random import randint

candy= int(input('Введите количество конфет для игры: '))
max_step=int(input('Максимальное число конфет за один ход: '))

def step(name, candy, max_step):
    
    correct=False
    while not correct:
        take=int(input(f'Сколько конфет возьмем {name}? '))
        if take<=max_step and take>0 and take<=candy:
            candy=candy-take
            print(f'Осталось {candy} конфет')
            correct=True
        else: print('Неверное количество конфет')
    return candy

def check_winner(candy, flag_step,first_name,second_name):
    if candy == 0:
        return first_name if flag_step % 2 == 0 else second_name
    else:
        return False

def play():
    global candy
    global max_step
    first_player = input('Введите имя первого игрока: ')
    second_player = input('Введите имя второго игрока: ')
    count_for_check_win = candy // max_step
    flag_step = randint(0, 1)
    win = False
    while not win:
        if flag_step % 2 == 0:
            candy = step(first_player, candy, max_step)
        else:
            candy = step(second_player, candy, max_step)
        if flag_step>= count_for_check_win - 1:
            temp = check_winner(candy, flag_step, first_player, second_player)
            if temp:
                print(f'{temp} выиграл(а)')
                win = True
        flag_step += 1


    
play()
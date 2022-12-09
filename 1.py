# Создайте программу для игры в ""Крестики-нолики"".
x = 'X'
o = 'O'
field = [[' ', ' ', ' '] for i in range(3)]
for line in field:
    print(line)
print('Игра крестики-нолики.Первый ход крестиком:')


def steps(field, sign):
    row, col = map(int, input(
        f'Куда бы вы хотели сходить {sign}? Введите позицию- 2 числа через пробел (от 0 до 2):\n ').split())
    corret_action = False
    while not corret_action:
        corret_action = True
        while col < 0 or col > 2 or row < 0 or row > 2 or field[row][col] == 'X' or field[row][col] == 'O':
            corret_action = False
            print('Неверный ввод. Попробуйте еще раз.')
            row, col = map(int, input(
                f'Куда бы вы хотели сходить {sign}? Введите позицию- 2 числа через пробел (от 0 до 2):\n ').split())
    field[row][col] = sign
    for line in field:
        print(line)
    return field


def check_winner(field, sign):
    win = False
    for i in range(0, 3):
        if field[i].count(sign) == 3:
            win = True
            break
        same_count = 0
        for j in range(0, 3):
            if field[j][i] == sign:
                same_count += 1
        if same_count == 3:
            win = True

    if field[0][0].count(sign) and field[1][1].count(sign) and field[2][2].count(sign):
        win = True
    if field[0][2].count(sign) and field[1][1].count(sign) and field[2][0].count(sign):
        win = True

    return win


stop = False
while not stop:
    steps(field, x)
    if check_winner(field, x):
        print(f'УРА! Победил {x}')
        stop = True
        break
    steps(field, o)
    if check_winner(field, o):
        print(f'УРА! Победа {o}')
        stop = True
        break
    empty_cells = sum(line.count(' ') for line in field)
    if empty_cells == 0:
        stop = True
        print('Ничья')

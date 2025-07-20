def my_number(n):
    steps = all_numbers(n)
    for _ in range(1, 8):
        if same_digits(n):
            print("Число не сводится к 6174:(")
            break
        n = next_number(n, True)
        if n == 6174:
            print(f"\nКоличество шагов: {steps}")
            break
        
def next_number(nb, debug):
    currect = nb
    mn1 = list(str(currect).zfill(4))
    mnub = int(''.join(map(str, sorted(mn1, reverse=True))))
    mnvz = int(''.join(map(str, sorted(mn1))))
    currect = mnub - mnvz
    if debug:
        print(f"{mnub} - {mnvz} = {currect}")
    return currect
        
def all_numbers(n):
    crrct = n
    trying = 0
    while crrct != 6174:
        if same_digits(n):
            return trying
            break1
        trying += 1
        crrct = next_number(crrct, False)
    return trying
        
def same_digits(n):
    return len(set(str(n))) == 1

stat = {}
        
while True:
    print("\n\nВыберите режим 'Постоянной Капрекары':")
    print("'1' - если Вы хотите проверить своё число.")
    print("'2' - если Вы хотите посмотреть статистку всех чисел (1000 до 9999)")
    myanswer = input()
    if myanswer == '1':
        print('Отлично, введите своё четырёхзначное число (1000-9999).')
        try:
            mynumber = int(input())
            if 1000 <= mynumber <= 9999:
                my_number(mynumber)
                continue
            else:
                print('Ошибка! Нужно ввести четырёхзначное число (1000-9999)!')
                continue
        except ValueError:
            print('Это не число! Хе-хе')
            continue
    elif myanswer == '2':
        for i in range(1000, 10000):
            trying = 0
            if same_digits(i):
                if trying in stat:
                    stat[trying] += 1
                    continue
                else:
                    stat[trying] = 1
                    continue
            crct = all_numbers(i)
            if crct in stat:
                stat[crct] += 1
            else:
                stat[crct] = 1
                continue
        for z in sorted(stat):
            print(f"[{z}] Кол-во чисел, у которых {z} итераций - {stat[z]}")
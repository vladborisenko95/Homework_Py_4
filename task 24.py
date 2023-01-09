# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

from random import randint
def picking_berries(number_of_bushes):

    bushes = list(randint(1 ,10) for i in range(number_of_bushes))
    print(f'Грядка с ягодами:\n'
          f'{bushes}')
    max_summ = 0

    for i in range(number_of_bushes-1):

        if max_summ < sum(bushes[i:i+3]):
            max_summ = sum(bushes[i:i+3])
            bush = i+1

    if max_summ < sum(bushes[number_of_bushes-2:]) + bushes[0]:
        print(f'Для максимального сбора ягод, модулю нужно остановиться у куста под номером: {number_of_bushes}')
        print(f'Максимальное количество собранных ягод: {max_summ}')
    elif max_summ < sum(bushes[0:2]) + bushes[number_of_bushes-1]:
        print('Для максимального сбора ягод, модулю нужно остановиться у куста под номером: 1')
        print(f'Максимальное количество собранных ягод: {max_summ}')
    else:
        print(f'Для максимального сбора ягод, модулю нужно остановиться у куста под номером: {bush+1}')
        print(f'Максимальное количество собранных ягод: {max_summ}')

picking_berries(int(input('Введите кол-во кустов на грядке: ')))
num = 3

if num>=0:
    print("Число больше или равно 0")
else:
    print("Число отрицательное")

def task_yes_no(str_1, str_2):
    if str_1 in str_2:
        print("Да")
    else:
        print("Нет")

task_yes_no(str_1='test',str_2='test1')

num_float = 3.4

if num_float>0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')

Permit_print = True

if num>0 and Permit_print:
    print('num - положительное число')
elif not Permit_print:
    print('Печать запрещена')


def student_rank(year):
    if year ==1 or year == 2 or year == 3 or year == 4:
        print('Бакалавр')
    elif year in range(5,7):
        print("Магистр")
    elif 7<= year <=9:
        print("Аспирант")
    else:
        print("Введите корректный год обучения")

student_rank(10)


a = 5

if a>100 or a<-100:
    print('-')
else:
    print('+')


def hw_3_1(a: int, b: int) ->None:
    if a>b:
        print(a)
    else:
        print(b)
hw_3_1(1,3)


def hw_3_2(a: int,b: int) ->None:
    if a-b==135 or a-b==-135:
        print("yes")
    else:
        print("No")
hw_3_2(3,134)

def hw_3_3(a:int) ->None:
    if a in [1,2,12]:
        print('Зима')
    elif a in [3,4,5]:
        print('Весна')
    elif a in [6,7,8]:
        print ('Лето')
    elif a in [9,10,11]:
        print('Осень')
    else:
        print('Ты ошибся, проверь еще раз')

hw_3_3(3)

def hw_3_4(a:int, b:int, c:int) ->None:
    if a>10 and b>10 and c>10:
        print('Yes')
    else:
        print('No')

hw_3_4(11,13,11)


def hw_3_5(numbers:list) ->None:
    a:int = 0
    for number in numbers:
        if number>0:
            a=a+1
    print(a)
b:list = [-3,1.2,-1.2,2,145]

hw_3_5(b)

def hw_3_6(years:int, month:int) -> None:
    days:int = years * 365 + month * 29
    print(days)

hw_3_6(1,3)
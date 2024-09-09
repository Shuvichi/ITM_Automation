def task_1() ->None:
    a: int = 1
    b: float = 1.3
    c: str = "Nastya"
    d: list = [1, 2, 3, "four"]
    e: bool = False

    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))

task_1()

def task_2() ->None:
    a=[1,2,3,5,8,13,21]
    print(a[0:3])
    print('Это числа Фибаначи')

task_2()

def task_3(number: int) -> int:
    return number * number
print(task_3(3))

def test_passing():
    assert (1,2,3) == (1,2,3)

#
# def test_file():
#     assert 'test' == 'testing'

#Функция для проферки несоотвествия
def test_note():
    a = 'test'
    b = 'testing'
    assert not a == b


def test_1():
    x = ["a","b","c"]
    y = [1,2,3]
    assert not x == y

import pytest


@pytest.fixture(scope='session', autouse=True) #autouse=True - выполняется автоматически. 
#scope='session' - выполняется один раз для всех тестов
def before_all_tests(): #сюда как аргумент передается функции в которых используется эта фикстур
    print('before all tests') #выводится в консоль
    yield #выполняется тест и далее продолжается выполнение кода
    print('after all tests')

@pytest.fixture(scope='function') #scope='function' - выполняется для каждого теста
def before_after_each_test():
    print('test started')
    yield #возвращается в тест
    print('test finished')


@pytest.mark.simple #маркировка теста simple
def test_one(before_after_each_test):
    assert 4 == 4

@pytest.mark.simple #маркировка теста simple
def test_two(before_after_each_test):
    assert 5%2 == 1

@pytest.mark.simple     
def test_three(before_after_each_test):
    assert 1 > 0.5

@pytest.mark.simple
@pytest.mark.skip(reason='Skipping test') #пропускается тест и пишется причина пропуска
def test_four(before_after_each_test):
    assert 100 == 100

@pytest.mark.simple
def test_five(before_after_each_test):
    assert 100 != 101

@pytest.mark.simple
def test_six(before_after_each_test):
    text = 'I lova python'
    assert 'I' in text 

@pytest.mark.hard
def test_seven(before_after_each_test):
    text2 = 'I lova python'
    assert 'I lova python' is text2

@pytest.mark.hard
def test_eight(before_after_each_test):
    assert len('I lova python') == 16

@pytest.mark.hard
def test_nine(before_after_each_test):
    assert len('I lova python') < 10

@pytest.mark.simple
def test_ten(before_after_each_test):
    assert 100 > 101

@pytest.mark.hard
@pytest.mark.parametrize('a, b, c, d, e', 
[(1, 2, 3, 4, 5),
(-1, -2, -3, -4, -5),
(1.1, 2.2, 3.3, 4.4, 5.5),
(24, 56, 98, 14, 98),
(0, 0, 0, 0, 0)]) 
#Первый объект = переменная(ые) которые передаем в тест
#Второй объект = значения которые эти переменные принимают
#Переменных может быть много, но объектов всегда 2
#Количество значений в кортеже = количество переменных
def test_ymnozenie(a, b, c, d, e): #как аргумент передаются именно переменные
    assert a*b*c*d*e < 10000 #а уже в коде импользуются и меняются наши значения

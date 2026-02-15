import requests
import pytest
import allure

@pytest.fixture(scope='function')# отработает только в рамках одной функции (предусловия и постусловия)
def new_post_id():
    body = {
        "title": "еуыеуеыуе",
        "body": "hello",
        "userId": 1
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://jsonplaceholder.typicode.com/posts', 
        json = body,
        headers = headers
        )
    post_id = response.json()['id']
    yield post_id
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')

@pytest.fixture(scope='session')# отработает в всех задачах откуда запущена фикстура (предусловия до первой функции, постусловия после последней функции)
def hi():
    print('hello')
    yield
    print('bye')


#------------------------------------------------------------------------------------------------------------------------
@allure.feature('Posts') # более общее понятие, в которое входит сторис 
@allure.story('Get posts')
def test_get_one_post(new_post_id):
    with allure.step('Run get request'): # добавляем шаги для аллюра, в отчете аллюра будет видно на каком шаге тест упал 
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()
    with allure.step('Check response'):
        assert response['id'] == new_post_id

@allure.feature('Posts')
@allure.story('Get posts')
def test_get_all_post(hi):
    with allure.step('Run get request'):
        response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    with allure.step('Check equal'):
        assert len(response) == 100


@allure.feature('Posts')
@allure.story('Create posts')
def test_add_post():
    with allure.step('Prepare test data'):
        body = {
            "title": "еуыеуеыуе",
            "body": "hello",
            "userId": 1
        }
        headers = {'Content-Type': 'application/json'}
    with allure.step('Send request'):
        response = requests.post('https://jsonplaceholder.typicode.com/posts', 
            json = body,
            headers = headers
            )
    with allure.step('Check equal'):
        assert response.status_code == 201
    with allure.step('Check equal'):
        assert response.json()['id'] == 101


@allure.feature('Example')
@allure.story('Equal')
@pytest.mark.smoke # описали что это смок тест и его можно щапустить отдельно 
def test_simple_1():
    with allure.step('Check equal'):
        assert 1 + 1 == 2

@allure.feature('Example')
@allure.story('Equal')
@pytest.mark.regression # описали что это регресс тест и его можно запустить отдельно 
def test_simple_2():
    assert 5 * 2 == 10

@allure.feature('Example')
@allure.story('Some data')
@pytest.mark.parametrize('login', ['', '  ', '%@%@#%@']) # вроде как задаем в какое поле вводить какие данные и сколько 'данных' передано - столько раз тест и запустится 
def test_simple_3(login):
    print(login)
    assert 20 - 10 == 10 
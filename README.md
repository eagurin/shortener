# Бэкенд для веб-сервиса сокращения ссылок
[![Django-app workflow](https://github.com/eagurin/shortener/actions/workflows/main.yml/badge.svg)](https://github.com/eagurin/shortener/actions/workflows/main.yml)



Сокращение ссылки - формирование короткой ссылки, по которой будет осуществлен переход на исходную ссылку. Сервис должен уметь сократить исходную ссылку (то есть сопоставить этой ссылке уникальную сокращенную) и по сокращенной ссылке восстановить исходную и перейти по ней.
Считаем, что домен у сайта может быть любой, и что он задается в виде аргумента при запуске сервера. Например:
## Установка переменных окружения
```sh
DEBUG=True  # Для запуска в режиме Debug
BASE_URL=http://goo.gl/  # Ваш домен. По умолчанию http://localhost:8000/ 
```
Клонирование репозитория:
```sh
git clone https://github.com/eagurin/shortener.git
cd shortener/
````
Зайдите в репо и создайте и активируйте виртуальную среду:
```sh
python -m venv env
source env/bin/activate
```
Установите используемые пакеты:
```sh
pip install -r requirements.txt
```
Установите миграции:
```sh
python manage.py makemigrations
python manage.py migrate
```
Запуск репо локально:
Чтобы увидеть демонстрацию, запустите облегченный сервер разработки Django, доступный на http://127.0.0.1:8000/ :
```sh
python manage.py runserver
```
Для сокращения ссылки использоваться метод:
```sh
POST /_short
```
Данные о ссылке передаются в теле документа в формате JSON:
```sh
{"url": "https://www.site.com/with/long/url?and=param"}
```
Запрос на сокращение ссылки  выглядить следующим образом:
```sh
curl -H "Content-Type: application/json" \
-X POST \
-d '{"url": "https://www.site.com/with/long/url?and=param"}' \ http://localhost:8000/_short
```
Все ответы приходят в формате JSON. Так, на метод сокращения ссылки придет URL в формате:
```sh
{"shorten": "http://localhost:8000/xyz123"}
```

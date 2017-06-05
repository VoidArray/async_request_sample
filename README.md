# Python, асинхронные запросы.

Сервер на базе Django, клиентская часть на базе aiohttp

## Как развернуть сервер


### Установить модули для Python 3

django
### Создать таблицы в БД

python manage.py migrate

### Создать суперпользователя

python manage.py createsuperuser

### Запустить

python manage.py runserver


## Как развернуть Клиент

### Установить модули для Python 3

aiohttp

### Запустить

python .\async_client.py
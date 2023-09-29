# Тестовое задание
### Техническое задание

##### Реализовать rest api:

Завдання.
Написати файл views.py в revenue. Реалізувати ендпоинт в якому ми отримуємо queryset моделі RevenueStatistic з поділом по дням (date) та назвою (name), з агрегованими сумами значень revenue та пов'язаними значеннями spend, impressions, clicks, conversion з моделі SpendStatistic.
Написати файл views.py в spend. Реалізувати ендпоинт в якому ми отримуємо queryset моделі SpendStatistic з поділом по дням (date) та назвою (name), з агрегованими сумами значень spend, impressions, clicks, conversion та пов'язаними значеннями revenue з моделі RevenueStatistic.

Використовувати засоби Django Rest Framework.


### Описание 
## Использованные технологии

- Python
- Django
- Django REST framework
- Postgresql
- Nginx
- Docker
- docker-compose

### Инструкция по развертыванию проекта.

1. Клонируйте репозиторий:
```
git@github.com:Yana-K38/task_test.git
```
2. Создать файл .env в корне проекта и заполнить его всеми ключами:
```
DB_NAME=postgres_task
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```
3. Собрать контейнеры:
```
cd send_revenue/
docker-compose up -d --build
```
4. Сделать миграции, собрать статику и создать суперпользователя:
```
docker-compose exec  backend python manage.py makemigrations --noinput
docker-compose exec  backend python manage.py migrate --noinput
docker-compose exec  backend python manage.py collectstatic --no-input
docker cp static/  <ID container>:var/html/    
docker-compose exec backend python manage.py createsuperuser
```
Для заполнения базы данных начальными данными модели RevenueStatistic и SpendStatistic:
```
$ docker exec -e DJANGO_SETTINGS_MODULE=blog_api.settings <container backend ID> python custrom_mixer.py
```
##### После запуска проекта,  будут доступны эндпоинты:
```http://127.0.0.1/admin/```
```
    login: admin
    password: admin
```
```http://127.0.0.1:8000/revenue/revenue-statistic/```

```http://127.0.0.1:8000/spend/spend-statistic/```


# Yatube
## _Описание проекта Yatube_

Yatube - это API для блога.
API было написано согласно документации. 
Решает задачу взаимодействия сервера и мн-ва клиентов посредством JWT-токенов
С помощью этого проекта теперь любой пользователь сможет:

- Просмотреть/создать/удалить/изменить посты и комментарии
- Посмотреть подписки и подписаться

## Технологии

При разработке Yatube применялись:

- Django 2.2.16
- Django Rest Framework
- Djoser


## Установка

Склонируйте данный проект с github(используем ssh) и перейдите в директорию с проектом

```sh
git clone git@github.com:<your_username>/api_final_yatube.git
cd folder_with_app
```

Создайте и активируйте виртуальное окружение, установите все необходимые пакеты

```sh
python -m venv venv
source venv/Scripts/activate
pip install -r requirements
```

Перейдите в директорию yatube_api/, сделайте миграции и запустите проект

```sh
cd yatube_api/
python manage.py migrate
python manage.py runserver
```

## Примеры

Некоторые примеры запросов к API.

| Метод | Запрос | Что делает |
| ------ | ------ | ------ |
| GET | [api/v1/posts/][PlDb] | Получение публикаций |
| POST | [api/v1/posts/][PlGh] | Создание публикации |
| GET | [api/v1/posts/{post_id}/comments/{id}][PlGd] | Получение комментария |
| DELETE | [api/v1/posts/{post_id}/comments/{id}][PlOd] | Удаление комментария |
| PATCH | [api/v1/posts/{id}/][PlMe] | Частичное обновление публикации |
| GET | [api/v1/follow/][PlGa] | Подписки |
| POST | [api/v1/follow/][PlGa] | Подписка |
| POST | [api/v1/jwt/create/][PlGa] | Получить JWT-токен |

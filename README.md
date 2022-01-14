# Сайт риэлторского агентства

Сайт находится в разработке, поэтому доступна только страница со списком квартир и админка для наполнения БД.

## Запуск

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`  
- Скачайте тестовую базу данных [здесь](https://dvmn.org/filer/canonical/1565091134/187/)  
- Примените все миграции командой `python3 manage.py migrate`  
- Создайте суперпользователя, он будет нужен для входа в админку `python manage.py createsuperuser`  
- Запустите сервер командой `python3 manage.py runserver`  
- Админка доступна [по этому адресу](http://127.0.0.1:8000)  

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `DATABASE` — однострочный адрес к базе данных, например: `sqlite:///db.sqlite3`. Больше информации в [документации](https://github.com/jacobian/dj-database-url)

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

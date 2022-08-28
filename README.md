# Дипломный проект — сайт Foodgram, «Продуктовый помощник».
![example workflow](https://github.com/TimofeyVorobiev/foodgram-project-react/actions/workflows/main.yml/badge.svg)
## Описание проекта Foodgram
Онлайн-сервис и API для него. На этом сервисе пользователи 
могут публиковать рецепты, подписываться на публикации других 
пользователей, добавлять понравившиеся рецепты в список «Избранное», 
а перед походом в магазин скачивать сводный список продуктов, 
необходимых для приготовления одного или нескольких выбранных блюд.
## Установка проекта на локальной машине
Клонировать репозиторий и перейти в него:
```
git clone https://github.com/TimofeyVorobiev/foodgram-project-react.git
```
Создайте и активируйте виртуальное окружение для этого проекта:
```
python -m venv venv
```
```
source .\venv\Scripts\activate
```
Установите зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполните миграции:
```
python manage.py migrate
```
Перейдите в директорию проекта:
```
cd backend
```
Создайте файл .env в директории backend и заполните его данными по этому 
образцу:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
Запустите проект:
```
python manage.py runserver
```
## Установка проекта на боевом сервере
Форкнуть репозиторий:
```
git clone https://github.com/TimofeyVorobiev/foodgram-project-react.git
```
Зайти на Git-Settings-Secrets-Action и заполнить следующие параметры:
```
DB_ENGINE - тип Базы Данных
DB_HOST - контейнер БД
DB_NAME - имя БД
DB_PORT - порт БД
POSTGRES_USER - пользователь в БД
POSTGRES_PASSWORD - пароль пользователя в БД
DOCKER_PASSWORD - пароль к докерхаб
DOCKER_USERNAME - логин к докерхаб
HOST - адрес боевого сервера
USER - логин к боевому серверу
PASSPHRASE - пароль боевого сервера, если есть
SSH_KEY - приватный ключ локальной машины
TELEGRAM_TO - ваш ID в Telegram мессенджере
TELEGRAM_TOKEN - токен
```
Проект разоваричвается после выполнения комнды `git push` в репозиторий GitHub.

В разделе GitHub Actions можно отследить все стадии развертывания проекта 
согласно инструкциям workflow файла.

Зайти на сервер по команде:
`ssh ваш-логин@ваш-ip`

Обновить пакеты на боевом сервере:
`sudo apt update`

Установите docker.io командой `sudo apt install docker.io ` и docker-compose 
командой `sudo apt install docker-compose`

После успешного workflow, запустить следующие команды:

`sudo docker-compose exec web python manage.py makemigrations` и
создаем миграции.

`sudo docker-compose exec web python manage.py migrate` и
запускаем миграции.

`sudo docker-compose exec web python manage.py createsuperuser` и
создаем суперпользователя. 

Копируем статику `sudo docker-compose exec web python manage.py collectstatic --no-input`.

Копируем из csv файла тэги `sudo docker-compose exec web python manage.py load_tags.py`.

Копируем из csv файла ингредиенты `sudo docker-compose exec web python manage.py load_ingredients.py`.

Переходим к проекту по адресу: http://130.193.43.205 и регистрируем пользователя, создаем рецепты и развлекаемся.

Автор проекта Тимофей Воробьев.
# Контейнеризация API

## Установка

#### Шаг Первый. Сборка контейнера
```bash
docker-compose build
```
#### Шаг Второй. Запуск контейнера
```bash
docker-compose up
```
#### Шаг Третий. База данных
```bash
docker-compose run web python manage.py migrate --no-input
```
## Использование
### Создание суперпользователя Django
```bash
docker-compose run web python manage.py createsuperuser
```
### Импорт данных в формате .json
```bash
docker-compose run web python manage.py loaddata path/to/your/json
```
### Выключение контейнера
```bash
docker-compose down
```
### Удаление всех Docker контейнеров

```bash
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```




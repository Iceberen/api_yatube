# 📡 API Yatube

REST API для социальной сети **YaTube**, реализующий функциональность постов, групп, комментариев и подписок.

---

## 🔧 Возможности API

Поддерживает следующие функции:

- 🔐 Регистрация и авторизация по токену (JWT)
- 📝 CRUD для постов
- 💬 Комментарии к постам
- 👥 Группы (чтение)
- ➕ Подписка / отписка на авторов
- 🔍 Получение ленты подписок

---

## 🔌 Основные эндпоинты

| Метод | URL                          | Назначение                         |
|-------|------------------------------|------------------------------------|
| POST  | /api/v1/token/               | Получение JWT токена               |
| GET   | /api/v1/posts/               | Получение списка постов            |
| POST  | /api/v1/posts/               | Создание нового поста              |
| GET   | /api/v1/posts/{id}/          | Получение конкретного поста        |
| PUT   | /api/v1/posts/{id}/          | Полное обновление поста            |
| DELETE| /api/v1/posts/{id}/          | Удаление поста                     |
| GET   | /api/v1/groups/              | Список всех групп                  |
| GET   | /api/v1/groups/{id}/         | Информация о группе                |
| GET   | /api/v1/posts/{id}/comments/ | Список комментариев к посту        |
| POST  | /api/v1/posts/{id}/comments/ | Добавление комментария             |
| POST  | /api/v1/follow/              | Подписка на автора                 |
| GET   | /api/v1/follow/              | Лента подписок                     |

---

## ⚙️ Технологии

- Python 3.9+
- Django 3.2
- Django REST Framework
- Pytest
- JWT Auth (SimpleJWT)
- Postman

---

## 🚀 Запуск проекта
1. Клонируйте репозиторий:
    ```
    git clone https://github.com/Iceberen/api_yatube.git
    cd api_yatube

2. Cоздать и активировать виртуальное окружение:
    ```
    python -m venv venv
    source venv/bin/activate     # для Linux/macOS
    venv\Scripts\activate        # для Windows

3. Установить зависимости из файла requirements.txt:
    ```
    pip install -r requirements.txt


4. Выполните миграции и запустите сервер:
    ```
    python3 manage.py migrate
    python3 manage.py runserver     # для Linux/macOS
    python manage.py migrate
    python manage.py runserver      # для Windows

5. Тестирование Postman:
- Используйте коллекцию из postman_collection/CRUD_for_yatube.postman_collection.json
- Настройка данных — postman_collection/set_up_data.sh

---

## 🔐 Авторизация
Используется JWT (djoser + simplejwt).
- Получить токен:
    ```
    POST /api/v1/token/
    {
    "username": "ваше_имя",
    "password": "ваш_пароль"
    }
- Добавить в заголовки:
    ```
    Authorization: Bearer <your_token>

---

## 📁 Структура проекта
```
├── yatube_api/
│ ├── api/              # Эндпоинты и логика API (ViewSet’ы, сериализаторы, права доступа)
│ ├── posts/            # Приложение с моделями: Post, Comment, Group, Follow
│ ├── yatube_api/       # Настройки Django
│ └── manage.py
├── tests/                  # Автотесты с использованием pytest
├── postman_collection/     # Коллекция запросов Postman
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## 🧑‍💻 Автор
Разработано: [Iceberen](https://github.com/Iceberen) в рамках учебного спринта по DRF.

---
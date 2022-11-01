# Бэк-энд приложение для спортивного туризма
 Данное приложение включает в себя простые REST API которое позволяют пользователям добавлять информацию о перевалах в базу данных.
***
## Структура проекта:
```
project
├── core
│   ├── __init__.py 
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── submitData
│   ├── __init__.py
│   ├── admin.py
│   ├── api.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│── templates
│   └── swaggerui.html
├── manage.py
└── requirements.txt

```
### Описание структура базы данных:
База данных состоит из восьми моделей.

#### Модель пользователя - pereval_users
Таблица для добавления пользователя и его внесения через связь в таблицу записи перевалов.

 Поля:
1. email - Текстовое поле для почты. Является первичным ключом данной таблицы.
2. phone - Числовое поле для номера телефона пользователя. 
3. name - Текстовое поле для добавления имени.

PostgreSQL:
```
INSERT INTO "public"."pereval_users" ("email", "phone", "name") 
VALUES ('test@example.com', 88005553535, 'Иванов Иван Иванович')
ON CONFLICT DO NOTHING;
 ```

JSON:
 ```
{
    "email": "test@example.com",
    "phone": 88005553535,
    "name": "Иванов Иван Иванович"
}
 ```
#### Модель координат - preval_coordinates
Таблица для добавления координат перевалов и их внесения через связь в таблицу записи перевалов.

Поля:
1. latitude - Плавающее числовое поле для координат широты.
2. longitude - Плавающее числовое поле для координат долготы.
3. height - Числовое поле для координат высоты.

PostgreSQL:
```
INSERT INTO "public"."preval_coordinates" ("latitude", "longitude", "height") 
VALUES (45.3842, 7.1525, 1200)
ON CONFLICT DO NOTHING;
```

JSON:
 ```
{
    "latitude": 45.3842,
    "longitude": 7.1525,
    "height": 1200
}
 ```

#### Модель уровня сложности перевалов - pereval_level
Таблица для уровня сложностей перевалов и их внесения через связь в таблицу записи перевалов.

Так как есть фиксированное количество уровней, которые неизменны, было решено сделать отдельную таблицу для этого.

Поля:
1. name - Текстовое поле, которе является первичным ключом.

PostgreSQL:
```
INSERT INTO "public"."pereval_level" ("name") 
VALUES ('1А')
ON CONFLICT DO NOTHING;
```

JSON:
 ```
{
    "name": "1А",
}
 ```
#### Модель статуса модерации - moderation_status
Таблица для статуса модерации и его внесения через связь в таблицу записи перевалов.

Так как статусы предопределены и будут использоваться во всех таблица, без изменений, было решено сделать отдельную таблицу для этого.

Поля:
1. name - Текстовое поле, которе является первичным ключом.

PostgreSQL:
```
INSERT INTO "public"."moderation_status" ("name") 
VALUES ('new')
ON CONFLICT DO NOTHING;
```

JSON:
 ```
{
    "name": "new",
}
 ```

#### Модель перевалов - pereval_added
Таблица для записи перевалов.

Для неё необходимо заранее создать объекты статуса и уровня. А так же необходимо создать пользователя, хотя бы одного.
Однако координаты связываются один-к-одному, потому нужно создавать их каждый раз.

Поля:
1. beautyTitle - Текстовое поле.
2. title - Текстовое поле.
3. other_titles - Текстовое поле.
4. connect - Текстовое поле.
5. add_time - Поле для времени.
6. coord - Связь с таблицей координат.
7. user - Связь с таблицей пользователя.
8. level_winter - Связь с таблицей сложности перевала.
9. level_summer - Тоже самое.
10. level_autumn - Тоже самое.
11. level_spring - Тоже самое.
12. status - Связь с текущим статусом модерации записи. По умолчанию 'new'

PostgreSQL:
```
INSERT INTO "public"."pereval_added" ("beautyTitle", "title", "other_titles", "add_time", "coord_id", "user_id", "level_summer_id", "level_autumn_id") 
VALUES ('пер. ', 'Пхия', 'Триев', '2022-11-01T18:21:00Z', 8, 'test@example.com', '1А', '1А')
ON CONFLICT DO NOTHING;
```

JSON:
```
{
    "beautyTitle": "пер. ",
    "title": "Пхия",
    "other_titles": "Триев",
    "connect": "",
    "add_time": "2022-11-01T18:21:00Z",
    "coord": 1,
    "user": "test@example.com",
    "level_winter": "",
    "level_summer": "1А",
    "level_autumn": "1А",
    "level_spring": "",
    "status": "new"
}

 ```

#### Модель изображений - pereval_images
Таблица для загрузки изображений.

Изображения хранятся на сервере.

Поля:
1. title - поле для названия изображения.
2. date_added - автоматически заполняемое поле времени.
3. image - поле для добавления изображений
4. pereval - поле для связи с перевалом, к которому они принадлежат.

PostgreSQL:
```
INSERT INTO "public"."pereval_images" ("title", "date_added", "image", "pereval_id") 
VALUES ('title', '2022-11-01T18:21:00Z', 'path/to/image', 3)
ON CONFLICT DO NOTHING;
```

JSON:
 ```
{
    "title": "title",
    "image": "path/to/image",
    "pereval": "1"
}
 ```

#### Модель зон перевалов - pereval_areas
Таблица для зон перевалов.

Поля:
1. id_parent - Числовое поле.
2. title - Текстовое поле.

PostgreSQL:
```
INSERT INTO "public"."pereval_areas" ("id_parent", "title") 
VALUES (0, 'Планета Земля')
ON CONFLICT DO NOTHING;
```

JSON:
 ```
{
    "id_parent": 0,
    "title": "Планета Земля",
}
 ```

#### Модель типов активности - spr_activities_types
Таблица для типов активности.

Поля:
1. title - Текстовое поле.

PostgreSQL:
```
INSERT INTO "public"."spr_activities_types" ("title") 
VALUES ('пешком')
ON CONFLICT DO NOTHING;
```

JSON:
 ```
{
    "title": "пешком",
}
 ```

### Представления для REST API:
Проект работает с использованием Django REST framework.

#### Основные URL пути к интерфейсу DRF:
    "submitData/user" - для модели пользователей.
    
    "submitData/coord" - для модели координат.
    
    "submitData/level" - для модели уровня сложности перевала.
    
    "submitData/status" - для модели статуса модерации записи.
    
    "submitData/pereval" - для модели записей перевалов.
    
    "submitData/images" - для модели изоображений перевалов.
    
    "submitData/areas" - для модели зон перевалов.
    
    "submitData/activities" - для модели типа активностей.

#### Динамические URL пути:
    submitData/user/<емаил пользователя> - для просмотра всех записей оставленных определенным пользователем.
    submitData/<id перевала> - для просмотора конкретной записи перевала и её редактирования.

#### Так же доступен swagger - "swagger-ui/"
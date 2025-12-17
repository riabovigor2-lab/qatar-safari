Проект для аренды  внедорожников  по дюнам 


что использовал для проеката
Python 
Django 
Bootstrap 
SQLite 

--------------------------
    УСТАНОВКА ПРОЕКТА!!!!
    git clone https://github.com/riabovigor2-lab/qatar-safari.git
    cd qatar-safari
--------------------------

    виртуальное окружение!!!!
    python -m venv venv
    venv\Scripts\activate
--------------------------
    зависимость!!!!
    pip install -r requirements.txt
    python manage.py migrate
--------------------------

    python manage.py createsuperuser
    имя: admin
    имал: admin@test.com
    пароль: admin123
--------------------------

    начальные данные!!!
    python manage.py loaddata fixtures/initial_data.json

--------------------------
python manage.py runserver



 функционал сайта 

 рабочие страницы 
 Главная, каталог, автомобили, личный кабинет, мои бронирования, профиль, вход и регистрация 
 у админа есть функция редактирование брони 
 создавать брони пользователям 
 

Django-monolith
the django monolith questionnaire. a basic website with roles, authentication, and the ability to post and upload photos.

Запуск
Если необходимо, создайте вирутальное окружение:

python -m venv venv
и активируйте его

Перейдите в папку проекта и выполните:

pip install -r requirments.txt # установка зависимостей
python manage.py migrate # миграции в базу данных
Запустите проект на локальном хосту:

python manage.py runserver
Если вам необходимо, вы можете создать администратора:

python manage.py createsuperuser
и выполните требуемые шаги в консоли

Чтобы перейти в панель админ-управления, напишите в поисковую строку:

{ваш локальный хост}/admin

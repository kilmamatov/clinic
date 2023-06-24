# clinic
python3 -m venv venv (создаем врт окр)

source venv/bin/activate (активируем его)

pip install -r requirements.txt (устанавливаем все зависимости)

./manage.py migrate (Производим миграции и создаем базу данных)

только первый раз для создания проекта (ЕЩЕ РАЗ ПРОПИСЫВАТЬ НЕ НУЖНО) {

django-admin startproject project . (создаем проект джанго)

django-admin startapp core (создаем приложение джанго)

}

./manage.py createsuperuser (log: admin, pass: admin)  

./manage.py runserver

http://127.0.0.1:8000/admin/

Создаем пару врачей через админку


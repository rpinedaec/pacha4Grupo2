python -m venv venv
. venv/Scripts/activate
pip install -r requirements.txt
django-admin startproject ecommprj .   ---> Ya esta creada
py manage.py startapp ecommapp     ---> Ya esta creada
py manage.py migrate
py manage.py createsuperuser
python manage.py collectstatic
# snet-django-desafio
### com docker
```
cd SistemaWeb
docker-compose up --build
```
---
### sem docker
(opcional venv)
```
python3 -m venv env
./env/Scripts/activate.bat
```
```
cd SistemaWeb
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

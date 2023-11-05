# snet-django-desafio
### com docker
```
cd SistemaWeb
docker-compose up --build
```
http://localhost:8000/

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
python manage.py runserver localhost:8000
```
http://localhost:8000/

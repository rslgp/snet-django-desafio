# snet-django-desafio
### sem docker
(opcional venv)
```
python3 -m venv env
./env/Scripts/activate.bat
```
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### com docker
```
docker-compose up --build
```

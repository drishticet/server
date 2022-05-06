## Installtion

clone the repository and cd into the repo

```shell
pipenv install
pipenv shell

python manage.py makemigrations
python manage.py migrate
```

## Running

```
python manage.py runserver
```

## API endpoints

- http://127.0.0.1:8000/api/v1/users/ - get list of all the users
- http://127.0.0.1:8000/api/v1/rest-auth/registration/ - register new users
- http://127.0.0.1:8000/api/v1/leaderboard/ - get leaderboard of top 5 users
- http://127.0.0.1:8000/api/v1/usernamelist/ - return list of usernames

# Market and Storage
This project contains two Django applications: market and storage.

# Prerequisites
Before running the project, you'll need to have Docker installed on your machine.

# Getting started
Clone the repository to your local machine.

Navigate to the project directory in your terminal or command prompt.

Run the following command to start the applications:
```
docker compose up
```

Initialize databasein both projects: market and storage:
```
docker-compose exec market python3 manage.py migrate --run-syncdb
docker-compose exec storage python3 manage.py migrate --run-syncdb
```
Then add superuser:
```
docker-compose exec market python3 manage.py createsuperuser
docker-compose exec storage python3 manage.py createsuperuser
```




This will start the Django development server, and you can access the applications by visiting http://localhost:9000/ (for market)  and http://localhost:9001/ (for storage) in your web browser. You can specify ports in `docker-compose.yaml`.

<!-- move models to app core
    rename apps
    id for orders -->
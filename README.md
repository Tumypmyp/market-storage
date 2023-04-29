# Market and Storage
This is Django application with two separate modules: Market and Storage. The Store module allows administrators to create orders for products via the Django admin page. The Storage module is an API that receives these orders and allows administrators to update their status. Both modules use separate databases, and communication between them is only possible via REST API.

# Prerequisites
Before running the project, you'll need to have Docker installed on your machine.

# Getting started
Clone the repository to your local machine.

Navigate to the project directory in your terminal or command prompt.

Run the following command to start the applications:
```
docker compose up
```

Using second terminal initialize databases in both projects: market and storage:
```
docker-compose exec market python3 manage.py migrate --run-syncdb
docker-compose exec storage python3 manage.py migrate --run-syncdb
```
Then add superuser:
```
docker-compose exec market python3 manage.py createsuperuser
docker-compose exec storage python3 manage.py createsuperuser
```




This will start the Django development server, and you can access the applications by visiting http://localhost:9000/admin/ (for market)  and http://localhost:9001/admin/ (for storage) in your web browser. You can specify ports in `docker-compose.yaml`.

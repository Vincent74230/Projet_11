# "Déployez votre application sur un serveur, comme un pro"
## 10th project of the Python developer path
### Vincent NOWACZYK


Link to the application :  http://207.154.225.46/


#### Context:
The goal of this exercice was to put online a Django project, using DigitalOcean, NginX, Gunicorn.


#### How to run the app on your own computer:
1 - Git clone or fork the project from my github : https://github.com/Vincent74230/Projet_8_digital_ocean

2 - The programm needs a virtual environment, create one and activate it.

3 - Install the dependencies : `pip install -r requirements`

4 - The programm needs a postgreSQL database:
Login as postgres user : `sudo su postgres`
Enter the postgres shell : `psql`
Create a new user : `CREATE USER username WITH PASSWORD 'password';`
Create new database : `CREATE DATABASE mydb WITH OWNER myuser;`
Privileges : `GRANT ALL PRIVILEGES ON DATABASE mydb TO username;`
Allow username to create databases (needed, because Django will create temporary db to run the tests):
`ALTER USER username CREATEDB;`

Exit postgres shell and user.

5 - On your Linux shell : `install-webdrivers --path webdrivers`

6 - Open the settings.py and change username and password on the database section.

7 - Create a .env file on the root level of the app, type in your secretkey and env variable:
SECRET_KEY=secretkey
ENV=DEVELOPMENT

8 - Make the migrations : `python manage.py makemigrations`

9 - Handle staticfiles : `python manage.py collectstatic`

10 - Run the app : `python manage.py runserver`

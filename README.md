# Créez une plateforme pour amateurs de Nutella
## Projet d'étude n°8 du parcours de développeur d'applications Python
### Vincent NOWACZYK


Lien vers l'application :  https://vincentnow-purbeurre.herokuapp.com/home/


#### Contexte de l'exercice:

Un couple de restorateurs nouvellement installés décident de créer un site permettant à leurs clients
de trouver des substituts alimentaires saints à ce qu'ils mangent régulièrement.
Ils font appel à nous pour développer un plateforme.

#### Ce projet valide les compétences suivantes:

- Elaboration d'un site statique en Django
- Exploitation d'une API web : Openfoodfacts
- Développement d'un algorithme de recherche en Python
- Utilisation d'une base de données POSTGRESQL
- Utilisations de tests unitaires et d'intégration
- Deploiement sur Heroku
- Respect d'un cahier des charges


#### How to run the app on your own computer:

Programm needs a postgresql database:
- Create a postgresql database:
- Open a console, open psql and create a DB called 'pur_beurre_db' with user 'pur_beurre_owner'
- Give all privileges to pur_beurre_owner on pur_beurre_db.


Clone the app on github:
- https://github.com/Vincent74230/Projet_8
All the app is license free

Run the app:
- First change the password of the database on `settings.py` (DATABASES={})
- Open a virtualenv and install requirements `pip3 install requirements.txt`
- Run it by typing `python manage.py runserver`
- Open the link given by your console
from fabric.api import local
import os

from fabvenv import virtualenv


def clear_cart_schema():
	""" Clears intial migrations for existing Cart Schema """
	mysql_password = os.environ['MYSQL_PASSWORD']
	shell_command = "mysql -u root --password="
	

	# Example  for reference 
	#	local(" mysql -u root --password={password} -e 'show databases;' ".format(password=mysql_password))
	#	query = "show databases;"
	#	local("{0}{1} -e '{2}' ".format(shell_command,mysql_password,query))
	#	local("{0}{1} -e 'use sid;' ".format(shell_command,mysql_password))
	
	# 1. 	Empty the django_migrations
	local("{0}{1} -e 'delete from django_migrations;' sid ".format(shell_command,mysql_password))

	

	# 2. 	Delete  migrations folder (for every app)
	local("rm -rf cart/migrations/")

	# 3. 	Reset the migrations for the "built-in" apps
	local("python manage.py migrate --fake")

	# 4. 	For each app run - Take care of dependencies 
	# 		(models with ForeignKey's should run after their 
	# 		parent model).
	local("python manage.py makemigrations cart")
	
	# 5. 	Fake intial 
	local("python manage.py migrate  --fake-initial")
	
	#6. 	Finally migrate 
	local("python manage.py migrate")


def migrate_cart():
	local("python manage.py makemigrations cart")
	local("python manage.py migrate")
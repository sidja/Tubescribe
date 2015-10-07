from fabric.api import local
import os

from fabvenv import virtualenv

from tubescribe.util.fabutil import *


from fabric.api import put, run, settings, sudo
from fabric.operations import prompt
from fabric.contrib import django

from fabric.api import *
from fabtools import require
import fabtools



env.user						= 'root'
env.key_filename				= '/home/sid/.ssh/deploy_open_ssh'
env.VIRTUALENV 					= '/webapps/tubescribe/'

env.roledefs = {
	'master' : [' 128.199.167.207'],
	#'staging' : ['1.1.1.1'],
}




# >>> from fabvenv import virtualenv
# >>> with virtualenv('/home/me/venv/'):
# ...     run('python foo')

#@task
def runremotedev():
	with virtualenv(env.VIRTUALENV):
		sudo('echo $PATH')
		#sudo("python manage.py runserver 128.199.167.207:9000 " \
		#	"--settings=tubescribe.settings.local")


#@task
def setup_db():
	""" Install and create PostgresSQL DB and DB user"""
	
	# Require a PostgreSQL server
	require.postgres.server()
	require.postgres.user('tubescribe', 'password')
	require.postgres.database('tubedb', 'tubescribe')
	
	# psycopg2 does not seem to be working with out this 
	sudo('apt-get -y install python-psycopg2 libpq-dev python-virtualenv git python-dev', )


	# pip install django-braces
	# pip install youtube-dl
	# pip install django-bootstrap3
	# pip install fabric-virtualenv
	# pip install git+git://github.com/ronnix/fabtools.git




def runlocal():
	""" Run local server """
	local("python manage.py runserver 128.199.167.207:9000 " \
		"--settings=tubescribe.settings.local")


def runremote():
	"""  Run remote server """


def run():
	local("python manage.py --settings=tubescribe.settings.local runserver")




# >>> from fabvenv import virtualenv
# >>> with virtualenv('/home/me/venv/'):
# ...     run('python foo')



#!/bin/bash


DJANGODIR=/webapps/tubescribe/Tubescribe

# Save system ip address
IP_ADDR=$(ip addr | grep 'state UP' -A2 | tail -n1 | awk '{print $2}' | cut -f1  -d'/')

PORT=8000

DJANGO_WSGI_MODULE=tubescribe.wsgi

cd $DJANGODIR
pwd

# Traditional run ex
#	gunicorn tubescribe.wsgi:application --bind 128.199.167.207:8000


#echo ${DJANGO_WSGI_MODULE} ${IP_ADDR}:${PORT}

# Kill all gunicorn instances

# This exits bash script 
#kill -9 `ps aux | grep gunicorn | awk '{print $2}'`

gunicorn ${DJANGO_WSGI_MODULE}:application --bind ${IP_ADDR}:${PORT}











# NAME="tubescribe"                                	 # Name of the application
# DJANGODIR=/webapps/tubescribe/Tubescribe 		    # Django project directory
# SOCKFILE=/webapps/tubescribe/run/gunicorn.sock 	# we will communicte using this unix socket
# USER=deploy                                       	# the user to run as
# GROUP=webapps                                    	# the group to run as
# NUM_WORKERS=3                                    	# how many worker processes should Gunicorn spawn
# DJANGO_SETTINGS_MODULE=hello.settings            	# which settings file should Django use
# DJANGO_WSGI_MODULE=hello.wsgi                    	# WSGI module name

# echo "Starting $NAME as `whoami`"

# # Activate the virtual environment
# cd $DJANGODIR
# source ../bin/activate
# export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
# export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# # Create the run directory if it doesn't exist
# RUNDIR=$(dirname $SOCKFILE)
# test -d $RUNDIR || mkdir -p $RUNDIR

# # Start your Django Unicorn
# # Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
# exec ../bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
#   --name $NAME \
#   --workers $NUM_WORKERS \
#   --user=$USER --group=$GROUP \
#   --bind=unix:$SOCKFILE \
#   --log-level=debug \
#   --log-file=-
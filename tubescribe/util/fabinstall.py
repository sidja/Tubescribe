



def install_gunircor():
	if env.VIRTUALENV:
		with virtualenv(env.VIRTUALENV):
			sudo('pip install gunicorn')
			
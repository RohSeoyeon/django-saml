# Djano-SAML

This repository tests Django environment uses Onelogin's SAML as the authentication.
The code was referenced here https://github.com/SAML-Toolkits/python3-saml.


## Onelogin settings

check https://developers.onelogin.com/saml/python

## Get Started

**Python : v3.9.10**
1. Install packages
	```
	pip install -r requirements.txt
	```
2. edit **onelogin** package file if you use SHA256(not necessary)
dir: {env}/lib/python3.9/site-packages/onelogin/saml2/constants
	```
	.
	.
	# Add this line
	DSA_SHA256 = 'http://www.w3.org/2001/04/xmldsig#dsa-sha256'
	.
	.
	# Edit this line
	DEPRECATED_ALGORITHMS = [DSA_SHA256, RSA_SHA256, SHA256]
	```
3. edit **django** package file's get_user function - disable password verifying
	dir: {env}/lib/python3.9/site-packages/django/contrib/auth/\_\_init__
	```
	def  get_user(request):
	"""
	Return the user model instance associated with the given request session.
	If no user is retrieved, return an instance of `AnonymousUser`.
	"""
	from .models import AnonymousUser

	user = None
	try:
		user_id = _get_user_session_key(request)
		backend_path = request.session[BACKEND_SESSION_KEY]
	except  KeyError:
		pass
	else:
		if backend_path in settings.AUTHENTICATION_BACKENDS:
			backend = load_backend(backend_path)
			user = backend.get_user(user_id)

	# Verify the session
	# if hasattr(user, "get_session_auth_hash"):
	# 	session_hash = request.session.get(HASH_SESSION_KEY)
	# 	session_hash_verified = session_hash and constant_time_compare(
	# 		session_hash, user.get_session_auth_hash()
	# 	)
	# 	if not session_hash_verified:
	# 		request.session.flush()
	# 		user = None

	return user or AnonymousUser()
	```
4. Edit SECRET_KEY and ALLOWED_HOSTS in settings.py

5. migrate and run server
	 ```
	 python3 manage.py migrate
	 python3 manage.py runserver 0.0.0.0:8000
	 ```
6. check authentication at /test
	'successfully accessed' message comes, it's done!
	(if it returns 403 response authentication is something wrong)

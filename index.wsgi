import sae
from hectorsite import wsgi

application = sae.create_wsgi_app(wsgi.application)

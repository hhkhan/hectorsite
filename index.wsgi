import sys
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hectorsite.settings")
sys.path.append(os.path.join(os.path.dirname(__file__), 'hectorsite'))

import sae
from hectorsite import wsgi

application = sae.create_wsgi_app(wsgi.application)

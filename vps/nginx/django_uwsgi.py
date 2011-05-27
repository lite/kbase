import os
import sys

sys.path.append('/home/dli/code/projects')
os.environ['DJANGO_SETTINGS_MODULE'] = 'djproj.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

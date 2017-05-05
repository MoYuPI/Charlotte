import sys
import os
import django

sys.path.append('../../../Charlotte')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Charlotte.settings'
django.setup()
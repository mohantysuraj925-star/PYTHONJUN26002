import os
import sys
from django.core.wsgi import get_wsgi_application

# Render ke liye absolute path set kar rahe hain
sys.path.append('/opt/render/project/src/Month-1/Week-3/Day-2/Practice')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SuraajCore.settings')
application = get_wsgi_application()

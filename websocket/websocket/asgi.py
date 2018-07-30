import os
import django
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTING_MODULE", "websocket.settings")
django.setup()
application = get_default_application()

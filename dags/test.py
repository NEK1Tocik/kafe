import os
import sys
#sys.path.append('C:\\Users\\admin\\Documents\\python\\pythonProject2')
sys.path.append('C:\\Users\\admin\\Documents\\python\\pythonProject2\\shpak')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shpak.shpak.settings')
import django
django.setup()
from pizza.models import PizzaItem


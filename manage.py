import os
import sys

# Add the project root to Python's path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')

from django.core.management import execute_from_command_line

execute_from_command_line(sys.argv)

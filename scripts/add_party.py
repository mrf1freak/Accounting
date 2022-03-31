import os, sys, csv

proj_path = os.getcwd()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Accounting.settings")
sys.path.append(proj_path)
os.chdir(proj_path)
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from Party.models import Party

os.chdir('scripts')

with open('party.csv') as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        name, amount, code = line[0], int(line[1]), line[2]

        print(name, amount, code)

        party = Party(code=code, name=name)
        party.initial_balance = amount
        party.save()
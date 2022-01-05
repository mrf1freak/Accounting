import os, sys, csv

proj_path = os.getcwd()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Accounting.settings")
sys.path.append(proj_path)
os.chdir(proj_path)
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


from Account.models import Account
from GeneralEntry.models import GeneralEntry
from django.contrib.auth.models import AnonymousUser
import datetime
from django.contrib.auth import authenticate, login


os.chdir('scripts')

with open('party.csv') as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        name, amount, code = line[0], int(line[1]), line[2]

        print(name, amount, code)


        account = Account(code=code, name=name)

        type = ""
        if amount < 0:
            type = "Debit"
        else:
            type = "Credit"

        user = authenticate(username='nabeel', password='allah123')
        
        account.save()
        if amount != 0:
            entry = GeneralEntry(description="Initial Balance", amount=amount, user=user, type=type, account=account, date=datetime.datetime.today().strftime("%Y-%m-%d"))
            entry.save(
            
            )
        # form.save()
        # entry.save()

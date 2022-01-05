import os, sys, csv

proj_path = os.getcwd()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Accounting.settings")
sys.path.append(proj_path)
os.chdir(proj_path)
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


from Product.models import Product

os.chdir('scripts')

with open('products.csv') as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        code = line[1]
        name = line[0]

        p = Product(code=code, name=name)
        p.save()

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

django.setup()

import random
from first_app.models import User
from faker import Faker
fakegen = Faker()

def add_dat(n=5):
    for i in range(n):
        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.email()

        usr = User.objects.get_or_create(fname = fake_fname,lname = fake_lname,email = fake_email)[1]


if __name__ == '__main__':
    print("populating scripts")
    add_dat(10)
    print("Completed")

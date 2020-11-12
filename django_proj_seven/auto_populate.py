import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_proj_seven.settings')

import django
django.setup()

import faker
import random
from testappthree.models import #Model_Name(s)

f = faker.Faker()

def populate(N):

    for entry in range(N):

        # fake_fname = f.first_name()
        # fake_lname = f.last_name()
        # fake_email = f.free_email()

        # added_object = Model_Name.objects.get_or_create(f_name = fake_fname, l_name = fake_lname, email = fake_email)[0]

if __name__ == '__main__':

    print('populating data')
    populate(N = )
    print('data population complete')
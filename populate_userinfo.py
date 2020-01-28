import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoPro.settings')
import django
django.setup()

from app_one.models import UserInfo
from faker import Faker

fake_obj = Faker()

def population_data(n=5):

    for i in range(n):

        name = fake_obj.name().split()
        fake_first_name = name[0]
        fake_last_name = name[1]
        fake_email = fake_obj.email()

        UserInfo.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]

if __name__ == '__main__':
    print("\n Populating script")
    population_data(10)
    print('\n*****Data inserted*****')

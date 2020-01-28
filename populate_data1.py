import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoPro.settings')
import django
django.setup()

#Fake Population Script

import random
from app_one.models import AccessRecord, Webpage, Topic
from faker import Faker

fakeobj = Faker()
topics = ['Entertainment', 'Marketing', 'Travel', 'Airline', 'Music']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for i in range(N):

        top = add_topic()

        fake_url = fakeobj.url()
        fake_date = fakeobj.date()
        fake_name = fakeobj.company()

        #webpage insertion
        webpg = Webpage.objects.get_or_create(topic = top, url=fake_url, name = fake_name)[0]

        #AccessRecord Insertion
        AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print('\n Populating Script\n')
    populate(10)
    print("*****Data Inserted*****")

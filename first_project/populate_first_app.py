import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

django.setup()

import random
from first_app.models import AccessRecord,Topic,WebPage
from faker import Faker
fakegen = Faker()
topics = ['search','marketplace','networking','news','social','games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(n=5):

    for i in range(n):
        top = add_topic()

        fake_url=fakegen.url()
        fake_date =fakegen.date()
        fake_name= fakegen.company()

        wbpg = WebPage.objects.get_or_create(topic = top,url = fake_url,name = fake_name)[0]

        accr = AccessRecord.objects.get_or_create(name = wbpg , date= fake_date)[0]


if __name__ == '__main__':
    print("populating scripts")
    populate(20)
    print("completed")

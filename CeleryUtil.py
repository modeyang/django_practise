#!/usr/bin/python
#coding=utf-8


from django.core.management import setup_environ
from Django_Learn import settings
setup_environ(settings)

import celery
from celery import Task
from celery.registry import tasks
from mvc.models import Book

from datetime import date

@celery.task
class CreateBookTask(Task):
    def run(self, name, pub_date, *args, **kwargs):
        book = Book(name=name, pub_date=pub_date)
        book.save()
        print Book.objects.all()
        return book

tasks.register(CreateBookTask)

@celery.task
def create_book(name, pub_date):
    Book.objects.create(name=name, pub_date=pub_date)
    print Book.objects.all()

if __name__ == '__main__':
    CreateBookTask().delay('ygs', date.today())
    # print dir(Book.objects.all().delete())
    # create_book.delay('ygs', date.today())
    # CreateBookTask().run('ygs', date.today())
    # Book(name= 'ygs', pub_date = date.today()).save()
    # print date.today()

from django.db import models, transaction

# Create your models here.

from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from datetime import datetime
import json
import time

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=200, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Task_Date(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date = models.DateField()

@receiver(post_save, sender = Task)
def task_handler_post(sender, instance, **kwargs):
    print("Signal Received")

    # simulating a time-consuming task
    # sleep for 5 seconds to simulate delay
    time.sleep(5)
    print("Signal Handler Done")  

    # ensuring Task_Date creation happens in the same transaction
    with transaction.atomic():
        # creating instance of the model
        Task_Date.objects.create(task=instance, date=datetime.now())
        print("Object Created")


class History(models.Model):
    historical = models.TextField(default='{}')
    
@receiver(pre_save, sender=Task)
def task_handler(sender, instance, **kwargs):
    print("Signal Received")

    # automatically creates slug
    instance.slug = (slugify(instance.name))

@receiver(pre_delete, sender = Task)
def task_handler_pre_delete(sender, instance, **kwargs):
    data = {'task': instance.name, 'description': instance.description, 'slug':instance.slug}
    History.objects.create(historical = json.dumps(data))
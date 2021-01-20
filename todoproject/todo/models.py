from django.db import models

PRIORITY = (('danger', 'high'), ('info', 'normal'), ('success', 'low'))

# Create your models here.
class ToDoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length = 100,
        choices = PRIORITY
    )

    duedate = models.DateField()

    def __str__(self):
        return self.title


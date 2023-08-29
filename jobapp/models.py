from django.db import models

class Form(models.Model):
    first = models.CharField(max_length=80)
    last = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)

    def __str__(self):
        return f'{first} {last}'
    
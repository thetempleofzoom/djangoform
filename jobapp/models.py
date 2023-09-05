from django.db import models

class Form(models.Model):
    first = models.CharField(max_length=80)
    last = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)

    # determines what is shown in admin form section. don't forget self variable.
    def __str__(self):
        return f'{self.first} {self.last}'
    
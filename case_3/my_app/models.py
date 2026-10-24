from django.db import models

class Name(models.Model):
    name = models.CharField(max_length=15, verbose_name='Имя')

    def __str__(self):
        return self.name

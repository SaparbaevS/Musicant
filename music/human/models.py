from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    course = models.IntegerField()

    instrument_choices = [
        ('guitar', 'Гитара'),
        ('piano', 'Пианино'),
        ('violin', 'Скрипка'),
        ('drums', 'Барабаны'),
        ('flute', 'Флейта'),
    ]
    instrument = models.CharField(max_length=10, choices=instrument_choices)
    performance = models.IntegerField(choices=[(i, str(i)) for i in range(1, 13)])
    has_paid = models.BooleanField()

    def __str__(self):
        return f'{self.name} - {self.surname}'


    def get_absolute_url(self):
        return f"/{self.pk}"
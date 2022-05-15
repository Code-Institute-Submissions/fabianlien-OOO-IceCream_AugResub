from django.db import models


# Create your models here.
class Reservation(models.Model):
    AVAILABLE_GROUPS = (
       (1, '1'),
       (2, '2'),
       (3, '3'),
       (4, '4'),
       (5, '5'),
       (6, '6'),
       (7, '7'),
       (8, '8')
    )
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.BigIntegerField(blank=True)
    party_size = models.IntegerField(choices=AVAILABLE_GROUPS)
    date = models.DateField()
    time = models.TimeField()
    duration = models.DurationField(default=3)
    message = models.TextField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.party_size} prs.'

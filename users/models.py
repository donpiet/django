from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Termin(models.Model):
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=9)
    status = models.CharField(default='zajety', max_length=10)
    price = models.CharField(default='5', max_length=10)

    # def get_url(self):
    #     return reverse('termin', kwargs={'pk': self.pl})

    def get_absolute_url(self):
        return reverse('termin-create')

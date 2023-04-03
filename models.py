from django.db import models
from django.urls import reverse
from datetime import datetime

class Klient(models.Model):
    name = models.CharField(max_length=100, null=False)
    vorname = models.CharField(max_length=100, null=False)
    telefonnummer  = models.CharField(max_length=100, null=False)
    projekt = models.CharField(max_length=100, null=False)
    bemerkung = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return "{}, {}".format(self.name, self.vorname)
    
    def get_absolute_url(self):
        return reverse("detailclient", kwargs={"pk": self.pk})

class Eintrag(models.Model):
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    datum = models.DateField(null=False, default=datetime.today)
    doku = models.TextField(max_length=1000)
    bild = models.ImageField(upload_to='images/', null=True, blank=True,)
    
    def context(self):
        Eintrag.klient == Klient.id

    def __str__(self):
        return "{}, {}, {}".format(self.datum, self.klient, self.doku)
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
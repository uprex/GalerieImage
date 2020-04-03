from django.db import models

# Create your models here.


class Post(models.Model):
    url = models.CharField(max_length=250)
    nom = models.CharField(max_length=150)
    date = models.DateTimeField()
    nb_telechargement = models.IntegerField()
    img_file = models.FileField(upload_to="../static/")

    object = models.Manager()

    def __unicode__(self):
        return self.title
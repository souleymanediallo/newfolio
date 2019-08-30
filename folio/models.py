from django.db import models

# Create your models here.
class Folio(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images_pic", default="folio.jpg")
    description = models.TextField()

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="blogs/",blank=True)
    reviews = models.FloatField()


    def __str__(self) :
        return self.title
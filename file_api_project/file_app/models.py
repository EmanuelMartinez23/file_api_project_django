from django.db import models

class File(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='files/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
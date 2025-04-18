from django.db import models

class App(models.Model):

    CATEGORY_CHOICES = [
        (1, 'Apps'),
        (2, 'Games'),
    ]
    name = models.CharField(max_length=255)
    decription = models.TextField(blank=True, null=True)
    app_file = models.FileField(upload_to='apps/')
    thumbnail = models.ImageField(upload_to='thumnails/', blank=True, null=True)
    version = models.CharField(max_length=30, blank=True, null=True)
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=1)


    def __str__(self):
        return f"{self.name} ({self.version})"
    
    def get_category_display(self):
        return dict(self.CATEGORY_CHOICES).get(self.category, "Unknown")
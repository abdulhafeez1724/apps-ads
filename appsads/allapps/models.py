from django.db import models
from users.models import NewUser

# Create your models here.
class Apps(models.Model):
    name = models.CharField(max_length=255)
    package = models.CharField(max_length=255)
    links = models.URLField()
    icons = models.ImageField(upload_to='static/icons/')  
    platform = models.CharField('Platform',max_length=50,
        choices=NewUser.Platform.choices,
        default=NewUser.Platform.ANDROID,
        blank=False
    )
    added_by = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    created_at = created_at = models.DateTimeField(auto_now_add=True)
    index = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Apps"

class Placement(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    index = models.IntegerField(default=0)
    added_by = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    app = models.ForeignKey(Apps, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Placements"

class AdNetwork():
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    index = models.IntegerField(default=0)
    added_by = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    app = models.ForeignKey(Apps, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Ad Networks"
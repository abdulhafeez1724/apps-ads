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
    created_at = models.DateTimeField(auto_now_add=True)
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

class AdNetwork(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    index = models.IntegerField(default=0)
    added_by = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    app = models.ForeignKey(Apps, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Ad Networks"


class Source(models.Model):
    app = models.ForeignKey(Apps, on_delete=models.CASCADE)
    network = models.ForeignKey(AdNetwork, on_delete=models.CASCADE)
    placement = models.ForeignKey(Placement, on_delete=models.CASCADE)
    data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    index = models.IntegerField(default=0)

    def __str__(self):
        return self.data
    
    class Meta:
        # order by
        ordering = ['index']
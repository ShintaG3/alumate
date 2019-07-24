from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL

class MyProfile(models.Model):
    user                = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="profile")
    img                 = models.ImageField(upload_to='profile_image', null=True,blank=True)
    introduction        = models.CharField(max_length=500,null=True,blank=True)
    current_occupation  = models.CharField(max_length=500,null=True,blank=True)
    tags                = models.CharField(max_length=256,null=True,blank=True)
    identicon           = models.CharField(max_length=200,null=True,blank=True)

    def get_img_url(self):
        if self.img:
            return self.img.url
        else:
            return self.identicon

    def __str__(self):
        return f"{self.id} {self.user}"

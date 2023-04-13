from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

class Profile(models.Model):
    user = models.OneToOneField(User, related_name=("user"), on_delete=models.CASCADE)
    name = models.CharField(("الاسم"), max_length=50)
    info = models.TextField(("معلومات عن الدكتور"))
    price = models.IntegerField(("السعر"),null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(("الصورة الشخصيه"), upload_to='media/profile',null=True, blank=True)
    slug = models.SlugField(("slug"),blank=True, null=True)
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]
    def __str__(self) -> str:
        return self.user.username
    

    def save(self, *args, **kwargs):
       
       if not self.slug:
           self.slug = slugify(self.user.username)
       
       super(Profile, self).save(*args, **kwargs) # Call the real save() method

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    

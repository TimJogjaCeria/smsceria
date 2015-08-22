from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    GENDER = (('L', 'Laki-laki'), ('P', 'Perempuan'))

    user = models.OneToOneField(User, related_name="profile")
    gender = models.CharField(
        max_length=10, choices=GENDER, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.CharField(max_length=100, null=True)
    longitude = models.CharField(max_length=100, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Profiles"

    def __unicode__(self):
        return '%s' % (self.user)


def create_profil_user_callback(sender, instance, **kwargs):
    profil, created = Profile.objects.get_or_create(user=instance)
post_save.connect(create_profil_user_callback, User)
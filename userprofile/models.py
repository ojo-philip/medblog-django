from django.db import models
from django.conf import settings
from PIL import Image

User = settings.AUTH_USER_MODEL


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pic', default='default.jpg')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    about_you = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    #     super().save(force_insert, force_update, using, update_fields)
    #     img = Image.open(self.image.path)
    #     if img.height > 350 or img.width > 350:
    #         output_size = (350, 350)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)


class SearchQuery(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    query = models.CharField(max_length=220)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Search Queries'

    def __str__(self):
        return self.user.username

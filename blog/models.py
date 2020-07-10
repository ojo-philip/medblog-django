from django.db import models
from django.utils import timezone
# from django.db.models.signals import pre_saves
# from .utils import unique_slug_generator
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings
from django.db.models import Q

User = settings.AUTH_USER_MODEL


class PostQuerySet(models.QuerySet):
    def search(self, query):
        return self.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__username__icontains=query)
        )


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_img', blank=True, null=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=250, default='', editable=False)
    objects = PostManager()

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            "pk": self.id,
            "slug": self.slug,

        }
        return reverse("blog:post_detail", kwargs=kwargs)

    def get_edit_url(self):
        kwargs = {
            "pk": self.id,
            "slug": self.slug,

        }
        return reverse("blog:post_update", kwargs=kwargs)

    def get_delete_url(self):
        kwargs = {
            "pk": self.id,
            "slug": self.slug,

        }
        return reverse("blog:post_delete", kwargs=kwargs)

    def get_comment_url(self):
        kwargs = {
            "pk": self.id,
            "slug": self.slug,

        }
        return reverse("blog:comment_page", kwargs=kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

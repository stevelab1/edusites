from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse



class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,
                            blank=True)
    url = models.URLField(max_length=300)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', default='https://res.cloudinary.com/hmklz8dtf/image/upload/v1/media/users/2020/11/14/3abc6275419f468bf41a10b64a90f31b--st-etienne-cathedrals_jqbogy')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True,
                               db_index=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='images_liked',
                                        blank=True)
    total_likes = models.PositiveIntegerField(db_index=True,
                                              default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)

    def get_absolute_url(self):
            return reverse('moodboard:detail', args=[self.id, self.slug])

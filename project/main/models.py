from PIL import Image
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

import secrets


User = get_user_model()


class Tiers(models.Model):
    """Tiers plan for Account"""
    link = secrets.token_hex(nbytes=16)
    link_two = secrets.token_hex(nbytes=20)

    activate_url = 'http://127.0.0.1:8000/' + link
    activate_url_two = 'http://127.0.0.1:8000/' + link_two

    STATUS_TRUE = 'True'
    STATUS_FALSE = 'False'
    STATUS_NONE = 'None'
    STATUS_URL = activate_url
    STATUS_URL_TWO = activate_url_two

    CHOICES_STATUS = (
        (STATUS_TRUE, 'True'),
        (STATUS_FALSE, 'False')
    )
    CHOICES_STATUS_URL = (
        (STATUS_NONE, 'None'),
        (STATUS_URL, activate_url),
        (STATUS_URL_TWO, activate_url_two)
    )

    name = models.CharField(verbose_name='Name', max_length=255)
    slug = models.SlugField(unique=True)
    size_thumbnail_image = models.PositiveIntegerField(verbose_name='Px', default=0,
                                                       validators=[MinValueValidator(0), MaxValueValidator(1920)])
    size_thumbnail_image_two = models.PositiveIntegerField(verbose_name='Px two', default=0,
                                                           validators=[MinValueValidator(0), MaxValueValidator(1920)])
    url_original_image = models.CharField(verbose_name='Original image (url)', max_length=255,
                                          choices=CHOICES_STATUS, default=STATUS_FALSE)
    random_expiring_url = models.CharField(verbose_name='Random expiring url', default=STATUS_NONE,
                                           choices=CHOICES_STATUS_URL, max_length=255)
    link_expiration_date = models.PositiveIntegerField(verbose_name='Link expiration date', default=300,
                                                       validators=[MinValueValidator(300), MaxValueValidator(30000)],
                                                       null=True, blank=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    """Customer(User)"""

    user = models.ForeignKey(User, verbose_name='Customer', on_delete=models.CASCADE)
    tiers = models.ForeignKey(Tiers, verbose_name='Tier', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Phone', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Address', null=True, blank=True)

    def __str__(self):
        return "{}: {}".format(self.user.username, self.tiers.name)


def image_thumbnail_path(instance, filename):
    return "img/{}".format(filename)


class UploadImage(models.Model):
    """Upload image"""

    user = models.ForeignKey(User, verbose_name='Customer', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Imagine origin url', upload_to=r'img/')
    thumbnail_image = models.ImageField(verbose_name='Imagine thumbnail', upload_to=r'img_thumbnail/')
    thumbnail_image_two = models.ImageField(verbose_name='Imagine thumbnail two', upload_to=r'img_thumbnail_two/')

    def __str__(self):
        return "{}: {}".format(self.user.username, self.image)

    def save(self, *args, **kwargs):
        """Image size processing"""
        super().save()
        img = Image.open(self.thumbnail_image.path)
        customer = Customer.objects.filter(user=self.user)
        for u in customer:
            if u.tiers.size_thumbnail_image > 0:
                if img.height > u.tiers.size_thumbnail_image:
                    output_size = (u.tiers.size_thumbnail_image, 500)
                    img.thumbnail(output_size)
                    img.save(self.thumbnail_image.path)
            else:
                pass
            if u.tiers.size_thumbnail_image_two > 0:
                img = Image.open(self.thumbnail_image_two.path)
                if img.height > u.tiers.size_thumbnail_image_two:
                    output_size = (u.tiers.size_thumbnail_image_two, 500)
                    img.thumbnail(output_size)
                    img.save(self.thumbnail_image_two.path)
            else:
                pass


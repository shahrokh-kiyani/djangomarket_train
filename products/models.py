from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=7)
    status = models.BooleanField(default=True)
    cover = models.ImageField(blank=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", args=[self.pk])


class Comment(models.Model):
    PRODUCT_STARS = (
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Normal'),
        ('4', 'Good'),
        ('5', 'Perfect'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    stars = models.CharField(choices=PRODUCT_STARS, max_length=10)
    active = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True, null=True)

    def get_absolute_url(self):
        return reverse("detail", args=[self.pk])
    
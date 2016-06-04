from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Rating(models.Model):
    beer_name = models.CharField(blank=False, max_length=50)
    brewer_name = models.CharField(max_length=50, blank=True)
    score = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    notes = models.CharField(max_length=200, blank=True)

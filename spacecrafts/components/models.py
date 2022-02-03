# spacecrafts/components/models.py
from django.db import models


class Category(models.Model):
    COMPONENT_CATEGORIES = [
        ('Power Source', 'Power Source'),
        ('Electronics', 'Electronics'),
        ('Hardware', 'Hardware'),
        ('Engines', 'Engines'),
        ('Safety Tools', 'Safety Tools'),
    ]
    title = models.CharField(
        max_length=100, choices=COMPONENT_CATEGORIES,
    )

    def __str__(self):
        return self.title


class Component(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(
        Category, related_name="category", on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

from django.db import models
from django import utils
from django.core.validators import MaxValueValidator, MinValueValidator

import datetime


class Author(models.Model):
    name = models.CharField("Автор", max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Keyword(models.Model):
    keyword_name = models.CharField("Ключевое слово", max_length=250)

    def __str__(self):
        return self.keyword_name

    class Meta:
        verbose_name = 'Ключевое слово'
        verbose_name_plural = 'Ключевые слова'


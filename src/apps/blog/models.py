from django.db import models


class Post(models.Model):
    headline = models.CharField(verbose_name='Заголовок поста', max_length=255)
    text = models.TextField(verbose_name='Запись', default='')
    date = models.DateTimeField(verbose_name='Дата добавления')
    author = models.CharField(verbose_name="Автор", max_length=255)

    def __str__(self):
        return '%d' % self.id

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

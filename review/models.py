from django.db import models


class Reviews(models.Model):
    name = models.CharField('Имя', max_length=50)
    text = models.TextField('Отзыв')
    data = models.DateTimeField('Даьа')
    rating = models.IntegerField('Рейтинг')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
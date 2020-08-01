from django.db import models


STATUS_CHOICES = [
    ('active', 'Активно'), 
    ('blocked', 'Заблокировано'),
]


class Book(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, default='Name', verbose_name='Имя')
    author = models.EmailField(max_length=40, null=False, blank=False, default='Email Address', verbose_name='Емейл')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='new', verbose_name='Модерация')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return '{}. {}'.format(self.pk, self.title)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

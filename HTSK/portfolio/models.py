from django.db import models
from django.core.files import File


# Create your models here.
class Works(models.Model):
    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'
    name_project = models.CharField('Название проекта', default='work', max_length=100)
    git_link = models.URLField('Ссылка на GitRep', default='https://github.com')
    photo_path = models.ImageField('картинка работа', default=File(open('portfolio/static/logo.jpg', mode='rb')),
                                   upload_to='portfolio/static/work')
    description = models.TextField('Описание', default='something...')

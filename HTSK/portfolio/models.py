from django.db import models


# Create your models here.
class Works(models.Model):
    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'
    name_project = models.CharField('Название проекта', default='', max_length=100)
    git_link = models.URLField('Ссылка на GitRep', default='')
    photo_path = models.ImageField('картинка работа', upload_to='portfolio/static/work')
    description = models.TextField('Описание', default='')

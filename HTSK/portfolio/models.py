from django.db import models


class Works(models.Model):
    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    name_project = models.CharField('Название проекта', default='work', max_length=100)
    git_link = models.URLField('Ссылка на GitRep', default='https://github.com')
    photo_path = models.ImageField('Картинка проекта',
                                   upload_to='portfolio/static/work')
    description = models.TextField('Описание', default='something...')
    habr_link = models.URLField('Ссылка на Habr статью', blank=True)  # (blanc=True) == (required=False)

    def __str__(self):
        return self.name_project

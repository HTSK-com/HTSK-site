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


class Employee(models.Model):
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    surname = models.CharField('Фамилия', max_length=40)
    name = models.CharField('Имя', max_length=40)
    father_name = models.CharField('Отчество', max_length=43, blank=True)
    Git_Hub_profile = models.URLField('Ссылка на репозиторий', blank=True)
    picture_of_staff = models.ImageField('Фотография сотрудника', upload_to='portfolio/static/employee')
    position = models.CharField('Должность', max_length=100)
    experience = models.TextField('Опыт и стаж работы')
    about_myself = models.TextField('О себе', blank=True)
    contact_information = models.TextField('Контактные данные', blank=True, default='htsk.comp@gmail.com')

    def __str__(self):
        return f'{self.surname} {self.name} {self.father_name}'

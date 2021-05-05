from django.test import TestCase
from .models import Works


class TemplateUseTest(TestCase):
    """Тест домашней страницы"""

    def test_uses_home_template(self):
        """тест: используется домашний шаблон"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_uses_our_works_template(self):
        """тест: используется рабочий шаблон"""
        response = self.client.get('our_works')
        self.assertTemplateUsed(response, 'our_works.html', response.content.decode())


class WorkModelTest(TestCase):
    """Тест модели work"""

    def test_saving_and_retrieving_items(self):
        """тест: сохранение и получение элементов"""
        Works.objects.create()
        save_items = Works.objects.first()
        self.assertEqual(save_items.name_project, 'work')



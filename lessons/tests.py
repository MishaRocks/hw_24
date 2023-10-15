from django.test import TestCase

from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from curses.models import Curs
from lessons.models import Lesson
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        # Тестовый пользователь
        self.user = User.objects.create(
            email='test@example.com',
            is_active=True
        )
        self.user.set_password('test')
        self.user.save()

        # Получаем JWT-токен для аутентификации
        get_token = reverse('users:token_obtain_pair')
        token_response = self.client.post(path=get_token, data={'email': 'test@example.com', 'password': 'test'})
        token = token_response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        self.headers = {'HTTP_AUTHORIZATION': f'Bearer {token}'}

        self.course = Curs.objects.create(
            title="test_course",
        )

        # Создаем тестовый урок
        self.lesson = Lesson.objects.create(
            title="Test Lesson",
            description="This is a test lesson",
            user=self.user
        )

    def test_create_lesson(self):
        """
        Тест операции создания (create) проверки создания уроков
        """
        data = {
            "title": "test",
            "curs": 1,
            "description": "test description"
        }
        create_lesson = reverse('lessons:lesson-create')
        response = self.client.post(create_lesson, data, format='json', **self.headers)
        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['title'], data['title'])

    def test_retrieve_lesson(self):
        """
        Тест операции чтения (retrieve) урока
        """
        retrieve_url = reverse('lessons:lesson-retrieve', args=[self.lesson.id])
        response = self.client.get(retrieve_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.lesson.title)

    def test_update_lesson(self):
        # Тест операции обновления (update) урока
        update_url = reverse('lessons:lesson-update', args=[self.lesson.id])
        updated_data = {
            "title": "Updated Lesson",
            "description": "This is an updated lesson",
        }
        response = self.client.patch(update_url, updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.title, updated_data['title'])
        self.assertEqual(self.lesson.description, updated_data['description'])

    def test_delete_lesson(self):
        # Тест операции удаления (delete) урока
        delete_url = reverse('lessons:lesson-delete', args=[self.lesson.id])
        response = self.client.delete(delete_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lesson.objects.filter(id=self.lesson.id).exists())

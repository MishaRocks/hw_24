from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from curses.models import Curs
from subscribes.models import Subscribe
from users.models import User


class CursSubscriptionTestCase(APITestCase):
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

        self.curs = Curs.objects.create(
            title="test_course",
        )

    def test_subscribe_to_curs(self):
        """
        Тест операции создания подписки на курс
        """
        subscribe_url = reverse('subscribes:Subscribe-create', args=[self.curs.id])
        response = self.client.post(subscribe_url, {}, format='json', **self.headers)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['detail'], "Подписка успешно установлена.")

    def test_subscribe_to_curs_twice(self):
        """
        Тест, чтобы проверить, что пользователь не может подписаться на один курс дважды
        """
        Subscribe.objects.create(user=self.user, curs=self.curs)  # Создаем подписку
        subscribe_url = reverse('subscribes:Subscribe-create', args=[self.curs.id])
        response = self.client.post(subscribe_url, {}, format='json', **self.headers)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], "Вы уже подписаны на этот курс.")


class CourseUnsubscribeTestCase(APITestCase):
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

        self.curs = Curs.objects.create(
            title="test_course",
        )
        self.curs_subscription = Subscribe.objects.create(user=self.user, curs=self.curs)

    # def test_unsubscribe_from_course(self):
    #     """
    #     Тест операции отписки от курса
    #     """
    #     unsubscribe_url = reverse('subscribes:Subscribe-delete', args=[self.curs.id])
    #     response = self.client.delete(unsubscribe_url, format='json', **self.headers)
    #
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     self.assertFalse(Subscribe.objects.filter(id=self.curs_subscription.id, is_active=True).exists())

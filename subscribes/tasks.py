from celery import shared_task
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response


@shared_task
def send_subscription_notification(user_email, curs_title):
    subject = 'Вы успешно подписались на курс'
    message = f'Вы успешно подписались на курс "{curs_title}". Спасибо за подписку!'
    from_email = None
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list)


@shared_task
def send_unsubscription_notification(user_email, curs_title):
    subject = 'Вы успешно отписались от курса'
    message = (f'Вы успешно отписались от курса "{curs_title}". '
               f'Мы надеемся, что вы найдете другие интересные курсы у нас!')
    from_email = None
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)


@shared_task
def send_course_update_notification(curs_title, user_emails):
    subject = 'Обновление курса'
    message = f'Курс "{curs_title}" был обновлен. Проверьте новый материал!'
    from_email = None
    recipient_list = user_emails  # Список адресов получателей

    send_mail(subject, message, from_email, recipient_list)
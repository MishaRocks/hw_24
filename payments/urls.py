from django.urls import path

from payments.views import PaymentCreateAPIView, PaymentListAPIView, PaymentSuccessAPIView, PaymentCancelAPIView

urlpatterns = [
    path('create/', PaymentCreateAPIView.as_view(), name='payment-create'),
    path('', PaymentListAPIView.as_view(), name='payment-list'),
    path('api/payment/success/', PaymentSuccessAPIView.as_view(), name='success'),
    path('api/payment/cancel/', PaymentCancelAPIView.as_view(), name='cancel'),
]

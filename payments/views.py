from django_filters.rest_framework import DjangoFilterBackend
from requests import Response
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from payments.models import Payment
from payments.serializers import PaymentSerializer, PaymentCreateSerializer


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('pay_date', 'curs', 'lesson', 'pay_sum', 'pay_method')


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentCreateSerializer
    permission_classes = [AllowAny]


class PaymentSuccessAPIView(APIView):
    @staticmethod
    def get(request):
        verify_payment_number = request.query_params.get('verify_payment_number')
        payment = get_object_or_404(Payment, verify_payment_number=verify_payment_number)

        payment.status = Payment.Status.SUCCESS
        payment.save()

        response_data = {'message': 'Payment successful'}
        return Response(response_data, status=status.HTTP_200_OK)


class PaymentCancelAPIView(APIView):
    @staticmethod
    def get(request):
        verify_payment_number = request.query_params.get('verify_payment_number')
        payment = get_object_or_404(Payment, verify_payment_number=verify_payment_number)

        payment.status = Payment.Status.CANCEL
        payment.save()

        response_data = {'message': 'Payment canceled'}

        return Response(response_data, status=status.HTTP_200_OK)

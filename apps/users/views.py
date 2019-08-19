import logging
from datetime import datetime, timedelta

from django.db import transaction
from django.utils.translation import ugettext_lazy as _
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.bookings.models import CleanerBookings
from apps.bookings.serializers import CleanerBookingsSerializer
from apps.users.constants import UserType
from apps.users.models import User
from apps.users.serializers import UserSerializer, CustomerUserSerializer

logger = logging.getLogger(__name__)


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }


@api_view(['POST'])
def manage_cleaner(request):
    try:
        logger.info('Request to register new cleaner')
        request_data = request.data.copy()
        serializer = UserSerializer(data=request_data)
        if not serializer.is_valid():
            errors = dict(serializer.errors)
            field = list(errors.keys())[0]
            message = "%s - %s" % (field, errors[field][0])
            return Response(
                {'message': message},
                status=status.HTTP_400_BAD_REQUEST
            )
        instance = serializer.save(user_type=UserType.CLEANER)
        return Response(
            UserSerializer(instance=instance, remove_fields=['password']).data,
            status=status.HTTP_200_OK
        )
    except Exception as e:
        print(str(e))
        logger.debug('Exception caught in file {}'.format(__file__), exc_info=True)
        return Response(
            {'message': _('Something went wrong !')},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['POST'])
def manage_customer(request):
    try:
        request_data = request.data.copy()
        serializer = CustomerUserSerializer(data=request_data)
        if not serializer.is_valid():
            errors = dict(serializer.errors)
            field = list(errors.keys())[0]
            message = "%s - %s" % (field, errors[field][0])
            return Response(
                {'message': message},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = serializer.validated_data
        phone = data.get('phone')
        booking_time = data.get('booking_time')
        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            instance = serializer.save(user_type=UserType.CLEANER)
            user = instance
        # TODO  logic for checking bookings conflicts
        bookings = CleanerBookings.objects.filter(booking_starttime=booking_time)
        cleaners_engaged = bookings.values_list('cleaner__id')
        cleaners = User.objects.filter(
            city=data.get('city'),
            user_type=UserType.CLEANER).exclude(id__in=cleaners_engaged)
        if cleaners.count() > 0:
            instance = CleanerBookings.objects.create(
                booking_starttime=booking_time,
                booking_endtime=booking_time + timedelta(hours=1),
                cleaner=cleaners.first(),
                customer=user
            )
            return Response(
                CleanerBookingsSerializer(instance=instance).data,
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'message': 'No cleaner is free at  specified time'},
                status=status.HTTP_400_BAD_REQUEST
            )
    except Exception as e:
        print(str(e))
        logger.debug('Exception caught in file {}'.format(__file__), exc_info=True)
        return Response(
            {'message': _('Something went wrong !')},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
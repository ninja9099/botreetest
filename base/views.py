import logging

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils.translation import ugettext_lazy as _
from base.models import Country
from base.serializers import CountrySerializers

logger = logging.getLogger(__name__)


@api_view(['GET'])
def get_cities(request):
    try:
        queryset = Country.objects.filter(active=True)
        serializer = CountrySerializers(instance=queryset, many=True)
        logger.info('User %s has requested to get list of all cities' % request.user)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    except Exception as e:
        print(str(e))
        logger.debug('Exception caught in file {}'.format(__file__), exc_info=True)
        return Response(
            {'message': _('Something went wrong !')},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

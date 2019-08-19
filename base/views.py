import logging

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from base.models import Country
from base.serializers import CountrySerializers

logger = logging.getLogger(__name__)


@api_view(['GET'])
# @permission_classes((IsAuthenticated,))
def get_cities(request):
    try:
        import pdb
        pdb.set_trace()
        queryset = Country.objects.filter(is_active=True)
        serializer = CountrySerializers(instance=queryset, many=True)
        logger.info('User %s has requested to get list of all cities' % request.user)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    #     Logic for getting cities
    except:
        logger.debug('Exception caught in file {}'.format(__file__), exc_info=True)

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

from app.models import InfoFam
from app.api.serializers import InfoFamSerializer

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# @api_view(['POST',])



# def api_index(request):
#
#     info_fam = InfoFam(ip=get_client_ip(request))
#
#     if request.method == "POST":
#         serializer = InfoFamSerializer(info_fam, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InfoFamViewSet(viewsets.ModelViewSet):
    queryset = InfoFam.objects.all()
    serializer_class = InfoFamSerializer

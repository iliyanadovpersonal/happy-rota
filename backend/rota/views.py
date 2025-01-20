from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Rota, RotaRow
from .serializers import RotaSerializer

@api_view(['GET'])
def fetch_rota(request):
    rota = Rota.objects.all().order_by('date')
    serializer = RotaSerializer(rota, many=True)
    return Response(serializer.data)

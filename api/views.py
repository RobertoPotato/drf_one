from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import ItemModel
from .serializers import ItemModelSerializer

@api_view(['GET'])
def getData(request):
    items = ItemModel.objects.all()
    serializer = ItemModelSerializer(items, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def addItem(request):
    serializer = ItemModelSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
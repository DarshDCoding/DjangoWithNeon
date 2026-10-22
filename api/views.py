from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, mixins, generics

from testing.models import Product
from .serializers import ProductSerializer

# Create your views here.
@api_view(["GET"])
def test_endpoint(request):
    return Response({"message":"Everything Works"}, status=status.HTTP_200_OK)

class ProductView(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetails(generics.RetrieveUpdateDestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
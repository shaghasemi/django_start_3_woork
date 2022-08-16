from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save()
        # print(serializer.validated_data)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content")
        # or None
        if content is None:
            content = title
        serializer.save(content=content)


product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_detail_view = ProductDetailAPIView.as_view()


@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            # Default View
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, data=request.data)
            return Response(data)
        # List View
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    if method == 'POST':
        # Create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "Not good data"}, status=400)

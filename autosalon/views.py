from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


from .serializers import UserSerializer, CarModelSerializer, OrderSerializer
from .models import User, CarModel, Order


class UserListView(APIView):
    @swagger_auto_schema(responses={200: UserSerializer(many=True)})
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True, read_only=True)

        return Response(
            {
                'result': 'success',
                'data': serializer.data
            }, status=status.HTTP_200_OK
        )

    @swagger_auto_schema(request_body=UserSerializer, responses={200: UserSerializer})
    def post(self, requeest):
        serializer = UserSerializer(data=requeest.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarModelListView(APIView):
    @swagger_auto_schema(responses={200: CarModelSerializer(many=True)})
    def get(self, request):
        cars = CarModel.objects.all()
        serializer = CarModelSerializer(cars, many=True, read_only=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CarModelSerializer, responses={200: CarModelSerializer})
    def post(self, requeest):
        serializer = CarModelSerializer(data=requeest.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderListView(APIView):
    @swagger_auto_schema(responses={200: OrderSerializer(many=True)})
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=OrderSerializer, responses={200: OrderSerializer})
    def post(self, requeest):
        serializer = OrderSerializer(data=requeest.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(APIView):
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={200: OrderSerializer})
    def get(self, pk):
        task = self.get_object(pk)
        serializer = OrderSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=OrderSerializer, responses={200: OrderSerializer})
    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = OrderSerializer(task, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        task = self.get_object(pk)
        task.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
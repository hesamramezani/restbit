from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView , ListAPIView , RetrieveUpdateDestroyAPIView
from .models import connection_model , crypto_model , mobile_number_model , price_model
from .serializer import connection_model_serializer , user_serializer , crypto_serializer , \
    mobile_number_serializer , price_serializer
from rest_framework.permissions import IsAdminUser , IsAuthenticated
from django.contrib.auth.models import User
from .permission import IsSuperUser , IsOwner
from rest_framework.response import Response
import cryptocompare
import json
from kavenegar import *


class create_connection(CreateAPIView):
    queryset = connection_model.objects.all()
    serializer_class = connection_model_serializer

class list_connection(ListAPIView):
    queryset = connection_model.objects.all()
    serializer_class = connection_model_serializer
    permission_classes = (IsAdminUser,)

class create_user(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = user_serializer

class list_user(ListAPIView):
    queryset = User.objects.all()
    serializer_class = user_serializer
    permission_classes = (IsSuperUser,)



class crypto_list(ListAPIView):
    queryset = crypto_model.objects.all()
    serializer_class = crypto_serializer
    permission_classes = (IsSuperUser,)

class crypto(APIView):

    def get (self , request , pk):
        queryset = crypto_model.objects.get(pk = pk)
        serializer = crypto_serializer(queryset)
        return Response(serializer.data)

    def delete (self , request , pk):
        queryset = crypto_model.objects.get(pk = pk)
        queryset.delete()
        return Response(status=201)

    def put(self , request , pk):
        queryset = crypto_model.objects.get(pk = pk)
        serializer = crypto_serializer(queryset , request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=202)
        else:
            return Response(status=404)

    permission_classes = (IsAuthenticated , IsOwner)

class create_crypto(CreateAPIView):
    queryset = crypto_model.objects.all()
    serializer_class = crypto_serializer
    permission_classes = (IsAuthenticated,)


class create_number(CreateAPIView):
    queryset = mobile_number_model.objects.all()
    serializer_class = mobile_number_serializer
    permission_classes = (IsAuthenticated,)

class editdelete_number(RetrieveUpdateDestroyAPIView):
    queryset = mobile_number_model.objects.all()
    serializer_class = mobile_number_serializer
    permission_classes = (IsAuthenticated,)

class create_price(CreateAPIView):
    queryset = price_model.objects.all()
    serializer_class = price_serializer
    permission_classes = (IsAuthenticated,)

class price(APIView):
    def get(self , request , pk):
        queryset = price_model.objects.get(pk = pk)
        serializer = price_serializer(queryset)
        return Response(serializer.data , status=202)

    def put(self , request , pk):
        queryset = price_model.objects.get(pk=pk)
        print(queryset)
        serializer = price_serializer(queryset, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=202)
        else:
            return Response(serializer.errors , status=404)

    def delete(self , request , pk):
        queryset = price_model.objects.get(pk=pk)
        queryset.delete()
        return Response(status=201)

    permission_classes = (IsAuthenticated , IsOwner)

class kavenegar(APIView):

    def get(self , request , pk):
        queryset = price_model.objects.get(pk = pk)
        serializer = price_serializer(queryset)
        return Response(serializer.data , status=202)

    def post(self , request , pk):
        queryset = price_model.objects.get(pk=pk)
        hi = User.objects.get(pk = pk)
        query = crypto_model.objects.get(pk = hi.pk)
        serializer = crypto_serializer(query)
        serializer1 = price_serializer(queryset)
        field = serializer.data["field"]
        print(field)

        for i in field:
            crypto = cryptocompare.get_price(str(i) , currency="USD")
            main_price = crypto[i]   # the price of crypto we get from library
            print("===================")
            mainnn = main_price["USD"]
            print("===================")
            print(i)
            user_price = serializer1.data[i]
            print(user_price)    # user chose his price
            query_number = mobile_number_model.objects.get(pk=pk)
            serializer_number = mobile_number_serializer(query_number)
            user_number = serializer_number.data["mobile"]
            print(user_number)
            if int(user_price) >= int(mainnn):
                try:
                    import json
                except ImportError:
                    import simplejson as json
                try:
                    api_key = "7445745248683759756C754235376B667773706B2B42702B6E62666D6872506B48474D72487750584230493D"
                    api = KavenegarAPI(api_key)
                    params = {
                        'sender': '10004346',
                        'receptor': str(user_number) ,
                        'message': 'قیمت ارزی که انتخاب کردی به حد نساب رسید '
                    }
                    response = api.sms_send(params)
                    print(str(response))
                except APIException as e:
                    print(str(e))
                except HTTPException as e:
                    print(str(e))

        return Response(serializer1.data , status=202)

    permission_classes = (IsAuthenticated , IsOwner)


class revoke(APIView):             # for delete access from db

    def delete(self , request):
        request.auth.delete()
        return Response(status=201)

    permission_classes = (IsAuthenticated,)

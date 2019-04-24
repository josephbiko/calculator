from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .serializers import UrlSerializer
from .models import UrlModel
from django.shortcuts import get_object_or_404

class UrlViewset(APIView):
    def get(self,request,pk=-1):
        if not pk:
            s = UrlSerializer(UrlModel.objects.all(),many=True)
            return Response(status=200,data=s.data)
        url = get_object_or_404(UrlModel,pk=pk)
        s = UrlSerializer(url)
        return Response(status=301,data=s.data)

    def post(self,request,pk=None):
        print(request.data)
        s = UrlSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        s.save()
        return Response(status=201,data=s.data)

    def delete(self,request,pk = -1):
        if not pk:
            UrlModel.objects.all().delete()
        else:
            get_object_or_404(UrlModel, pk=pk).delete()
        return Response(status=204)

    def put(self,request,pk=None):
        if not pk:
            return Response(status=404)

        url = get_object_or_404(UrlModel, pk=pk)
        s = UrlSerializer(url,data=request.data)
        s.is_valid(raise_exception=True)
        s.save()
        return Response(status=201,data=s.data)




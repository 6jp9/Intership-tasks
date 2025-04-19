from django.shortcuts import render
from django.views.generic import View
import io
from rest_framework.parsers import JSONParser
from testapp.models import Test
from testapp.serializers import TestSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name='dispatch')
class TestCRUD(View):
    def get(self, request, *args, **kwargs):
        if request.body:
            stream = io.BytesIO(request.body)
            pdata = JSONParser().parse(stream)
            id = pdata.get('id', None)
            if id is not None and Test.objects.filter(id=id).exists():
                data = Test.objects.get(id=id)
                serializer = TestSerializer(data)
                jdata = JSONRenderer().render(serializer.data)
                return HttpResponse(jdata, content_type='application/json', status=200)
            

        print('id does not exist or not given')
        qs = Test.objects.all()
        serializer = TestSerializer(qs, many=True)
        jdata = JSONRenderer().render(serializer.data)
        return HttpResponse(jdata, content_type='application/json')
    

    def post(self,request,*args):
        if request.body:
            stream = io.BytesIO(request.body)
            pdata = JSONParser().parse(stream)
            serializer = TestSerializer(data = pdata)
            if serializer.is_valid():
                serializer.save()
                msg = {'msg':'record created........'}
                jdata = JSONRenderer().render(msg)
                return HttpResponse(jdata,content_type = 'application/json')
            jdata = JSONRenderer().render(serializer.errors)
            return HttpResponse(jdata,content_type = 'application/json',status=400)
        
    def put(self,request):
        if request.body:
            stream = io.BytesIO(request.body)
            pdata = JSONParser().parse(stream)
            id = pdata.get('id')
            tdata = Test.objects.get(id=id)
            serializers = TestSerializer(tdata,data=pdata)
            if serializers.is_valid():
                serializers.save()
                msg = {'msg':'data updated....'}
                jdata = JSONRenderer().render(msg)
                return HttpResponse(jdata,content_type = 'application/json',status=400)
            jdata = JSONRenderer().render(serializers.errors)
            return HttpResponse(jdata,content_type = 'application/json',status=400)
    
    def delete(self,request):
        if request.body:
            stream = io.BytesIO(request.body)
            pdata = JSONParser().parse(stream)
            id = pdata.get('id')
            data = Test.objects.get(id=id)
            data.delete()
            msg = {'msg':'record deleted....'}
            jdata = JSONRenderer().render(msg)
            return HttpResponse(jdata,content_type = 'application/json',status=400)
        

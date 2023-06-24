from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import*
# Create your views here.
class NotificationView(APIView):
    def get(self, request):
        queryset = NotificationModel.objects.all()
        serializer = NotificationSerializer(queryset, many=True)  # Pass queryset as data, and specify many=True
        return Response({"data": serializer.data, "message": "successfully"})
    def post(self,request):
        data =request.data
        serializer = NotificationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':200, "data":serializer.data,"message":"successfully"})
        return Response({"status":403,'data':serializer.errors,'message':"somehing went wrong"})
    def put(self,request):
        try:
            queryset = NotificationModel.objects.get(id=request.data['id'])
            serializer = NotificationSerializer(queryset,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':200,"data":serializer.data,'message':'update successfully'})
            return Response({'status':403,'data':serializer.errors,'message':"something wen wrong"})
        except:
            return Response({'status':401,'message':"failed"})
        
    def patch(self, request):
        try:
            instance = NotificationModel.objects.get(id=request.data['id'])
            serializer = NotificationSerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": 200, "data": serializer.data, "message": "Update successful"})
            return Response({"status": 400, "message": "Validation error", "data": serializer.errors})
        except NotificationModel.DoesNotExist:
            return Response({"status": 404, "message": "Notification not found"})
        
    def delete(self,request):
        try:
            instance = NotificationModel.objects.get(id=request.data['id'])
            instance.delete()
            return Response({'data':"you deleted successfully"})
        except:
            return Response({'data':"sorry this object is not found"})



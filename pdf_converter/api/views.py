from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import datetime
from .helpers import * 

# JWT Authentication
from rest_framework_simplejwt.authentication import JWTAuthentication

# JWT token creating manually 

from rest_framework_simplejwt.tokens import RefreshToken 

class studentapi(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        student_obj=student.objects.all()
        serializer = studentSerializers(student_obj,many=True)
        return Response({'status' : 200,'Load' : serializer.data})

    # GENERATE MANUALY TOKEN
    '''def post(self,request):
        serializer=UserSerializer(data=request.data)
        if not serializer.is_valid():
            Response({"status":405,"Error":serializer.errors,"message":"error found"})
        
        user=User.objects.get(username=serializer.data['username'])
        token_obj , _ =Token.objects.get_or_create(user=user)
        Response({"status":200,"payload":serializer.data,"token":str(token_obj)})'''

    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if not serializer.is_valid():
            Response({"status":405,"Error":serializer.errors,"message":"error found"})
        serializer.save()
        user=User.objects.get(username=serializer.data['username'])
        refresh = RefreshToken.for_user(user)
        Response({"status":200,"payload":serializer.data,'refresh': str(refresh),
        'access': str(refresh.access_token)})

    def patch(self,request):
        try:
            student_obj=student.objects.get(name=request.data['name'])
            serializer=studentSerializers(student_obj,data=request.data,partial=True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403,'error':serializer.errors,'message':'something invalid'})
            serializer.save()
            return Response({'status' : 200,'Load' : serializer.data,'message':'data updated'})
        except Exception as e:
            return Response({'status':403,'message':'invalid name'})
    

    def put(self,request):
        stu_obj=student.objects.get(name=request.data['name'])
        serializer=studentSerializers(data=request.data)
        if not serializer.is_valid():
            return Response({'status':403,'error':serializer.errors,'messsage':'something going wrong'})
        serializer.save()
        return Response({'status':200,'message':'sucessfuly updated'})

    def delete(self,request):
        try:
            stu_obj=student.objects.get(name=request.data['name'])
            stu_obj.delete()
            return Response({'status':200,'message':'success'})

        except Exception as e:
            return Response({'status':403,'message':"something went wrong "})
    
   
# GENRIC VIEW
from rest_framework import generics

class studentGenric(generics.ListAPIView,generics.CreateAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializers

class studentGenric2(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializers
    lookup_field='name'

@api_view(['GET'])
def get_book(request):
    book_obj=Book.objects.all()
    serializer=booksterializer(book_obj,many=True)
    return Response({"status":200,"payload":serializer.data})

    
'''class GeneratePdf(APIView):
    def get(self,request):
        student_objs=student.objects.all()
        params={
            'today':datetime.date.today(),
            'student_objs':student_objs
        }
        file_name,status=save_pdf(params)
        if not status:
            return Response({"status":400})
        return Response({"status":200,'path':f'/media/{file_name}.pdf'})'''

# GENERATE PDF FROM HTML DOCUMENT DATA 

class GeneratePdf(APIView):
    def get(self,request):
        student_objs=student.objects.all()
        params={
            'today':datetime.date.today(),
            'student_objs':student_objs
        }

        file_name,status=save_pdf(params)
        if not status:
            return Response({"status":400})
        return Response({"status":200,"path":f'/media/{file_name}.pdf'})

# TO CONVERT DATA INTO EXCEL FILE USING PANDAS
import pandas as pd
import uuid
from django.conf import settings

class Excelfiles(APIView):
    def get(self,requets):
        student_objs=student.objects.all()
        serializer=studentSerializers(student_objs,many=True)
        df=pd.DataFrame(serializer.data)
        print(df)
        file_name=uuid.uuid4()
        
        df.to_csv(f'media/excel/{file_name}.csv',encoding='UTF-8',index=False)
        return Response({'status':200,"response":df})

    def post(self,request):
        excel_obj=excel_export.objects.create(excel=request.FILES['files'])
        df=pd.read_csv(f'{settings.BASE_DIR}/media/excel/{excel_obj.excel}')
        print(df.values.tolist())
        return Response({"status":200})
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from users.models import AddBookModel, CheckInModel, User, AddLibraryModel
from users.serializer import AddBookSerializer, AddLibrarySerializer, CheckInSerializer, UserSerializer
import jwt,datetime # type: ignore

# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def get(self, request):
        return Response()

class LoginView(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email = email).first()
        print(user.id, email,password)

        if user is None:
            raise AuthenticationFailed('User not found')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')
        payload = {
            "id":user.id,
            "exp":datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat":datetime.datetime.utcnow(),
            "subject": user.id,
            "role": user.usertype,
            "fname": user.fname ,
            "lname":user.lname,
            "libraryname": user.library_name
        }
        token = jwt.encode(payload,'secret',algorithm='HS256')
        response =  Response({
            'token':token.encode('utf-8'),
            'payload':payload
        })
        return response

class AddLibrary(APIView):
    def post(self,request):
        serializer = AddLibrarySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def get(self,request):
        addlibrary = AddLibraryModel.objects.all()
        data = list(addlibrary.values())
        return JsonResponse(data, safe=False)

class AddBook(APIView):
    def post(self,request):
        serializer = AddBookSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def get(self,request):
        addbook = AddBookModel.objects.all()
        data = list(addbook.values())
        return JsonResponse(data, safe=False)

class CheckIn(APIView):
    def post(self,request):
        bookrecord = AddBookModel.objects.get(id = request.data['bookId'])
        bookrecord.quantity = bookrecord.quantity - request.data['selectedquantity']
        request.data['quantity'] = request.data['selectedquantity']
        bookrecord.save()
        print(bookrecord.quantity)
        serializer = CheckInSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def get(self,request):
        checkin = CheckInModel.objects.all()
        data = list(checkin.values())
        return JsonResponse(data, safe=False)

class ReturnBook(APIView):
    def post(self,request):
        bookrecord = AddBookModel.objects.get(id = request.data['bookId'])
        bookrecord.quantity = bookrecord.quantity + request.data['quantity']
        bookrecord.save()
        returnrecord = CheckInModel.objects.get(id = request.data['id'])
        returnrecord.status = 'Returned'
        returnrecord.save()
        return Response("Data Saved")
    def get(self,request):
        checkin = CheckInModel.objects.all()
        data = list(checkin.values())
        return JsonResponse(data, safe=False)
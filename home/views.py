from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
@api_view(['GET'])
def get_book(request):
    book_obj = Book.objects.all()
    serializer = BookSerializer(book_obj, many=True)
    return Response({'status': 200, 'payload': serializer.data})


# registration
class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong...'})
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        # token_obj, _ = Token.objects.get_or_create(user=user)
        refresh = RefreshToken.for_user(user)
        return Response(
            {'status': 200, 'payload': serializer.data, 'refresh': str(refresh),'access': str(refresh.access_token),
             'message': 'New user record has been created...'})

        """
        return Response(
            {'status': 200, 'payload': serializer.data, 'token': str(token_obj), 'message': 'New user record '
                                                                                            'has been '
                                                                                            'created...'})
        """

class StudentAPI(APIView):
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        student_obj = Student.objects.all()
        serializer = StudentSerializer(student_obj, many=True)
        print(request.user)
        # print(serializer.data)
        return Response({'status': 200, 'payload': serializer.data})

    def post(self, request):
        data = request.data
        # print(data)
        serializer = StudentSerializer(data=request.data)
        if request.data['age'] < 18:
            return Response({"status": 403, 'message': 'age must be >18'})
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong...'})
        serializer.save()
        return Response({'status': 200, 'payload': serializer.data, 'message': 'New user record has been created...'})

    def put(self, request):
        try:
            student_obj = Student.objects.get(id=request.data['id'])
            serializer = StudentSerializer(student_obj, data=request.data)
            # request methods
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong...'})

            serializer.save()
            return Response({'status': 200, 'payload': serializer.data, 'message': 'Your data is updated...'})
        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': 'invalid id'})

    def patch(self, request):
        try:
            student_obj = Student.objects.get(id=request.data['id'])
            serializer = StudentSerializer(student_obj, data=request.data,
                                           partial=True)  # if you are adding partial=True put methods became patch
            # request methods
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong...'})

            serializer.save()
            return Response({'status': 200, 'payload': serializer.data, 'message': 'Your data is updated...'})
        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': 'invalid id'})

    def delete(self, request):
        try:
            sid = request.GET.get('id')
            student_obj = Student.objects.get(id=sid)
            student_obj.delete()
            return Response({'status': 200, 'message': 'Student record deleted successfully'})
        except Student.DoesNotExist:
            return Response({'status': 404, 'message': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'status': 500, 'message': f'An error occurred: {str(e)}'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# @api_view(['GET'])
# def get_student(request):
#     student_obj = Student.objects.all()
#     serializer = StudentSerializer(student_obj, many=True)
#     print(serializer.data)
#     return Response({'status': 200, 'payload': serializer.data})
#
#
# @api_view(['POST'])
# def post_student(request):
#     data = request.data
#     # print(data)
#     serializer = StudentSerializer(data=request.data)
#     # if request.data['age'] < 18:
#     #     return Response({"status": 403, 'message': 'age must be >18'})
#
#     if not serializer.is_valid():
#         print(serializer.errors)
#         return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong...'})
#
#     serializer.save()
#
#     return Response({'status': 200, 'payload': serializer.data, 'message': 'New user record has been created...'})
#
#
# @api_view(["PUT"])
# def update_student(request, id):
#     try:
#         student_obj = Student.objects.get(id=id)
#         serializer = StudentSerializer(student_obj, data=request.data,
#                                        partial=True)  # if you are adding partial=True put methods became patch request methods
#         if not serializer.is_valid():
#             print(serializer.errors)
#             return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong...'})
#
#         serializer.save()
#     except Exception as e:
#         return Response({'status': 403, 'message': 'invalid id'})
#
#     return Response({'status': 200, 'payload': serializer.data, 'message': 'New user record has been created...'})
#
#
# # def delete_student(request, id):
# @api_view(['DELETE'])
# def delete_student(request):
#     try:
#         sid = request.GET.get('id')
#         student_obj = Student.objects.get(id=sid)
#         student_obj.delete()
#         return Response({'status': 200, 'message': 'Student record deleted successfully'})
#     except Student.DoesNotExist:
#         return Response({'status': 404, 'message': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
#     except Exception as e:
#         return Response({'status': 500, 'message': f'An error occurred: {str(e)}'},
#                         status=status.HTTP_500_INTERNAL_SERVER_ERROR)

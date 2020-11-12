from .models import Member,User
from rest_framework.response import Response
from rest_framework import generics,status,filters
from rest_framework.views import APIView,Http404
from .serializers import MemberSerializers,MembersSerializers,UsersSerializers,UserSerializers
from django_filters.rest_framework import DjangoFilterBackend

class search_user(generics.ListAPIView):
        queryset = User.objects.all()
        serializer_class = UsersSerializers
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['email_address','password']

class search_member(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MembersSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_number']


class user_list(APIView):
    def get(self,request,format=None):
        all_users = User.objects.all()
        serializers = UsersSerializers(all_users,many=True)
        return Response(serializers.data)
    
    def post(self,request,format=None):
        serializers = UsersSerializers(data=request.data)
        if serializers.is_valid:
            serializers.save
            return Response(serializers.data,status=status.HTTP_200_CREATED)
        else :
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class single_user(APIView):
    
    def get_user(self,pk):
        try:
            return User.objects.get(pk = pk)
        except Member.DoesNotExist:
            return Http404

    def get(self,request,pk,format=None):
        user = self.get_user(pk)
        serializers = UserSerializers(user)
        return Response(serializers.data)



class new_member(APIView):
    def post(self,request,format=None):
        serializers = MembersSerializers(data=request.data)
        if serializers.is_valid:
            serializers.save
            return Response(serializers.data,status = status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors,status = status.HTTP_400_BAD_REQUEST)


class single_member(APIView):
    def get_member(self,pk):
        try:
            return Member.objects.get(pk = pk)
        except Member.DoesNotExist:
            return Http404


    def get(self,request,pk,format=None):
        member = self.get_member(pk)
        serializers = MemberSerializers(member)
        return Response(serializers.data)

    def delete(self,request,pk,format=None):
        member = self.get_member(pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self,request,pk,format=None):
        member = self.get_member(pk)
        serializers = MemberSerializers(member,request.data)
        if serializers.is_valid:
            serializers.save()
            return Response(serializers.data)
        else :
            return Response(serializers.errors,status = status.HTTP_400_BAD_REQUEST)


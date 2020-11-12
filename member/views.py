from .models import Member
from rest_framework import generics,status,filters
from rest_framework.views import APIView,Response,Http404
from .serializers import MemberSerializers,MembersSerializers,UserSerializers


class member_list(APIView):
    def get(self,request,format=None):
        all_members = Member.objects.all()
        serializers = MembersSerializers(all_members,many=True)
        return Response(serializers.data)

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

    def put(self,request,pk,format=None):
        member = self.get_member(pk)
        serializers = MemberSerializers(member,request.data)
        if serializers.is_valid:
            serializers.save()
            return Response(serializers.data)
        else :
            return Response(serializers.errors,status = status.HTTP_400_BAD_REQUEST)


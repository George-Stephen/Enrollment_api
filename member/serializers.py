from rest_framework import serializers
from .models import Member,User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username","email_address","password")

class MembersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ("member_image","id_number","title","first_name","middle_name","last_name","gender","birthday","email_address","email_address","phone_number","address","status")

class MemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ("id","member_image","id_number","title","first_name","middle_name","last_name","gender","birthday","email_address","email_address","phone_number","address","status")
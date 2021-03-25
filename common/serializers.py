from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator
from rest_framework.validators import ValidationError

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'
        # validators  = [
        #     UniqueValidator(
        #         queryset=Site.objects.filter(),
        #         message="LỖI RỒI DM MÀY",
        #         lookup="name"
        #     )
        #
        # ]
        # validators = []
    def validate(self, data):
        """
        Check that the blog post is about Django.
        """
        if 'django' not in data['name']:
            raise serializers.ValidationError("Blog post is not about Django")
        return value

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class StatusBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusBill
        fields = '__all__'


class TypeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeProduct
        fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all_'

class RolePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolePermission
        fields = '__all__'

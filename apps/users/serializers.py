import re
from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'city', 'password', 'phone')

    def __init__(self, *args, **kwargs):
        remove_fields = kwargs.pop('remove_fields', None)
        only_fields = kwargs.pop('only_fields', None)
        super(UserSerializer, self).__init__(*args, **kwargs)

        if remove_fields:
            for field_name in remove_fields:
                self.fields.pop(field_name)

    def validate(self, attrs):
        phone = attrs.get('phone')
        ph_nbr_pattern = r'^(\d{10})(?:\s|$)'
        compile_obj = re.compile(ph_nbr_pattern)
        match_obj = compile_obj.search(phone)
        if not match_obj:
            raise serializers.ValidationError({'phone': 'Phone number is not valid'})
        return attrs

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
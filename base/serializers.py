
from rest_framework import serializers
from base.models import Country, City, State


class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name',)


class StateSerializers(serializers.ModelSerializer):
    cities = CitySerializers(source='city_set', many=True, read_only=True)

    class Meta:
        model = State
        fields = ('id', 'name', 'cities')


class CountrySerializers(serializers.ModelSerializer):
    states = StateSerializers(source='state_set', many=True, read_only=True)

    class Meta:
        model = Country
        fields = ('id', 'name', 'states')

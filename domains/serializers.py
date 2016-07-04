from rest_framework import serializers
from .models import Domain
from .models import SubDomain


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ('name', 'expire', 'created_at', 'updated_at')


class SubDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ('domain', 'owner', 'share', 'created_at', 'updated_at')
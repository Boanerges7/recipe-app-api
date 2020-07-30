"""Import some modules."""
from rest_framework import serializers

from core.models import Tag


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag object."""

    class Meta:
        """Define some data."""

        model = Tag
        fields = ('id', 'name')
        read_only_Fields = ('id',)

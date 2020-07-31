"""Import some modules."""
from rest_framework import serializers

from core.models import Tag, Ingredient


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag object."""

    class Meta:
        """Define some data."""

        model = Tag
        fields = ('id', 'name')
        read_only_Fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for an ingredient object."""

    class Meta:
        """Define model and fields used."""

        model = Ingredient
        fields = ('id', 'name')
        read_only_Fields = ('id',)

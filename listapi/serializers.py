from rest_framework import serializers
from lists.models import Item, List, User

class UserSerializer(serializers.ModelSerializer):
    lists = serializers.HyperlinkedIdentityField('lists', view_name='user-lists', lookup_field='username')

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'lists', )


class ListSerializer(serializers.ModelSerializer):
    creator = UserSerializer(required=False)
    items = serializers.HyperlinkedIdentityField('items', view_name='item-list')
    # author = serializers.HyperlinkedRelatedField(view_name='user-detail', lookup_field='username')

    def get_validation_exclusions(self):
        # Need to exclude `author` since we'll add that later based off the request
        exclusions = super(ListSerializer, self).get_validation_exclusions()
        return exclusions + ['creator']

    class Meta:
        model = List

class ItemSerializer(serializers.ModelSerializer):
    description = serializers.Field('item.description')

    class Meta:
        model = Item
from django.test import TestCase
from items.models import ItemInstance, ItemTag, ItemType, ItemTagValue

class TagTests(TestCase):
    fixtures = ['tags.json']

    def setUp(self):
        super(TagTests, self).setUp()
        self.tag = ItemTag.objects.get(pk=1)
        self.tag_value = ItemTagValue.objects.get(pk=1)

    def test_unicode_for_tag_name(self):
        self.assertEqual(str(self.tag_value), self.tag.key + ' - ' + self.tag_value.value)
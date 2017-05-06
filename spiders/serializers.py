from rest_framework import serializers
from spiders.models import NewHouse

#
# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#     def create(self, validated_data):
#         """
#         Create and return a new `NewHouse` instance, given the validated data.
#         """
#         return NewHouse.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance

class NewHouseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewHouse
        fields = ('id','name', 'supervision_bank', 'supervision_acount',
                  'project_state', 'address', 'dev_company', 'license_authority',
                  'sale_permit', 'license_key', 'online_saleable_area', 'online_saleable_flats',
                  'saleable_area', 'saleable_flats', 'sold_area', 'sold_flats',
                  'residential_area', 'residential_flats', 'sold_residential_area', 'sold_residential_flats',
                  'reserve_area', 'reserve_flats', 'saleable_parking_amount', 'saleable_garage_amount',
                  'sold_avg_price', 'districts', 'contact_phone', 'remark','created')


class NewHouseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewHouse
        fields = ('id','name', 'project_state', 'address','districts','created')

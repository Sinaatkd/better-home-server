from rest_framework import serializers

from estate_module.models import Estate, EstateProperty, EstateImage, EstateCategory



class EstatePropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = EstateProperty
        fields = ('icon', 'title')



class EstateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstateImage
        fields = ('image', )


class EstateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EstateCategory
        fields = ('title', 'slug')


class EstateSerializer(serializers.ModelSerializer):
    category = EstateCategorySerializer(many=True)
    images = EstateImageSerializer(many=True)
    estate_properties = EstatePropertySerializer(many=True)
    
    class Meta:
        model = Estate
        exclude = ('is_delete', 'created_at', 'last_updated_time')


class EstateCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        exclude = ('is_delete', 'created_at', 'last_updated_time')

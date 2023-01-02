from rest_framework import serializers

from estate_module.models import Estate, EstateProperty, EstateImage



class EstatePropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = EstateProperty
        fields = ('id', 'icon', 'title')



class EstateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstateImage
        fields = ('id', 'image')



class EstateSerializer(serializers.ModelSerializer):
    images = EstateImageSerializer(many=True)
    estate_properties = EstatePropertySerializer(many=True)
    
    class Meta:
        model = Estate
        exclude = ('is_delete', 'created_at', 'last_updated_time', 'fav_of_users')


class EstateCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        exclude = ('is_delete', 'created_at', 'last_updated_time', 'fav_of_users')

    
    def update(self, instance, validated_data):
        # check consultant special ad monthly quota
        # if the quota was over. Ad not change
        if not instance.is_special and (validated_data.get('is_special')):
            if instance.consultant.special_ad_monthly_quota > 0:
                instance.consultant.special_ad_monthly_quota -= 1
            else:
                raise serializers.ValidationError('سهمیه ی ماهانه ثبت آگهی ویژه شما به اتمام رسیده است.')

        # check consultant ladder ad monthly quota
        # if the quota was over. Ad not change
        if not instance.is_ladder and (validated_data.get('is_ladder')):
            if instance.consultant.ladder_monthly_quota > 0:
                instance.consultant.ladder_monthly_quota -= 1
            else:
                raise serializers.ValidationError('سهمیه ی ماهانه ثبت آگهی نردبون شما به اتمام رسیده است.')
        instance.consultant.save()
        return super().update(instance, validated_data)

    def create(self, validated_data):
        # check consultant ad monthly quota
        # if the quota was over. Ad not create
        if validated_data['consultant'].ad_monthly_quota <= 0:
            raise serializers.ValidationError('سهمیه ی ماهانه ثبت آگهی شما به اتمام رسیده است.')
        else: validated_data['consultant'].ad_monthly_quota -= 1
            
        # check consultant special ad monthly quota
        # if the quota was over. Ad not create
        if validated_data['is_special']:
            if validated_data['consultant'].special_ad_monthly_quota > 0:
                validated_data['consultant'].special_ad_monthly_quota -= 1
            else:
                raise serializers.ValidationError('سهمیه ی ماهانه ثبت آگهی ویژه شما به اتمام رسیده است.')

        # check consultant ladder ad monthly quota
        # if the quota was over. Ad not create
        if validated_data['is_ladder']:
            if validated_data['consultant'].ladder_monthly_quota > 0:
                validated_data['consultant'].ladder_monthly_quota -= 1
            else:
                raise serializers.ValidationError('سهمیه ی ماهانه ثبت آگهی نردبون شما به اتمام رسیده است.')
        validated_data['consultant'].save()
        return super().create(validated_data)
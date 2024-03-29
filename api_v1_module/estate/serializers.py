from django.contrib.auth import get_user_model
from django.utils.timezone import now

from rest_framework import serializers

from estate_module.models import Estate, EstateProperty, EstateImage, EstateRegion

from estate_module.utils import diff_between_two_dates

User = get_user_model()


class EstatePropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = EstateProperty
        fields = ('id', 'icon', 'title')



class EstateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstateImage
        fields = ('id', 'image')


class ConsultantSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'phone_number')


class EstateRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstateRegion
        exclude = ('is_delete', 'is_active', 'created_at', 'last_updated_time',)


class EstateSerializer(serializers.ModelSerializer):
    images = EstateImageSerializer(many=True)
    estate_properties = EstatePropertySerializer(many=True)
    consultant = ConsultantSerializer()
    region = EstateRegionSerializer()
    is_favorite = serializers.SerializerMethodField('is_fav')
    last_ladder_updated_time = serializers.SerializerMethodField()


    class Meta:
        model = Estate
        exclude = ('is_delete', 'created_at', 'last_updated_time', 'fav_of_users')

    def is_fav(self, estate):
        user = self.context['request'].user
        if user.fav_of_users.filter(id=estate.id).exists():
            return True
        return False
    
    def get_last_ladder_updated_time(self, obj):
        current = now()
        last_ladder_updated_time = obj.last_ladder_updated_time
        diff_dates = diff_between_two_dates(current, last_ladder_updated_time)
        if 0 < diff_dates.days < 30:
            return f'{diff_dates.days} روز پیش'
        elif 30 <= diff_dates.days < 365:
            return f'{int(diff_dates.days / 30)} ماه پیش'
        elif diff_dates.days >= 365:
            return f'{int(diff_dates.days / 365)} سال پیش'

        diff_dates_minute = int(diff_dates.seconds / 60)
        if 0 <= diff_dates_minute <= 5:
            return 'لحظاتی پیش'
        elif 5 < diff_dates_minute < 60:
            return f'{diff_dates_minute} دقیقه پیش'
        elif diff_dates_minute >= 60:
            return f'{int(diff_dates_minute / 60)} ساعت پیش'


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
from django_filters import FilterSet, NumberFilter

from estate_module.models import Estate



class EstateFilter(FilterSet):
    min_price = NumberFilter(field_name='price', lookup_expr='gte')
    max_price = NumberFilter(field_name='price', lookup_expr='lte')
    min_meterage = NumberFilter(field_name='meterage', lookup_expr='gte')
    max_meterage = NumberFilter(field_name='meterage', lookup_expr='lte')
    min_deposit = NumberFilter(field_name='deposit', lookup_expr='gte')
    max_deposit = NumberFilter(field_name='deposit', lookup_expr='lte')
    
    class Meta:
        model = Estate
        fields = ['is_special', 'ad_type', 'is_ladder', 'max_price',
                  'min_price', 'estate_properties',
                  'min_deposit', 'max_deposit', 'category',
                  'number_of_rooms', 'min_meterage', 'max_meterage']

from  events_api.models import Seller
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Seller
        fields = ['user']
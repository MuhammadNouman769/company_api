from rest_framework import serializers
from apps.company_api.models import Company
#  create serializers
class CompanySerializer(serializers.HyperlinkedModelSerializer):
     company_id = serializers.ReadOnlyField()
     class Meta:
          model = Company
          fields = '__all__'
 
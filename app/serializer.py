from rest_framework import serializers
from app.models import InfoFam, InfoFamSim

# serializer main model
class InfoFamSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoFam
        fields = ['id','ip','n_fam', 'total_inc', 'percapita',]

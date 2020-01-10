from rest_framework import serializers
from app.models import InfoFam #, InfoFamSim

class InfoFamSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoFam
        fields = ['id','jefefam','ip','n_fam', 'total_inc', 'percapita',]

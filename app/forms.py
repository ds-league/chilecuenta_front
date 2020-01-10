from django import forms
from django.forms import ModelForm
from .models import InfoFam #, InfoFamSim

class InfoFamForm(ModelForm):
    class Meta:
        model =  InfoFam
        exclude = ('ip',)

# phase 2 : minimum wage
# class InfoFamSimForm(ModelForm):
#     class Meta:
#         model =  InfoFamSim
#         exclude = ('ip',)

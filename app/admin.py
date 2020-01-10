from django.contrib import admin
from .models import InfoFam #, InfoFamSim

# Register your models here.
# class SimularAdmin(admin.ModelAdmin):
#     list_display = ('ip', 'id_fam', 'jefe_fam', 'sexo', 'edad', 'ingreso')
#     class Meta:
#         model = Simular

class InfoFamAdmin(admin.ModelAdmin):
    list_display = ('jefefam','ip', 'n_fam', 'total_inc', 'percapita')
    class Meta:
        model = InfoFam

# class InfoFamSimAdmin(admin.ModelAdmin):
#     list_display = ('ip', 'n_fam', 'total_inc', 'percapita', 'min_inc')
#     class Meta:
#         model = InfoFam

# admin.site.register(Simular, SimularAdmin)
admin.site.register(InfoFam, InfoFamAdmin)
# admin.site.register(InfoFamSim, InfoFamSimAdmin)

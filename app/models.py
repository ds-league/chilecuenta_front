from django.db import models

class InfoFam(models.Model):
    # JF_CHOICES = [('f', 'F'), ('m', 'M')]
    jefefam = models.CharField(max_length=1)#, choices=JF_CHOICES, default='F')
    ip = models.GenericIPAddressField(default='192.168.0.1')
    n_fam = models.IntegerField()
    total_inc = models.IntegerField()
    percapita = models.IntegerField()

# phase 2: minimum wage
# class InfoFamSim(models.Model):
#     ip = models.GenericIPAddressField(default='192.168.0.1')
#     n_fam = models.IntegerField()
#     total_inc = models.IntegerField()
#     percapita = models.IntegerField()
#     min_inc = models.IntegerField()

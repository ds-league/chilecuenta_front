from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from .forms import InfoFamForm #, InfoFamSimForm
import json

import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
import requests
from app.models import InfoFam
from .serializers import InfoFamSerializer

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# Create your views here.
def index(request):
    # form to obtain family info:
    # ip address, fam administrator, fam members, total income, percapita
    form_class = InfoFamForm
    if request.method == 'POST':
        form = form_class(request.POST)

        if form.is_valid():
            save_1 = form.save(commit=False)
            # save_1.ip = get_client_ip(request) # attach ip address

            #get data from form
            jefefam = form.cleaned_data['jefefam']
            n_fam = form.cleaned_data['n_fam']
            total_inc = form.cleaned_data['total_inc']
            pc = form.cleaned_data['percapita']

            # post request
            url = "http://127.0.0.1:8000/infofam/"
            data = {
                    "jefefam":jefefam,
                    "ip":get_client_ip(request),
                    "n_fam":n_fam,
                    "total_inc": total_inc,
                    "percapita":pc
                   }

            response = requests.post(url, data=data)

            if response.status_code == 201:
                print(response.json())
            else:
                pass

            # save data to use it in next view
            request.session['n_fam_value'] = n_fam
            request.session['total_inc_value'] = total_inc
            request.session['percapita_value'] = pc

            # save_1.save()

            return  redirect('simulation')
    else: form = form_class()

    # distribution data - get from DB
    labels_line = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    data_line = [30, 40, 50, 60, 70, 90, 200, 500, 600, 800]
    # pie chart data   (check why is not possible to remove this figure in main view)
    labels_pie = ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10", "G11", "G12"]
    data_pie = [30, 10, 10, 32, 2, 1, 3, 2, 5, 1, 1, 3]

    context_data = {
        'form' : form,
        'labels_line': json.dumps(labels_line),
        'data_line': json.dumps(data_line),
        'labels_pie': json.dumps(labels_pie),
        'data_pie': json.dumps(data_pie),
    }
    return render(request, 'index.html', context_data)

def simulation_result(request):
    ## phase 2 : minimum wage - check later
    # form_class = InfoFamSimForm
    # if request.method == 'POST':
    #     form = form_class(request.POST)
    #     if form.is_valid():
    #         save_1 = form.save(commit=False)
    #         save_1.ip = get_client_ip(request)

    #         n_fam = form.cleaned_data['n_fam']
    #         total_inc = form.cleaned_data['total_inc']
    #         pc = form.cleaned_data['percapita']
    #         min_inc = form.cleaned_data['min_inc']

    #         request.session['n_fam_value'] = n_fam
    #         request.session['total_inc_value'] = total_inc
    #         request.session['percapita_value'] = pc
    #         request.session['min_inc_value'] = min_inc

    #         save_1.save()

    #         return  redirect('min_income')
    # else: form = form_class()

    # distribution data - get from DB
    labels_line = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    data_line = [30, 40, 50, 60, 70, 90, 200, 300, 500, 600, 800]
    # pie chart data - get from pre calculated data
    labels_pie = ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10", "G11", "G12"]
    data_pie = [30, 10, 10, 32, 2, 1, 3, 2, 5, 1, 1, 3]

    # location of the family in the distribution - get from DB
    ind = 30

    # get data from previous view
    n_fam0 = request.session.get('n_fam_value')
    total_inc0 = request.session.get('total_inc_value')
    pc0 = request.session.get('percapita_value')

    context_data = {
        # 'form': form,
        'labels_line': json.dumps(labels_line),
        'data_line': json.dumps(data_line),
        # 'data_line2': json.dumps(data_line2),
        'labels_pie': json.dumps(labels_pie),
        'data_pie': json.dumps(data_pie),
        'n_fam': n_fam0,
        'total_inc': total_inc0,
        'pc': pc0,
        'ind': ind,
    }

    return render(request, 'result.html', context_data)

# phase 2 - minimum wage result
# def mininc_result(request):
#     labels_line = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100] #'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10']
#     data_line = [30, 40, 50, 60, 70, 90, 200, 300, 500, 600, 800]
#     data_line2 = [70, 90, 100, 110, 130, 140, 200, 300, 500, 600, 800]
#
#     labels_pie = ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10", "G11", "G12"]
#     data_pie = [30, 10, 10, 32, 2, 1, 3, 2, 5, 1, 1, 3]
#
#     n_fam = request.session.get('n_fam_value')
#     total_inc = request.session.get('total_inc_value')
#     pc = request.session.get('percapita_value')
#     min_inc = request.session.get('min_inc_value')
#
#     context_data = {
#         'labels_line': json.dumps(labels_line),
#         'data_line': json.dumps(data_line),
#         'data_line2': json.dumps(data_line2),
#         'labels_pie': json.dumps(labels_pie),
#         'data_pie': json.dumps(data_pie),
#         'n_fam': n_fam,
#         'total_inc': total_inc,
#         'pc': pc,
#         'min_inc': min_inc,
#     }
#
#     return render(request, 'result_inc.html', context_data)

# serializer model view 
class InfoFamViewSet(viewsets.ModelViewSet):
    queryset = InfoFam.objects.all()
    serializer_class = InfoFamSerializer

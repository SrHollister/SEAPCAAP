from django.shortcuts import render
from App.Models.ConsultasModel import consultas_model
from App.Models.AntpatheredofamModel import Antpatheredofam_model

class ConsultasController():
    def index(request):
        consultas_list = consultas_model.consultas_list()
        context_con = {'consultas_list': consultas_list}
        return render(request, 'views/consultas/consultas.html', context_con)

    def details(request,FolioConsulta):
        objects = consultas_model.getconsulta(FolioConsulta)
        context_con = {'consulta': objects}
        return render(request, 'views/consultas/detailsconsulta.html',context_con)
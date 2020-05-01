from django.db import models
from ..models import antpatheredofam

class Antpatheredofam_model():
    def consultas_list():
        consultasvar = consultagral.objects.order_by("FolioConsulta")
        return consultasvar
    
    def getAntpatheredofam(FolioConsulta):
        consultamost = consultagral.objects.get(FolioConsulta=FolioConsulta)
        return consultamost
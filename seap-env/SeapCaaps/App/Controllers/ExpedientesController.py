from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from App.Models.ExpedientesModel import expedientes_model, RegistrarExpediente
from ..models import expedientes, pacientes

class ExpedientesController():
    def index(request):
        expedientes_list = expedientes_model.expedientes_list()
        context_exped = {'expedientes_list': expedientes_list}
        return render(request, 'views/expedientes/expedientes.html', context_exped)

    def details(request,Id_Exped):
        objects = expedientes_model.getexpediente(Id_Exped)
        context_exped = {'expediente': objects}
        return render(request, 'views/expedientes/detailsexped.html', context_exped)

    def registrarexpediente(request):
        dataCURP = None
        template = 'views/expedientes/registrarexpediente.html'
        if request.method == "POST":
            form = RegistrarExpediente(request.POST)
            if form.is_valid():
                CURP = form.cleaned_data.get('CURP')
                CURPexped = expedientes.objects.filter(CURP = CURP)
                for item in CURPexped:
                    dataCURP = item.CURP
                if dataCURP != None:
                    context_exped = {'form': form, 'error':'El paciente ya cuenta con expediente registrado.'}
                    return render(request, template, context_exped)
                else:
                    CURP = form.cleaned_data.get('CURP')
                    #NewExpediente = expedientes(CURP=CURP)
                    #NewExpediente.save()
                    NewExpediente = expedientes()
                    NewExpediente.CURP = pacientes.objects.get(CURP = request.POST['CURP'])
                    NewExpediente.save()
                    return HttpResponseRedirect('expedientes')
            else:
                context_exped = {'form': form}
                return render(request, template, context_exped)
        else:
            context_exped = {'form': RegistrarExpediente()}
            return render(request, template, context_exped)
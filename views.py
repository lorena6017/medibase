from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime, date, time, timedelta
from django.shortcuts import render, redirect
from tablib import Dataset 
# Creo que  no esta importado el modelo
from .models import InformacionLaboral

from openpyxl import Workbook, load_workbook

def index_medicoDetalle(request):
	return HttpResponse("soy la pagina principal de medico")
#Lista Medicos
class MedicoList(ListView):
	model = InformacionLaboral
	template_name = 'medico/medico_list.html'
	paginate_by = 10

#Crear Medico
def MedicoCreate(request):
	formato1 = "%Y-%m-%d"
	fecha_actual = datetime.now()
	form = MedicoForm()
	form2 = InformacionLaboralForm()
	if request.method == 'POST':
		print('entre al post')
		guardar = Medico(
			tipoDocumento=TipoDocumento.objects.get(pk=request.POST['tipoDocumento']),
			numeroDocumento=request.POST['numeroDocumento'],
			primerNombre=request.POST['primerNombre'],
			segundoNombre=request.POST['segundoNombre'],
			primerApellido=request.POST['primerApellido'],
			segundoApellido=request.POST['segundoApellido'],
			fecha_nacido=request.POST['fecha_nacido'],
			edad=request.POST['edad'],
			genero=Genero.objects.get(pk=request.POST['genero']),
			correo=request.POST['correo'],
		)
		guardar.save()
		save_info = InformacionLaboral(
			Medico=guardar,
			direccion=request.POST['direccion'],
			telefono=request.POST['telefono'],
			celular=request.POST['celular'],
			correoLaboral=request.POST['correoLaboral'],
			Especialidad=Especialidad.objects.get(pk=request.POST['Especialidad']),
			Institucion=Institucion.objects.get(pk=request.POST['Institucion']),
			TipoMonotributo=TipoMonotributo.objects.get(
				pk=request.POST['TipoMonotributo']),
			Municipios=Municipios.objects.get(pk=request.POST['Municipios']),
		)
		save_info.save()
		return HttpResponseRedirect('/lista_medico/')
	else:
		return render(request, 'medicoDetalle/medicoDetalle_form.html', {'form': form,  'form2': form2, 'fecha_actual': fecha_actual.strftime(formato1)})

# Detalle
class MedicoDetalle(DetailView):
	model = InformacionLaboral
	template_name = 'MedicoDetalle/medicoDetalle.html'
	context_object_name = 'detalle'

#Editar
def Medico_Editar(request, pk):
	medico = Medico.objects.get(pk=pk)
	info = InformacionLaboral.objects.get(Medico=medico.id)
	form = MedicoForm(instance=medico)
	form1 = InformacionLaboralForm(instance=info)
	if request.method == "POST":
		form = MedicoForm(request.POST, instance=medico)
		form1 = InformacionLaboralForm(request.POST, instance=medico)
		form.save()
		form1.save()
		return redirect('/lista_medico/')
	return render(request, 'medico/medico_editar.html', {'form': form, 'form1': form1})

def ImportarData(request):
	mostrar = None
	query = MedicoForm()
	valores = []
	for q in query:
		valores.append(q.label)
	query = InformacionLaboralForm()
	for q in query:
		valores.append(q.label)
	
	if request.method == 'POST':
		doc = load_workbook(request.FILES['file_excel'])
		hoja = doc.get_sheet_by_name('Hoja1')
		mostrar = hoja['A1':'H1']
		return render (request, 'MedicoDetalle/importar.html',{'mostrar':mostrar, 'query':valores})
	return render (request, 'MedicoDetalle/importar.html',{'mostrar':mostrar, 'query':valores})


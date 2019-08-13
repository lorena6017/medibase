from django.conf.urls import url
from django.urls import path
from .views import *
from django.template import RequestContext
app_name = 'medidb'

urlpatterns = [

    path("medico_nuevo/", MedicoCreate, name="medico_nuevo"),
    path("lista_medico/", MedicoList.as_view(), name="lista_medico" ),
    path("index/", index_medicoDetalle),
    path("detalle/<int:pk>", MedicoDetalle.as_view(), name="detalle_medico"),
    path('editar_medico/<int:pk>', Medico_Editar, name="editar_medico"),
    path("importar/", ImportarData, name="importar" ),
     

]
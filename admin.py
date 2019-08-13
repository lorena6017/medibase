from django.contrib import admin
from medidb.models import *

# Register your models here.

admin.site.register(TipoDocumento)
admin.site.register(Genero)
admin.site.register(Medico)
admin.site.register(Pais)
admin.site.register(Departamentos)
admin.site.register(Municipios)
admin.site.register(TipoMonotributo)
admin.site.register(TipoEntidad)
admin.site.register(Institucion)
admin.site.register(Especialidad)
admin.site.register(InformacionLaboral)


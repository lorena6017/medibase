from django.db import models
# Create your models here.

class Genero(models.Model):
    nombreGenero = models.CharField(max_length=30)

    def __str__(self):
        return self.nombreGenero


class TipoDocumento(models.Model):
    codigoTipoDocumento = models.CharField(max_length=8)
    nombreTipoDocumento = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.nombreTipoDocumento)


class Medico(models.Model):
    tipoDocumento = models.ForeignKey(
        TipoDocumento, null=False, blank=False, on_delete=models.CASCADE)
    numeroDocumento = models.CharField(max_length=30)
    primerNombre = models.CharField(max_length=50)
    segundoNombre = models.CharField(max_length=50)
    primerApellido = models.CharField(max_length=50)
    segundoApellido = models.CharField(max_length=50)
    fecha_nacido = models.DateField(null=True, blank=True)
    edad = models.IntegerField()
    genero = models.ForeignKey(
        Genero, null=False, blank=False, on_delete=models.CASCADE)
    correo = models.EmailField()

    def NombresCompletos(self):
        cadena = "{0} {1} {2} {3}"
        return cadena.format(self.primerNombre, self.segundoNombre, self.primerApellido, self
                             .segundoApellido)

    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.tipoDocumento, self.numeroDocumento,
                                           self.NombresCompletos(), self.edad, self.genero)


class Pais(models.Model):
    codigoPais = models.CharField(max_length=8)
    nombrePais = models.CharField(max_length=100)

    def __str__(self):
        return '{0}, {1}'.format(self.codigoPais, self.nombrePais)


class Departamentos(models.Model):
    Pais = models.ForeignKey(
        Pais, null=False, blank=False, on_delete=models.CASCADE)
    codigoDepartamento = models.CharField(max_length=8)
    nombreDepartamento = models.CharField(max_length=100)

    def __str__(self):
        return '{0}, {1}, {2}'.format(self.codigoDepartamento, self.nombreDepartamento, self.Pais.nombrePais)


class Municipios(models.Model):
    Departamentos = models.ForeignKey(
        Departamentos, null=False, blank=False, on_delete=models.CASCADE)
    codigoMunicipio = models.CharField(max_length=8)
    nombreMunicipio = models.CharField(max_length=100)

    def __str__(self):
        return '{0}, {1}, {2}'.format(self.codigoMunicipio, self.nombreMunicipio, self.Departamentos.nombreDepartamento)


class TipoMonotributo(models.Model):
    nombreTipoMonotributo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreTipoMonotributo


class TipoEntidad(models.Model):
    nombreTipoEntidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreTipoEntidad


class Institucion(models.Model):
    nombreInstitucion = models.CharField(max_length=150)
    TipoEntidad = models.ForeignKey(
        TipoEntidad, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '{0}, {1}'.format(self.nombreInstitucion, self.TipoEntidad.nombreTipoEntidad)


class Especialidad(models.Model):
    nombreEspecialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreEspecialidad


class InformacionLaboral(models.Model):
    Medico = models.ForeignKey(
        Medico, null=False, blank=False, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    celular = models.CharField(max_length=30)
    correoLaboral = models.EmailField()
    Especialidad = models.ForeignKey(
        Especialidad, null=False, blank=False, on_delete=models.CASCADE)
    Institucion = models.ForeignKey(
        Institucion, null=True, blank=True, on_delete=models.CASCADE)
    TipoMonotributo = models.ForeignKey(
        TipoMonotributo, null=False, on_delete=models.CASCADE)
    Municipios = models.ForeignKey(
        Municipios, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}, {1}, {2}, {3}, {4},{5},{6},{7}".format(self.Medico.NombresCompletos(), self.celular,
                                                            self.direccion,
                                                            self.telefono, self.correoLaboral,
                                                            self.Especialidad.nombreEspecialidad,
                                                            self.TipoMonotributo.nombreTipoMonotributo,
                                                            self.Institucion.nombreInstitucion,
                                                            self.Municipios.nombreMunicipio)

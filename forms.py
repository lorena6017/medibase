from django.forms import Form
from django import forms
from .models import *
from django.db import models


class MedicoForm(forms.Form):

    class Meta:
        model = Medico

    tipoDocumento = forms.ModelChoiceField(widget=forms.Select(
        attrs={'class': 'w3-animate-opacity form-control'}), queryset=TipoDocumento.objects.all(), empty_label='Tipo de Documento')
    numeroDocumento = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Num Documento', 'class': 'w3-animate-opacity form-control'}))
    primerNombre = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Primer Nombre', 'class': 'w3-animate-opacity form-control'}))
    segundoNombre = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Segundo Nombre', 'class': 'w3-animate-opacity form-control'}))
    primerApellido = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Primer Apellido', 'class': 'w3-animate-opacity form-control'}))
    segundoApellido = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Segundo Apellido', 'class': 'w3-animate-opacity form-control'}))
    fecha_nacido = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Fecha Nacimiento', 'class': 'w3-animate-opacity form-control', 'type': 'date'}))
    edad = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Edad', 'class': 'w3-animate-opacity form-control'}))
    genero = forms.ModelChoiceField(widget=forms.Select(
        attrs={'class': 'w3-animate-opacity form-control'}), queryset = Genero.objects.all(), empty_label='Genero')
    correo = forms.CharField(widget=forms.TextInput(attrs={
                             'placeholder': 'Correo Personal', 'class': 'w3-animate-opacity form-control'}))


class InformacionLaboralForm(forms.Form):

    class Meta:
        model: InformacionLaboral

    correoLaboral = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Correo Laboral', 'class': 'w3-animate-opacity form-control'}))
    Municipios = forms.ModelChoiceField(queryset=Municipios.objects.all(), widget=forms.Select(
        attrs={'placeholder': 'Ciudad', 'class': 'w3-animate-opacity form-control'}), empty_label='Ciudad')
    Especialidad = forms.ModelChoiceField(queryset=Especialidad.objects.all(), widget=forms.Select(
        attrs={'placeholder': 'Especialidad', 'class': 'w3-animate-opacity form-control'}), empty_label='Especialidad')
    Institucion = forms.ModelChoiceField(queryset=Institucion.objects.all(), widget=forms.Select(
        attrs={'placeholder': 'Institucion', 'class': 'w3-animate-opacity form-control'}), empty_label='Intitucion')
    TipoMonotributo = forms.ModelChoiceField(queryset=TipoMonotributo.objects.all(), widget=forms.Select(
        attrs={'placeholder': 'Tipo Monotributo', 'class': 'w3-animate-opacity form-control'}), empty_label='Tipo')
    celular = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Numero Celular', 'class': 'w3-animate-opacity form-control'}))
    telefono = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Telefono Fijo', 'class': 'w3-animate-opacity form-control'}))
    direccion = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Direccion Actual', 'class': 'w3-animate-opacity form-control'}))

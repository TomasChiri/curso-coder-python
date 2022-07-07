from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()

class CursoBusquedaFormulario(forms.Form):
    criterio = forms.CharField()
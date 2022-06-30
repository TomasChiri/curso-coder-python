from django.contrib import admin
from django.urls import path
from mi_app.views import listar_cursos, listar_estudiantes, mostrar_index, saludar_a, saludo, saludo_personalizado

urlpatterns = [
    # path('saludar/', saludo),
    path('mi-pagina/', mostrar_index),
    path('saludar/persona/<nombre>', saludar_a),
    path('saludo-personalizado', saludo_personalizado),
    path('listar-cursos/', listar_cursos),
    path('listar-estudiantes', listar_estudiantes),
]

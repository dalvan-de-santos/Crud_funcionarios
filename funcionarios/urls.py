from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrar_func, name='cadastrar_func'),
    path('deletar/<int:id>', views.deletar_func, name='deletar_func'),
    path('atualizar/<int:id>', views.atualizar_func, name='atualizar_func')
]
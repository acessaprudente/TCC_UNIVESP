from django.contrib import admin
from django.urls import path
from .views import home, lista_funcoes, funcao_novo, funcao_update, funcao_search, funcao_delete
from .views import lista_setores, setor_novo, setor_update, setor_search, setor_delete

urlpatterns = [
    path('home', home, name='home'),
    path('lista_funcoes', lista_funcoes, name='lista_funcoes'),
    path('funcao_novo', funcao_novo, name='funcao_novo'),
    path('funcao_update/<int:id>', funcao_update, name='funcao_update'),
    path('funcao_delete/<int:id>', funcao_delete, name='funcao_delete'),
    path('funcao_search', funcao_search, name='funcao_search'),
    
    path('lista_setores', lista_setores, name='lista_setores'),
    path('setor_novo', setor_novo, name='setor_novo'),
    path('setor_update/<int:id>', setor_update, name='setor_update'),
    path('setor_delete/<int:id>', setor_delete, name='setor_delete'),
    path('setor_search', setor_search, name='setor_search'),
]   




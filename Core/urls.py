from django.contrib import admin
from django.urls import path
from .views import home, lista_funcoes, funcao_novo, funcao_update, funcao_search, funcao_delete
from .views import lista_setores, setor_novo, setor_update, setor_search, setor_delete
from .views import lista_tiporiscos, tiporisco_novo, tiporisco_update, tiporisco_delete
from .views import lista_riscos, risco_novo, risco_update, risco_delete
from .views import lista_exames, exame_novo, exame_update, exame_delete
from .views import lista_grupos, grupo_novo, grupo_update, grupo_delete

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
    
    path('lista_tiporiscos', lista_tiporiscos, name='lista_tiporiscos'),
    path('tiporisco_novo', tiporisco_novo, name='tiporisco_novo'),
    path('tiporisco_update/<int:id>', tiporisco_update, name='tiporisco_update'),
    path('tiporisco_delete/<int:id>', tiporisco_delete, name='tiporisco_delete'), 

    path('lista_riscos', lista_riscos, name='lista_riscos'),
    path('risco_novo', risco_novo, name='risco_novo'),
    path('risco_update/<int:id>', risco_update, name='risco_update'),
    path('risco_delete/<int:id>', risco_delete, name='risco_delete'),
    
    path('lista_exames', lista_exames, name='lista_exames'),
    path('exame_novo', exame_novo, name='exame_novo'),
    path('exame_update/<int:id>', exame_update, name='exame_update'),
    path('exame_delete/<int:id>', exame_delete, name='exame_delete'), 
    
    path('lista_grupos', lista_grupos, name='lista_grupos'),
    path('grupo_novo', grupo_novo, name='grupo_novo'),
    path('grupo_update/<int:id>', grupo_update, name='grupo_update'),
    path('grupo_delete/<int:id>', grupo_delete, name='grupo_delete'),        
]   





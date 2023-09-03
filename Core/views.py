from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.core.paginator import Paginator
from .models import Funcao
from .forms import FuncaoForm


# Create your views here.
def home(request):
    return render(request, 'core/home.html')
"""
def lista_funcoes(request):
    form = FuncaoForm
    funcoes = Funcao.objects.all().order_by('nome')
    return render(request, 'core/lista_funcoes.html', {'form':form,'funcoes': funcoes})
"""

def lista_funcoes(request):
    form = FuncaoForm
    funcoes_list = Funcao.objects.all().order_by('nome')
    paginator = Paginator(funcoes_list, 2)
    page = request.GET.get('page')
    funcoes = paginator.get_page(page)
    data = {}
    data['funcoes'] = funcoes
    data['form'] = form
    #return render(request, 'core/lista_funcoes.html', {'form':form,'funcoes': funcoes})
    return render(request, 'core/lista_funcoes.html', data)











def funcao_novo(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        count = Funcao.objects.filter(nome = nome). count()
        if count > 0:
            messages.error(request,'Registro já cadastrado com esse nome!')
        else:
            return redirect('lista_funcoes')
        nome = request.POST.get('nome')
        count = Funcao.objects.filter(nome=nome).count()
        if count > 0:
            messages.error(request, 'Registro já cadastrado com este Nome !')
            return redirect('funcao_novo')
        else:
            form = FuncaoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_funcoes')
    else:
        form = FuncaoForm
        return render(request, 'core/funcao_novo.html', {'form': form})


        
def funcao_update(request, id):
    funcao = Funcao.objects.get(id=id)
    form = FuncaoForm(request.POST or None, instance=funcao)
    data = {}
    data['funcao'] = funcao
    data['form'] = form
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('lista_funcoes')
    else:
        form = FuncaoForm
        return render(request, 'core/funcao_update.html', data)
    



        
def funcao_search(request):
    search = request.GET.get('search')
    funcoes = Funcao.objects.filter(nome__icontains=search)
    form = FuncaoForm()
    data = {}
    data['funcoes'] = funcoes
    data['form'] = form
    return render(request, 'core/lista_funcoes.html', data)       

def funcao_delete(request, id):
    funcao = Funcao.objects.get(id=id)
    funcao.delete()
    messages.success(request, 'Registro Excluido com sucesso !')
    return redirect('lista_funcoes')
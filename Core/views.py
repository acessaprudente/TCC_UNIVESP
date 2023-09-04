from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.core.paginator import Paginator
from .models import Funcao, Setor
from .forms import FuncaoForm, SetorForm


# Create your views here.
def home(request):
    return render(request, 'core/home.html')

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
    
    
def lista_setores(request):
    form = SetorForm
    setores_list = Setor.objects.all().order_by('nome')
    paginator = Paginator(setores_list, 2)
    page = request.GET.get('page')
    setores = paginator.get_page(page)
    data = {}
    data['setores'] = setores
    data['form'] = form
    return render(request, 'core/lista_setores.html', data)
def setor_novo(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        count = Setor.objects.filter(nome=nome).count()
        if count > 0:
            messages.error(request, 'Registro já cadastrado com este Nome !')
            return redirect('setor_novo')
        else:
            form = SetorForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_setores')
    else:
        form = SetorForm
        return render(request, 'core/setor_novo.html', {'form': form})

def setor_update(request, id):
    setor = Setor.objects.get(id=id)
    form = SetorForm(request.POST or None, instance=setor)
    data = {}
    data['setor'] = setor
    data['form'] = form
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('lista_setores')
    else:
        form = SetorForm
        return render(request, 'core/setor_update.html', data)

def setor_search(request):
    search = request.GET.get('search')
    setores = Setor.objects.filter(nome__icontains=search)
    form = SetorForm()
    data = {}
    data['setores'] = setores
    data['form'] = form
    return render(request, 'core/lista_setores.html', data)

def setor_delete(request, id):
    setor = Setor.objects.get(id=id)
    setor.delete()
    messages.success(request, 'Registro Excluido com sucesso !')
    return redirect('lista_setores')

  

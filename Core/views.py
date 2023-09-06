from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.core.paginator import Paginator
from .models import Funcao, Setor, TipoRisco, Risco, Exame, Grupo
from .forms import FuncaoForm, SetorForm, TipoRiscoForm, RiscoForm, ExameForm, GrupoForm

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
    return render(request, 'core/lista_funcoes.html', data)

def funcao_novo(request):
    if request.method == "POST":
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

def lista_tiporiscos(request):
    form = TipoRiscoForm
    tiporiscos = TipoRisco.objects.all().order_by('nome')
    data = {}
    data['tiporiscos'] = tiporiscos
    data['form'] = form
    return render(request, 'core/lista_tiporiscos.html', data)

def tiporisco_novo(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        count = TipoRisco.objects.filter(nome=nome).count()
        if count > 0:
            messages.error(request, 'Registro já cadastrado com este Nome !')
            return redirect('tiporisco_novo')
        else:
            form = TipoRiscoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_tiporiscos')
    else:
        form = TipoRiscoForm
        return render(request, 'core/tiporisco_novo.html', {'form': form})

def tiporisco_update(request, id):
    tiporisco = TipoRisco.objects.get(id=id)

    nome = request.POST.get('nome')
    count = TipoRisco.objects.filter(nome=nome).exclude(id=id).count()
    if count > 0:
        messages.error(request, 'Registro já cadastrado com este Nome !')
        return redirect('lista_tiporiscos')

    form = TipoRiscoForm(request.POST or None, instance=tiporisco)
    data = {}
    data['tiporisco'] = tiporisco
    data['form'] = form
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('lista_tiporiscos')
    else:
        form = TipoRiscoForm
        return render(request, 'core/tiporisco_update.html', data)

def tiporisco_delete(request, id):
    tiporisco = TipoRisco.objects.get(id=id)
    tiporisco.delete()
    messages.success(request, 'Registro Excluido com sucesso !')
    return redirect('lista_tiporiscos')

def lista_riscos(request):
    form = RiscoForm
    riscos = Risco.objects.all().order_by('nome')
    data = {}
    data['riscos'] = riscos
    data['form'] = form
    return render(request, 'core/lista_riscos.html', data)

def risco_novo(request):
    if request.method == "POST":
        nome = request.POST.get('id_nome')
        tiporisco_id = request.POST.get('id_tiporisco')
        count = Risco.objects.filter(nome=nome).count()
        if count > 0:
            messages.error(request, 'Registro já cadastrado com este Nome !')
            return redirect('risco_novo')
        else:
            form = RiscoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_riscos')
    else:
        form = RiscoForm
        tiporiscos = TipoRisco.objects.all().order_by('nome')
        data = {}
        data['tiporiscos'] = tiporiscos
        data['form'] = form
        return render(request, 'core/risco_novo.html', data)

def risco_update(request, id):
    risco = Risco.objects.get(id=id)
    nome = request.POST.get('nome')
    count = Risco.objects.filter(nome=nome).exclude(id=id).count()
    if count > 0:
        messages.error(request, 'Registro já cadastrado com este Nome !')
        return redirect('lista_riscos')

    form = RiscoForm(request.POST or None, instance=risco)
    tiporiscos = TipoRisco.objects.all().order_by('nome')
    data = {}
    data['tiporiscos'] = tiporiscos
    data['risco'] = risco
    data['form'] = form

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('lista_riscos')
    else:
        form = RiscoForm
        return render(request, 'core/risco_update.html', data)

def risco_delete(request, id):
    risco = Risco.objects.get(id=id)
    risco.delete()
    messages.success(request, 'Registro Excluido com sucesso !')
    return redirect('lista_riscos')

def lista_exames(request):
    form = ExameForm
    exames = Exame.objects.all().order_by('nome')
    data = {}
    data['exames'] = exames
    data['form'] = form
    return render(request, 'core/lista_exames.html', data)

def exame_novo(request):
    if request.method == "POST":
        nome = request.POST.get('id_nome')
        validade = request.POST.get('validade')
        count = Exame.objects.filter(nome=nome).count()
        if count > 0:
            messages.error(request, 'Registro já cadastrado com este Nome !')
            return redirect('exame_novo')
        else:
            form = ExameForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_exames')
    else:
        form = ExameForm
        data = {}
        data['form'] = form
        return render(request, 'core/exame_novo.html', data)

def exame_update(request, id):
    exame = Exame.objects.get(id=id)
    form = ExameForm(request.POST or None, instance=exame)
    data = {}
    data['exame'] = exame
    data['form'] = form

    if request.method == "POST":
        nome = request.POST.get('nome')
        count = Exame.objects.filter(nome=nome).exclude(id=id).count()
        if count > 0:
            messages.error(request, 'Registro já cadastrado com este Nome !')
            return redirect('lista_exames')        
        if form.is_valid():
            form.save()
            return redirect('lista_exames')
    else:
        form = ExameForm
        return render(request, 'core/exame_update.html', data)

def exame_delete(request, id):
    exame = Exame.objects.get(id=id)
    exame.delete()
    messages.success(request, 'Registro Excluido com sucesso !')
    return redirect('lista_exames')

def lista_grupos(request):
    form = GrupoForm
    grupos = Grupo.objects.all().order_by('nome')
    data = {}
    data['grupos'] = grupos
    data['form'] = form
    return render(request, 'core/lista_grupos.html', data)

def grupo_novo(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        count = Grupo.objects.filter(nome=nome).count()
        if count > 0:
            messages.error(request, 'Registro já cadastrado com este Nome !')
            return redirect('grupo_novo')
        else:
            form = GrupoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_grupos')
    else:
        form = GrupoForm
        return render(request, 'core/grupo_novo.html', {'form': form})

def grupo_update(request, id):
    grupo = Grupo.objects.get(id=id)
    form = GrupoForm(request.POST or None, instance=grupo)
    data = {}
    data['grupo'] = grupo
    data['form'] = form
    if request.method == "POST":
        nome = request.POST.get('nome')
        count = Grupo.objects.filter(nome=nome).exclude(id=id).count()
        if count > 0:
            messages.error(request, 'Registro já cadastrado com este Nome !')
            return redirect('lista_grupos')
        
        if form.is_valid():
            form.save()
            return redirect('lista_grupos')
    else:
        form = GrupoForm
        return render(request, 'core/grupo_update.html', data)

def grupo_delete(request, id):
    grupo = Grupo.objects.get(id=id)
    grupo.delete()
    messages.success(request, 'Registro Excluido com sucesso !')
    return redirect('lista_grupos')

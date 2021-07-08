from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .forms import ContatoForm, ProdutoModelForm
from .models import Produto


def index(request):
    return render(request, 'index.html')

def consulta1(request, pk):
    x = Produto.objects.all()
    context = {
        'produtos': x[(pk*3):((1+pk)*3)],
        'qnt_produtos': range(0,int((len(Produto.objects.all())) /3))
        }
    return render(request, 'consulta.html', context)



def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():

                form.save()

                messages.success(request, 'Produto salvo com sucesso.')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao salvar produto.')
        else:
            form = ProdutoModelForm()
        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')

def pegar_produto(query=None):
    queryset = []
    queries = query.spliy
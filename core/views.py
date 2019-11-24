from django.shortcuts import render, get_object_or_404
from core.models import Produto
# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    produto = Produto.objects.all()

    context = {
        'produtos': produto
    }


    return render(request, 'index.html', context)

def produto(request,pk):
    # print(f'pk:{pk}')
    # p = Produto.objects.get(pk=pk)

    p = get_object_or_404(Produto, id=pk)

    context = {
        'p':p
    }
    return render(request, 'produto.html', context)


def contato(request):
    return render(request, 'contato.html')



def error404(request,ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)


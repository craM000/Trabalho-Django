from django.shortcuts import render, redirect
from . models import Pessoa

# Create your views here.

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {'pessoas':pessoas})

def salvar(request):
    vnome = request.POST.get('nome')
    vsobrenome = request.POST.get('sobrenome')
    vendereco = request.POST.get('endereco')
    vcpf = request.POST.get('cpf')
    Pessoa.objects.create(nome=vnome, sobrenome=vsobrenome, endereco=vendereco, cpf=vcpf)
    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {'pessoas':pessoas})

def editar(request,id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, 'update.html', {'pessoa': pessoa})

def update(request, id):
    if request.method == 'POST':
        vnome = request.POST.get('nome')
        vsobrenome = request.POST.get('sobrenome')
        vendereco = request.POST.get('endereco')
        vcpf = request.POST.get('cpf')
        print(vnome, vsobrenome, vendereco, vcpf)  # Verifique se os dados estão corretos
        pessoa = Pessoa.objects.get(id=id)
        pessoa.nome = vnome
        pessoa.sobrenome = vsobrenome
        pessoa.endereco = vendereco
        pessoa.cpf = vcpf
        pessoa.save()
        return redirect(home)
    else:
        pessoa = Pessoa.objects.get(id=id)
        return render(request, 'update.html', {'pessoa': pessoa})


def delete(request,id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)


from django.shortcuts import render, redirect, get_object_or_404
from funcionarios.models import Funcionario

def cadastrar_func(request):

    if request.method == "GET":

        funcionarios = Funcionario.objects.all()

        return render(request, 'cadastrar_func.html', {'funcionarios': funcionarios})
    
    elif request.method == "POST":
        nome = request.POST.get('nome')
        funcao = request.POST.get('funcao')
        sexo = request.POST.get('sexo')
        email = request.POST.get('email')

        funcionario = Funcionario(nome=nome, funcao=funcao, sexo=sexo, email=email)
        funcionario.save()

    return redirect('cadastrar_func')



def deletar_func(request, id):
    
    funcionario = get_object_or_404(Funcionario, id=id)
    funcionario.delete()

    return redirect('cadastrar_func')

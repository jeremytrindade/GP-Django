from django.http import HttpResponse


def hello(request):
    return HttpResponse('Olá Mundo')

def articles(request, year):
    return HttpResponse('O ano enviado foi: '+ str(year))

def lerDoBanco(nome):
    lista_nomes = [
        {'nome': 'Ana', 'idade': 20},
        {'nome': 'João', 'idade': 25},
        {'nome': 'Joaquim', 'idade': 27}
    ]

    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
        else:
            return {'nome': 'Não encontrado', 'idade': 0}

def fname(request, nome):
    result = lerDoBanco(nome)
    print(result)
    return HttpResponse('A pessoa foi encontrada, ela tem ' + str(result['idade']) + ' anos')

from django.http import HttpResponse


def hello(request):
    return HttpResponse('Olá Mundo')

def articles(request, year):
    return HttpResponse('O ano enviado foi: '+ str(year))

def lerDoBanco(name):
    lista_names = [
        {'name': 'Ana', 'age': 20},
        {'name': 'João', 'age': 25},
        {'name': 'Joaquim', 'age': 27}
    ]

    for person in lista_names:
        if person['name'] == name:
            return person
    return {'name': 'Person not found', 'age': 0}

def fname(request, name):
    result = lerDoBanco(name)
    if result['age'] > 0:
        return HttpResponse('The person was found, has ' + str(result['age']) + ' years old')
    else:
        return HttpResponse('Person not found')


#def lerDoBanco(nome):
#    lista_nomes = [
#        {'nome': 'Joaquim', 'idade': 20},
#        {'nome': 'João', 'idade': 25},
#        {'nome': 'Ana', 'idade': 27}
#    ]
#
#    for pessoa in lista_nomes:
#        if pessoa['nome'] == nome:
#            return pessoa
#        else:
#            return {'nome': 'Não encontrado', 'idade': 0}
#
#def fname(request, nome):
#    result = lerDoBanco(nome)
#    if result['idade'] > 0:
#        return HttpResponse(result['nome'] + '<br>'+'A pessoa foi encontrada, ela tem ' + str(result['idade']) + ' anos')
#    else:
#        return HttpResponse('Pessoa não encontrada')

# import bottle as b
from bottle import *

pessoas = [
    {
        "url": "pietro",
        "nome": "Pietro Ribeiro",
        "telefone": "(11) 012340-1933"
    },
    {
        "url": "joao_pedro",
        "nome": "João Bacchi",
        "telefone": "(11) 041340-1933"
    },
    {
        "url": "tomas",
        "nome": "Tomas Miele",
        "telefone": "(11) 017340-1933"
    }
]

@route('/')
def index():
    return "<h1>Funcionou!</h1>"

@route('/hello/<name>')
def hello_to(name):
    return f"<h1>Hello, {name}</h1>"
    # return "<h1>Hello, {}</h1>".format(name)

@route('/pessoas/<url_pessoa>')
def get_pessoa(url_pessoa):
    ind = -1

    for i in range(len(pessoas)):
        if pessoas[i]['url'] == url_pessoa:
            ind = i
    
    pessoa = pessoas[ind]

    return f"""<h1>{pessoa['nome']}</h1>
Telefone: {pessoa['telefone']}
    """

run()
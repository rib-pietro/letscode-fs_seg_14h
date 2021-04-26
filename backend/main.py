# import bottle as b
from bottle import *

pessoas = [
    {
        "id": 1,
        "url": "pietro",
        "nome": "Pietro Ribeiro",
        "telefone": "(11) 012340-1933",
        "visualizacoes": 0, 
    },
    {
        "id": 2,
        "url": "joao-pedro",
        "nome": "João Bacchi",
        "telefone": "(11) 041340-1933",
        "visualizacoes": 0,
    },
    {
        "id": 3,
        "url": "tomas",
        "nome": "Tomas Miele",
        "telefone": "(11) 017340-1933",
        "visualizacoes": 0,
    }
]

@route('/')
def index():
    return "<h1>Funcionou!</h1>"

@route('/hello/<name>')
def hello_to(name):
    return f"<h1>Hello, {name}</h1>" # "<h1>Hello, " + name + "</h1>" 
    # return "<h1>Hello, {}</h1>".format(name)

@route('/pessoas/cadastrar')
def formulario_cadastro():
    return """
    <form action="/pessoas/cadastrar" method="POST">
        <div>
            <label for="nome">Nome: </label>
            <input type="text" name="nome" id="nome"/>
        </div>
        <div>
            <label for="email">E-mail: </label>
            <input type="email" name="email" id="email"/>
        </div>
        <div>
            <label for="telefone">Telefone: </label>
            <input type="text" name="telefone" id="telefone"/>
        </div>
        <button type="submit">Cadastrar</button>
    </form>
    """

@route('/pessoas/cadastrar', method='POST')
def cadastrar_pessoa():
    infos = request.forms
    nova_pessoa = {}
    nova_pessoa['nome'] = infos['nome']
    nova_pessoa['telefone'] = infos['telefone']
    nova_pessoa['email'] = infos['email']
    nova_pessoa['url'] = nova_pessoa['nome'].lower().replace(' ', '-')
    nova_pessoa['id'] = len(pessoas) + 1
    nova_pessoa['visualizacoes'] = 0

    pessoas.append(nova_pessoa)

    return "Nova pessoa cadastrada!"

@route('/pessoas/<url_pessoa:int>')
def get_pessoa(url_pessoa):
    ind = -1

    for i in range(len(pessoas)):
        if pessoas[i]['id'] == url_pessoa:
            ind = i
    
    pessoa = pessoas[ind]

    # # SE NAO_ENCONTRADO
    # #    EXIBIR "NÃO ENCONTRADO" 
    if ind == -1:
        return "Não encontrado!"
    
    return f"""<h1>{pessoa['nome']}</h1>
Telefone: {pessoa['telefone']}
    """

@route('/pessoas/<url_pessoa>')
def get_pessoa(url_pessoa):
    ind = -1

    for i in range(len(pessoas)):
        if pessoas[i]['url'] == url_pessoa:
            ind = i
            pessoas[i]['visualizacoes'] += 1
    
    pessoa = pessoas[ind]

    # # SE NAO_ENCONTRADO
    # #    EXIBIR "NÃO ENCONTRADO" 
    if ind == -1:
        return "Não encontrado!"
    
    return f"""<h1>{pessoa['nome']}</h1>
<p>Telefone: {pessoa['telefone']}</p>
<p>Visitas no perfil: {pessoa['visualizacoes']}
    """


run()
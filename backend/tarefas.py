from bottle import *

# TEMPLATE_PATH = ['./visualizacoes'] # Alterar pasta padrão de templates

tarefas = []

@route('/')

@route('/tarefas/cadastrar')
def formulario_tarefa():
    # infos_template = { "tarefas": tarefas }
    # return template('formulario', infos_template)

    return template('formulario', tarefas=tarefas)
    # return f"""
    # <form method='POST' action='/tarefas/cadastrar'>
    #     <div>
    #         <label for="tarefa">Nova tarefa</label>
    #         <input id="tarefa" type="text" name="tarefa" />
    #     </div>
    #     <button type="submit">Adicionar</button>
    # </form>
    # {', '.join(tarefas)}
    # """

@route('/tarefas/cadastrar', method='POST')
def cadastrar_tarefa():
    infos = request.forms
    nova_tarefa = infos['tarefa']
    tarefas.append(nova_tarefa)

    redirect('/tarefas/cadastrar')
    # return 'Tarefa cadastrada!'

run()
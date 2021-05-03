from bottle import *

tarefas = []

@route('/tarefas/cadastrar')
def formulario_tarefa():
    return f"""
    <form method='POST' action='/tarefas/cadastrar'>
        <div>
            <label for="tarefa">Nova tarefa</label>
            <input id="tarefa" type="text" name="tarefa" />
        </div>
        <button type="submit">Adicionar</button>
    </form>
    {', '.join(tarefas)}
    """

@route('/tarefas/cadastrar', method='POST')
def cadastrar_tarefa():
    infos = request.forms
    nova_tarefa = infos['tarefa']
    tarefas.append(nova_tarefa)

    redirect('/tarefas/cadastrar')
    # return 'Tarefa cadastrada!'

run()
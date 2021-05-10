<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form method='POST' action='/tarefas/cadastrar'>
        <div>
            <label for="tarefa">Nova tarefa</label>
            <input id="tarefa" type="text" name="tarefa" />
        </div>
        <button type="submit">Adicionar</button>
    </form>
    <ul>
        <% for tarefa in tarefas: %>
            <li>{{ tarefa }}</li>
        <% end %>
    </ul>
    
</body>
</html>
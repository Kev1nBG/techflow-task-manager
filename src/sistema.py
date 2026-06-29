# Banco de dados simulado em memória (Lista de dicionários)
banco_de_tarefas = []

def adicionar_tarefa(id_tarefa, titulo, descricao):
    """Adiciona uma nova tarefa ao sistema (Create)"""
    if not titulo.strip():
        raise ValueError("O título da tarefa não pode ser vazio.")
        
    tarefa = {
        "id": id_tarefa,
        "titulo": titulo,
        "descricao": descricao,
        "concluida": False
    }
    banco_de_tarefas.append(tarefa)
    return tarefa

def listar_tarefas():
    """Retorna todas as tarefas cadastradas (Read)"""
    return banco_de_tarefas

def atualizar_status_tarefa(id_tarefa, concluida):
    """Atualiza o status de conclusão da tarefa (Update)"""
    for tarefa in banco_de_tarefas:
        if tarefa["id"] == id_tarefa:
            tarefa["concluida"] = concluida
            return tarefa
    return None

def deletar_tarefa(id_tarefa):
    """Remove uma tarefa do sistema usando o ID (Delete)"""
    global banco_de_tarefas
    tamanho_inicial = len(banco_de_tarefas)
    banco_de_tarefas = [t for t in banco_de_tarefas if t["id"] != id_tarefa]
    return len(banco_de_tarefas) < tamanho_inicial

    
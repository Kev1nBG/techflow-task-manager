import pytest
from src.sistema import (
    adicionar_tarefa, 
    listar_tarefas, 
    atualizar_status_tarefa, 
    deletar_tarefa,
    banco_de_tarefas
)

@pytest.fixture(autouse=True)
def limpar_banco():
    """Limpa o banco de dados antes de cada teste"""
    banco_de_tarefas.clear()

def test_adicionar_tarefa_sucesso():
    """Testa a criação de uma tarefa com sucesso (Create)"""
    tarefa = adicionar_tarefa(1, "Entregar Carga SP", "Entrega urgente na zona sul")
    assert tarefa["id"] == 1
    assert tarefa["titulo"] == "Entregar Carga SP"
    assert len(listar_tarefas()) == 1

def test_adicionar_tarefa_sem_titulo_deve_falhar():
    """Testa se o sistema impede tarefas sem título"""
    with pytest.raises(ValueError):
        adicionar_tarefa(2, "   ", "Descrição qualquer")

def test_listar_tarefas():
    """Testa a leitura das tarefas cadastradas (Read)"""
    adicionar_tarefa(1, "Rota A", "Carregar caminhão")
    adicionar_tarefa(2, "Rota B", "Descarregar caminhão")
    tarefas = listar_tarefas()
    assert len(tarefas) == 2

def test_atualizar_status_tarefa():
    """Testa a atualização do status da tarefa (Update)"""
    adicionar_tarefa(1, "Manutenção da Frota", "Troca de óleo")
    tarefa_atualizada = atualizar_status_tarefa(1, concluida=True)
    assert tarefa_atualizada["concluida"] is True

def test_deletar_tarefa():
    """Testa a remoção de uma tarefa (Delete)"""
    adicionar_tarefa(1, "Abastecer", "Diesel")
    sucesso = deletar_tarefa(1)
    assert sucesso is True
    assert len(listar_tarefas()) == 0
    
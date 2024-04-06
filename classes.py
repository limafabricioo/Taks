#Projeto para gerenciar tarefas diárias

class Task:
    def __init__ (self, nome, descricao, data, prazo):
        self.nome = nome
        self.descricao = descricao
        self.data = data
        self.status = ["Pendente", "Em Andamento", "Concluida"]

    def mudar_status (self, status_atual):
        if status_atual in self.status["Pendente"]:
            print("Você ainda não começou essa tarefa.")
        elif status_atual in self.status["Em Andamento"]:
            print("Você precisa terminar está tarefa para ir para a próxima.")
        else:
            print("Tarefa Concluída")

    #def adicionar_tarefa (self, tarefa):

from datetime import date

data_hoje = date.today()

nome_tarefa = input("Digite o nome da tarefa: ")
nome_descricao = input("Digite a descrição desta tarefa: ")
print(data_hoje)
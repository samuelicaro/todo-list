import json
import os

def limpar_tela():
    os.system('clear')

def verifica_arquivo():
    if os.path.exists("tarefas.json") and os.path.getsize("tarefas.json") > 0:
        with open("tarefas.json", "r") as arquivo:
            return json.load(arquivo)
    else:
        with open("tarefas.json", "w") as arquivo:
            json.dump([], arquivo)
            
def salva_tarefa(tarefas):
    with open("tarefas.json", "w") as arquivo:
            json.dump(tarefas, arquivo)

menu = {
    1: "Ver tarefas",
    2: "Adicionar tarefa",
    3: "Remover tarefa",
    4: "Editar tarefa",
    0: "Sair"
}

lista_de_tarefas = verifica_arquivo()

while True:
    print("SEJA BEM VINDO AO TODO LIST DO SAMUEL")
    for chave, valor in menu.items():
        print(chave, valor)

    escolha = int(input("Qual opção deseja escolher? "))

    if escolha == 1:
        limpar_tela()
        with open("tarefas.json") as arquivo:
            data_ler = json.load(arquivo)
        
        if not lista_de_tarefas:
            print("Nenhuma tarefa cadastrada ainda.")
        else:
            for tarefa in lista_de_tarefas:
                print(tarefa.get('titulo'))

    elif escolha == 2:
        limpar_tela()
        tarefa = input("Qual será a tarefa? ")

        adicionar_tarefa_json = {
            "titulo": tarefa
        }

        lista_de_tarefas.append(adicionar_tarefa_json)
        salva_tarefa(lista_de_tarefas)
        
        print("Tarefa adicionada com sucesso!")

    elif escolha == 0:
        limpar_tela()
        print("Até outra hora...")
        break
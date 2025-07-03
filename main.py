from task_manager import (
    adicionar_tarefa,
    listar_tarefas,
    marcar_tarefa_concluida,
    exibir_tarefas_por_prioridade,
    exibir_tarefas_por_categoria,
    remover_tarefa
)

def exibir_menu():
    print("\n--- Gerenciador de Tarefas ---")
    print("1. Adicionar Tarefa")
    print("2. Listar Todas as Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Exibir Tarefas por Prioridade")
    print("5. Exibir Tarefas por Categoria")
    print("6. Remover Tarefa")
    print("0. Sair")
    print("------------------------------")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome da tarefa: ")
            descricao = input("Descrição: ")
            prioridade = input("Prioridade (Baixa, Média, Alta): ")
            categoria = input("Categoria (Ex: Pessoal, Trabalho, Estudo): ")
            adicionar_tarefa(nome, descricao, prioridade, categoria)
        elif opcao == '2':
            listar_tarefas()
        elif opcao == '3':
            try:
                tarefa_id = int(input("Digite o ID da tarefa a ser marcada como concluída: "))
                marcar_tarefa_concluida(tarefa_id)
            except ValueError:
                print("ID inválido. Por favor, digite um número.")
        elif opcao == '4':
            prioridade = input("Digite a prioridade para filtrar (Baixa, Média, Alta): ")
            exibir_tarefas_por_prioridade(prioridade)
        elif opcao == '5':
            categoria = input("Digite a categoria para filtrar: ")
            exibir_tarefas_por_categoria(categoria)
        elif opcao == '6':
            try:
                tarefa_id = int(input("Digite o ID da tarefa a ser removida: "))
                remover_tarefa(tarefa_id)
            except ValueError:
                print("ID inválido. Por favor, digite um número.")
        elif opcao == '0':
            print("Saindo do Gerenciador de Tarefas. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()

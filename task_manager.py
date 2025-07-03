tarefas = []
proximo_id = 1

def adicionar_tarefa(nome, descricao, prioridade, categoria):
    global proximo_id
    tarefa = {
        "id": proximo_id,
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": False
    }
    tarefas.append(tarefa)
    proximo_id += 1
    print(f"Tarefa '{nome}' adicionada com sucesso! ID: {tarefa['id']}")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\n--- Lista de Tarefas ---")
    for tarefa in tarefas:
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"ID: {tarefa['id']} | Nome: {tarefa['nome']} | Prioridade: {tarefa['prioridade']} | Categoria: {tarefa['categoria']} | Status: {status}")
        print(f"  Descrição: {tarefa['descricao']}")
    print("------------------------")

def marcar_tarefa_concluida(tarefa_id):
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            tarefa["concluida"] = True
            print(f"Tarefa '{tarefa['nome']}' (ID: {tarefa_id}) marcada como concluída.")
            return
    print(f"Erro: Tarefa com ID {tarefa_id} não encontrada.")

def exibir_tarefas_por_prioridade(prioridade):
    encontradas = [t for t in tarefas if t["prioridade"].lower() == prioridade.lower()]
    if not encontradas:
        print(f"Nenhuma tarefa encontrada com prioridade '{prioridade}'.")
        return

    print(f"\n--- Tarefas com Prioridade: {prioridade.capitalize()} ---")
    for tarefa in encontradas:
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"ID: {tarefa['id']} | Nome: {tarefa['nome']} | Categoria: {tarefa['categoria']} | Status: {status}")
        print(f"  Descrição: {tarefa['descricao']}")
    print("-------------------------------------")

def exibir_tarefas_por_categoria(categoria):
    encontradas = [t for t in tarefas if t["categoria"].lower() == categoria.lower()]
    if not encontradas:
        print(f"Nenhuma tarefa encontrada na categoria '{categoria}'.")
        return

    print(f"\n--- Tarefas na Categoria: {categoria.capitalize()} ---")
    for tarefa in encontradas:
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"ID: {tarefa['id']} | Nome: {tarefa['nome']} | Prioridade: {tarefa['prioridade']} | Status: {status}")
        print(f"  Descrição: {tarefa['descricao']}")
    print("-----------------------------------")

def remover_tarefa(tarefa_id):
    global tarefas
    tarefas_originais = len(tarefas)
    tarefas = [t for t in tarefas if t["id"] != tarefa_id]
    if len(tarefas) < tarefas_originais:
        print(f"Tarefa (ID: {tarefa_id}) removida com sucesso.")
    else:
        print(f"Erro: Tarefa com ID {tarefa_id} não encontrada.")

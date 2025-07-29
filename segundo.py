tarefas = [];

while True:

    tarefa = input("Digite uma tarefa (ou 'sair' para finalizar): ");
    if tarefa.lower() == "sair":
        break
    tarefas.append(tarefa);

tarefas.sort();
print("\nLista de Tarefas: ");
for t in tarefas:
    print(f"- {t}");
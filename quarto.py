import json;

clientes = [];

def adicionarCliente(nome, idade, cidade):
    clientes.append({"nome": nome, "idade": idade, "cidade": cidade});
    with open("bancoclientes.json", "w") as arquivo:
        json.dump(clientes, arquivo, indent=4)

adicionarCliente("Pedro", 20, "São Paulo");
adicionarCliente("Francisco", 19, "São Paulo");

with open("bancoclientes.json", "r") as arquivo:
    print(json.load(arquivo));

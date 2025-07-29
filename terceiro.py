def calcularMedia(notas):
    return sum(notas) / len(notas);

def verificarAprovacao(media):

    if media >= 7:
        return print("Você está aprovado!");
    else:
        return print("Você está reprovado!");

def exibirResultado(notas):
    media = calcularMedia(notas);
    status = verificarAprovacao(media);
    print(f"Média: {media:.2f}, Status: {status}");

notas = [];
while True:
    inputNota = int(input("Digite suas 4 notas: ")); 
    if len(notas) == 3:
        break
    
    if inputNota > 10 or inputNota < 0:
        print("Valor não suportado!");
    else:
        notas.append(inputNota);  

notas.sort();
exibirResultado(notas);

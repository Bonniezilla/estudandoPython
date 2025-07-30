data = open("./mensagem.txt", "r");

mensagem = data.read();

print(mensagem);
data.close();
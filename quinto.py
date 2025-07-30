import random;
import string;

def gerarSenha(tamanho):
    chars = string.ascii_letters + string.digits + string.punctuation; 
    senha = "".join(random.choice(chars) for _ in range(tamanho));
    
    return senha;

while True: 
    inputTamanho = int(input("Digite um tamanho de senha: "));
    
    if inputTamanho != int:
        break;

print("Senha gerada:", gerarSenha(inputTamanho));
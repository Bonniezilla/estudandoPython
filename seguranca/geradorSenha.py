import random;
import string;

def geradorSenha(tamanho):
    chars = string.ascii_letters + string.digits + string.punctuation; 
    senha = "".join(random.choice(chars) for _ in range(tamanho));
    
    return senha;
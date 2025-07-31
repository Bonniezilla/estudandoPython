from seguranca import geradorSenha as gerarSenha;

from seguranca import validarSenha as validador;

try:
        tamanho = int(input("Digite um tamanho de senha: "));

        if tamanho <= 0:
            raise ValueError;
        
except ValueError:
    print("Só é permitido números inteiros!");

else:
    senha = gerarSenha(tamanho);
    statusSenha = validador(senha);
    print("Sua senha é:", senha);

    if statusSenha == True:
        print("Esta senha é válida");

    else:
        print("Esta senha é inválida");


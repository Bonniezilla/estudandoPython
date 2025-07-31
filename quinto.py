from seguranca import geradorSenha as gerarSenha;

from seguranca import validarSenha as validador;

tamanho = int(input("Digite um tamanho de senha: "));


senha = gerarSenha(tamanho);
statusSenha = validador(senha);
print("Sua senha é:", senha);

if statusSenha == True:
    print("Esta senha é válida");

else:
    print("Esta senha é inválida");


nome = input("Qual seu nome? ");
idade = int(input("Qual sua idade? "));

print(f"Olá {nome}, você tem {idade} anos");

if idade >= 18 :
    print("Você é maior de idade!");

elif idade >= 0: 
    print("Você é menor de idade!");

else: 
    print("Você ainda nem nasceu!");
import re;

def validarSenha(senha):
    validarLetra = re.search(r'[A-Z]', senha);

    validarNumero = re.search(r'\d', senha);

    validarChar = re.search(r'[^a-zA-Z0-9]', senha); 


    status = bool(validarLetra and validarChar and validarNumero and len(senha) >= 8);
    
    return status;
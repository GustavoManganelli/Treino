# IMPORTA MODULO PADRÃO DO PYTHON PARA 
# EXPREÇÕES REGULARES
import re

# DEFINE VALOR MINÍMO E DE CARACTERES DA SENHA
MIN_CHARS:int = 8
# DEFINE QUAIS CARACTERES ESPECIAIS DEVEM SER 
# ENCONTRADOS NA SENHA 
S_CHARS = r'[!@#$%]'

# DEFINE FUNÇÃO PARA VALIDAR SENHA
def validatePassword(password:str) -> bool:
    # VERIFICA SE TEM QTDE MINÍMA DE CARACTERES
    has_min_char = len(password) < MIN_CHARS
    # VERIFICA SE POSSUI ALGUM CARACTER DE A A Z MINUSCULO
    has_lower = re.search(r'[a-z]', password) is not None
    # VERIFICA SE POSSUI ALGUM CARACTER a A z MAIÚSCULO
    has_upper = re.search(r'[A-Z]', password) is not None
    # VERIFICA SE POSSUI ALGUM CARACTER ESPECIAL
    has_s_char = re.search(S_CHARS, password) is not None

    # SE NÃO TIVER TAMANHO MINÍMO DE CARACTERES
    if(not has_min_char):
        print(f'A senha precisa ter ao menos {MIN_CHARS} caracteres.')
        return False
    # SE NÃO TIVER CARACTERES MINUSCULOS
    if(not has_lower):
        print(f'A sehnha precisa ter ao menos 1 caracter em letra minuscula')
        return False
    # SE NÃO TIVER CARACTERES MAIÚSCULOS
    if(not has_upper):
        print(f'A sehnha precisa ter ao menos 1 caracter em letra maiuscula')
        return False
    # SE NÃO TIVER CARACTERES ESPECIAIS
    if(not has_s_char):
        print(f'A sehnha precisa ter ao menos 1 dos simbolos ! @ # $ %')
        return False

    return True

# SE ESSE FOR O MODULO DE INICIAÇÃO DO PYTHON INICIA O CHECK
if __name__ == '__main__':
    # INPUT PARA A SENHA
    password = input('Coloque a senha a ser avaliada: ')
    # USA FUNÇÃO PARA VALIDAR SE É OU NÃO UMA 
    # SENHA VALIDA
    if(validatePassword(password)):
        print('Senha valida.')






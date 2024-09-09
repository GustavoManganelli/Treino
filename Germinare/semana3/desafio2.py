class bondQtd:
    def __init__(self, type, quantity, points) -> None:
        self.type = type
        self.quantity = quantity
        self.points = points
    

def convertStringToBool(string:str) -> bool:
    if(string.upper() in ['SIM', 'S']):
        return True
    if(string.upper() in ['NÃO', 'N']):
        return False
    
    return False

def generateBondQtd(qtdBond: float, qtdSalary: float, has_up_score: bool, has_deat: bool, has_public_emp: bool, has_open_bankign: bool):
    points:int = 0
    type_bond:str = ''
    per_bond:float = 0.0

    if((qtdBond*2) <= qtdSalary):
        points += 1

    if(has_up_score):
        points += 1
    if(has_deat):
        points += 1
    if(has_public_emp):
        points += 1
    if(has_open_bankign):
        points += 1

    if(points == 5):
        per_bond = 100
        type_bond = 'Aprovação total'
    elif(points in [3,4]):
        per_bond = 60
        type_bond = 'Aprovado com desconto'
    elif(points == 2):
        per_bond = 20
        type_bond = 'Aprovado com restrições'
    else:
        per_bond = 0
        type_bond = 'Não aprovado'

    per_bond = per_bond / 100

    bondCalc = qtdBond * per_bond

    bond = bondQtd(type_bond, bondCalc, points)

    return bond
    
    


# SE ESSE FOR O MODULO DE INICIAÇÃO DO PYTHON INICIA O CHECK
if __name__ == '__main__':
    # INPUT PARA A QTDE REQUERIDA
    qtdBondStr = input('Digite quanto você deseja pegar emprestado: ')
    # TRANSFORMA VALOR EM TEXTO (STRING) EM NUMERO DECIMAL (FLOAT)
    qtdBond = float(qtdBondStr)

    
    qtdSalaryStr = input('Digite quanto você recebe mensalmente: ')
    # TRANSFORMA VALOR EM TEXTO (STRING) EM NUMERO DECIMAL (FLOAT)
    qtdSalary = float(qtdSalaryStr)

    has_up_score = convertStringToBool(input('Possui score a cima de 450 pontos? '))
    has_deat = convertStringToBool(input('Possui divida ativa? '))
    has_public_emp = convertStringToBool(input('É funcionario publico? '))
    has_open_bankign = convertStringToBool(input('Partilha informações com outros bancos via open banking? '))


    bond = generateBondQtd(qtdBond,qtdSalary,has_up_score,has_deat,has_public_emp,has_open_bankign)


    print(f'Tipo: {bond.type}')
    print(f'Pontos: {bond.points}')
    print(f'Valor concedido: {bond.quantity}')
        
usuario = {
    "Gabriel": 1234,
    "Fulano": 4564,
    "Ciclano": 7456
}

def verificar_dados(nome, senha):
    if nome in usuario and usuario[nome] == senha:
        return True
    else:
        return False

def login():
    nome = str(input('Nome: '))
    senha = int(input('Senha: '))

    if verificar_dados(nome, senha):
        print('Login realizado com sucesso')
    else:
        print('Erro nas credenciais')


login()
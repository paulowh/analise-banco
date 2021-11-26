# %%
import pandas as pd
import glob
from getpass import getpass
from datetime import datetime

# %%
usuarioacesso = ['admin', 'lucas', 'luan', 'narumi']
acessoace = ['firns', 123, 321, 456]
teste2 = "firns"
teste = "['{}']".format(teste2)
#d = {'usuario':usuarioacesso,'senha':acessoace} # dicionário
batatinha = "admin"
#df = pd.DataFrame(d)
df = pd.read_csv('senhas.csv')
ola = df.query('usuario == "{}"'.format(batatinha)).loc[:,"senha"].values
ola = str(ola)
print(ola)
if teste == ola:
    print("Esta Vivo !!!")


# %%
confirmacao = False
cont = 0
senhaAcesso = ""


while confirmacao != True:

    usuario = input("Usuario: ")
    senha = getpass("Digite sua senha: ") #esconde a senha digitada

    key = 5
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' 
    senhaConvertida = ''
    #message = message.upper()
    df = pd.read_csv('senhas.csv')
    senhaAcesso = df.query('usuario == "{}"'.format(usuario)).loc[:,"senha"].values

    for symbol in senha: 
        if symbol in LETTERS:
            num = LETTERS.find(symbol) 
            num = num + key  
            if num >= len(LETTERS): 
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)
            senhaConvertida = senhaConvertida + LETTERS[num]
        else:
            senhaConvertida = senhaConvertida + symbol

    usuario = usuario.lower()
    if senhaConvertida == senhaAcesso:
        print("Acesso Permitido")
        print("")
        print(senhaAcesso, senhaConvertida)
        confirmacao = True
        break
    elif senhaConvertida != senhaAcesso:
        print("usuario ou senha incorreto")
        print("")
        print(senhaAcesso, senhaConvertida)
        cont += 1
    if cont == 3:
        print("Acesso bloquado, tente novamente mais tarde")
        break

if confirmacao == True:
    print("Seja bem vindo ao controle de estoque da H.F.A \n\n")# %%
    print("Escolha uma opção \n")
    print("1 - Cadastro de Produtos \n2 - Fechamento do Dia \n3 - Num Sei Ainda \n4 - Num Sei Ainda \n5 - Cadastro de Usuario\n")
    escolha = int(input())
    if escolha == 1:
        print('Cadastro de Produtos')
        #cadastro de produtos
        print("Seja bem vindo ao controle de estoque da H.F.A")

        #Declaração das variaveis
        continuar = True
        dia = datetime.today().strftime('%d-%m-%Y') #pega a data atual
        prod = []
        #quant = []
        data = []

        oldBanco = pd.read_csv('banco.csv', index_col=0, header=0) #backup do "banco de dados"

        #criação de novos pordutos
        while continuar == True:
            prod.append(input("Nome do Produto: "))
            data.append(input("Estoque Atual: ")) 
            #quant.append(input("Valor Original: ")) 
            escolha = input("Desenha continuar: (s/n)")
            if escolha == "n":
                continuar = False
                break
            else:
                continuar = True
        d = {'Produto':prod, dia:data} # dicionário
        atuBanco = pd.DataFrame(d)

        newBanco = pd.concat([oldBanco, atuBanco], axis=0, ignore_index=True, sort=False)
        newBanco.to_csv('banco.csv')
        newBanco
    elif escolha == 2:
        print('Fechamento do Dia')
        #Atualizar dia
        oldBanco = pd.read_csv('banco.csv', index_col=0, header=0)
        dia = datetime.today().strftime('%d-%m-%Y')

        atuEstoque=[]
        for i in range(oldBanco.Produto.count()):
            print("Qual a quantidade atual do Produto ", oldBanco.Produto[i], ": ")
            atuEstoque.append(input())

        oldBanco.loc[:,dia] = atuEstoque
        oldBanco.to_csv('banco.csv')
    elif escolha == 3:
        print('Num Sei Ainda')
    elif escolha == 4:
        print('Num Sei Ainda')
    elif escolha == 5:
        print('Cadastro de Usuario')
        #CADASTRO DE SENHAS
        oldSenha = pd.read_csv('senhas.csv', index_col=0, header=0) #backup do "banco de senha"
        user = []
        senha =""

        user.append(input("fala teu nome ai irmão: "))
        senha = input("Vai meu rei, qual a senha? ")

        key = 5
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' 
        senhaConvertida = ''
        #message = message.upper()
        for symbol in senha: 
            if symbol in LETTERS:
                num = LETTERS.find(symbol) 
                num = num + key  
                if num >= len(LETTERS): 
                    num = num - len(LETTERS)
                elif num < 0:
                    num = num + len(LETTERS)
                senhaConvertida = senhaConvertida + LETTERS[num]
            else:
                senhaConvertida = senhaConvertida + symbol

        d = {'usuario':user, 'senha':senhaConvertida} # dicionário
        atuSenhas = pd.DataFrame(d)

        newSenha = pd.concat([oldSenha, atuSenhas], axis=0, ignore_index=True, sort=False)
        newSenha.to_csv('senhas.csv')
        newSenha

# %%


# %%



# %%



# %%




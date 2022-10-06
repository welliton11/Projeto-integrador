from Val_Cartao import Cartao
import pycep_correios
import sqlite3


conexao = sqlite3.connect("projeto_pj_DB.db")
cursor = conexao.cursor()

class Cadastro:
    def __init__(self) -> None:
        pass
    def Inserir_Dados(self):
        while True:
            try:
                nome = str(input("\nDigite seu primeiro nome: ")).capitalize()
                sobrenome = str(input("Digite seu sobrenome: ")).capitalize()
                while True:
                    cpf = str(input("Digite seu cpf (apenas números): "))
                    total = int(0)
                    a = 10
                    for i in range(0, 9):
                        for l in cpf[i]:
                            x = (int(l) * int(a))
                            total += x
                            a -= 1
                    digito1 = (11 - (total % 11))
                    if digito1 >= 10:
                        digito1 = 0
                    n = 11
                    total2 = 0
                    for i in range(0, 10):
                        for l in cpf[i]:
                            s = (int(l) * int(n))
                            total2 += s
                            n -= 1
                    digito2 = 11 - (total2 % 11)
                    if digito2 >9:
                        digito2 = 0
                    if int(digito1) == int(cpf[9]) and int(digito2) == int(cpf[10]):
                        break
                    else:
                        print('CPF inválido!')
                print('\n\033[;1mAbaixo digite a data de seu nascimento em partes, começando com o dia, o mês e o ano.(dd/mm/aaaa)\n\033[m')
                while True:
                    dia = str(int(input("Digite o dia de seu nascimento: "))).zfill(2)
                    mes = str(int(input("Digite o mês de seu nascimento: "))).zfill(2)
                    ano = int(input("E o ano de nascimento: "))
                    if int(dia) < 1 or int(dia) > 31 or int(mes) < 1 or int(mes) > 12:
                        print('\nFormato de data inválido\n')
                    elif ano < 1900:
                        print('\nVocê não tem essa idade!\n')
                    elif ano > 2014:
                        print('\nVocê precisa ter mais que 8 anos!\n')
                    else:
                        break
                data_de_nascimento = '{}/{}/{}'.format(dia, mes, ano)
                email = input("\nDigite o seu email: ")
                while True:
                    senha = input("Digite o sua senha (A senha deve ter entre 6 a 12 dígitos): ")
                    if len(senha) < 6:
                        print('Senha muito curta.')
                        continue
                    if len(senha) > 12:
                        print('Senha muito longa.')
                        continue
                    break
                if len(str(cpf)) != 11 or len(str(dia)) > 2 or len(str(mes)) > 2 or len(str(ano)) != 4:
                    print('Por favor, digite os dados corretamente!')
                    continue
                if not nome or not sobrenome or not dia or not mes or not ano or not email or not senha:
                    print('Todos os campos são obrigatórios.')
                    continue
                self.dados = input(f'\n\033[;1mNome: {nome} \nSobrenome: {sobrenome} \nCPF: {cpf} \nData de Nascimento: {data_de_nascimento} \nEmail: {email}\n \nOs dados acima estão corretos? ("s" ou "n")\033[m\n').lower()
                if self.dados == 's':
                    break
                if self.dados == 'n':
                    print('\n\033[1;91mPor favor, digite seus dados novamente.\033[m\n')
                    continue
                else:
                    print('\n\033[1;31mOpção inválida!\033[m\n')
            except:
                print('\n\n\033[1;31mDigite seus dados corretamente.\033[m\n')
        cursor.execute(f'INSERT INTO cadastro (nome, sobrenome, data_de_nascimento, cpf, email, senha) VALUES ("{nome}", "{sobrenome}", "{data_de_nascimento}", {cpf}, "{email}", "{senha}")')
        cursor.execute('SELECT * FROM cadastro')
        conexao.commit()
        cursor.execute(f'INSERT INTO carrinho (email2) VALUES ("{email}")')
        cursor.execute('SELECT * FROM carrinho')
        conexao.commit()
        cursor.execute(f'INSERT INTO favoritos (email3) VALUES ("{email}")')
        cursor.execute('SELECT * FROM favoritos')
        conexao.commit()
        cursor.execute(f'INSERT INTO endereço (email4) VALUES ("{email}")')
        cursor.execute('SELECT * FROM endereço')
        conexao.commit()
        cursor.execute(f'INSERT INTO cartao_de_credito (email5) VALUES ("{email}")')
        cursor.execute('SELECT * FROM cartao_de_credito')
        conexao.commit()
        cursor.execute(f'INSERT INTO cadastro (email6) VALUES ("{email}")')
        cursor.execute('SELECT * FROM cadastro')
        conexao.commit()
        
    def Entrar_na_Conta(self):
        a = True
        while True:
            self.email_confirm = input('\nEmail: ')
            self.senha_confirm = input('Senha: ')
            if not self.email_confirm or not self.senha_confirm:
                print('\033[1;31mVocê não pode deixar espaços em brancos.\033[m')
                continue
            cursor.execute(f'SELECT * FROM cadastro')
            for linha in cursor.fetchall():
                if linha[4] == self.email_confirm and linha[5] == self.senha_confirm:
                    print('\033[32mConectado\033[m')
                    self.senha_confirm = input('Confirme sua senha para ter acesso a sua conta: ')
                    while self.senha_confirm != linha[5]:
                        print('\033[1;31mSenha incorreta.\033[m')
                        self.senha_confirm = input('Confirme sua senha para ter acesso a sua conta: ')
                    a = False
                    print(f"\nBem vindo de volta, {linha[0]}.")
                else:
                    continue
            if a == True:
                print('\033[1;31m\nEmail ou senha incorretos, tente novamente.\033[m')
                continue
            break
class Categorias:
    def __init__(self) -> None:
        pass
    def Inserir_Produtos(self, cat):
        self.cat = cat
        self.cat = input('\n1.Eletrônicos \n2.Periféricos \n3.Jogos \n\nVocê deseja inserir produto em qual categoria?\n')
        match cat:
            case 1:
                self.produto = input('Digite o nome do produto: ')
                self.valor = input('Digite o preço do produto: ')
                cursor.execute(f'INSERT INTO eletronicos (produto, valor) VALUES ("{self.produto}", "{self.valor}")')
                cursor.execute('SELECT * FROM eletronicos')
                conexao.commit()
            case 2:
                self.produto = input('Digite o nome do produto: ')
                self.valor = input('Digite o preço do produto: ')
                cursor.execute(f'INSERT INTO perifericos (produto, valor) VALUES ("{self.produto}", "{self.valor}")')
                cursor.execute('SELECT * FROM perifericos')
                conexao.commit()
            case 3:
                self.produto = input('Digite o nome do produto: ')
                self.valor = input('Digite o preço do produto: ')
                cursor.execute(f'INSERT INTO jogos (produto, valor) VALUES ("{self.produto}", "{self.valor}")')
                cursor.execute('SELECT * FROM jogos')
                conexao.commit()
    def Eletronicos(self):
        cursor.execute('SELECT * FROM eletronicos')
        for linha in cursor.fetchall():
            print('\n',linha)
        print('')
    def Perifericos(self):
        cursor.execute('SELECT * FROM perifericos')
        for linha in cursor.fetchall():
            print('\n',linha)
        print('')
    def Jogos(self):
        cursor.execute('SELECT * FROM jogos')
        for linha in cursor.fetchall():
            print('\n',linha)
        print('')
class Produtos:
    def __init__(self, Produto, Valor) -> None:
        self.produto = Produto
        self.valor = Valor
class Pagamentos:
    def __init__(self) -> None:
        pass
    def Formas_Pag(self):
        while True:
            m = True
            contador = 0
            while m == True:
                self.email_test = input('Para continuar, digite seu email: ')
                cursor.execute('SELECT * FROM cartão_de_credito')
                for linha in cursor.fetchall():
                    if linha == self.email_test:
                        cursor.execute(f'SELECT * FROM cartão_de_credito WHERE email = "{self.email_test}"')
                        for i in cursor.fetchall():
                            for j in i:
                                if j != None:
                                    contador +=1
                        m = False
                        if contador <= 2:
                            utilizar_cartão = ('Você ja tem um cartão salvo, deseja utilizá-lo? ("s" ou "n"): ').lower()
                            if utilizar_cartão == "s":
                                pass # ** DESENVOLVER ESTA PARTE **
                            elif utilizar_cartão == "n":
                                break
                            else:
                                print('Opção inválida, seu endereço não será salvo!!')
                                break
                        break
                print('Você digitou o email errado, digite novamente.')
            while True:
                endereco = pycep_correios.get_address_from_cep(input('\n\033[;1mENDEREÇO DE ENTREGA:\033[m \nDigite seu cep: '))
                self.numero = input('Digite o número da casa: ')
                self.complemento = input('Digite o complemento: ')
                self.rua = print(endereco['logradouro'])
                self.bairro = print(endereco['bairro'])
                self.cidade = print(endereco['cidade'])
                self.uf = print(endereco['uf'])
                self.cep = print(endereco['cep'])
                print(f'{self.numero} \n{self.complemento}')
                gg = str(input('Os dados acima estão corretos? ("s" ou "n"): ')).lower()
                if gg == "s":
                    pass
                elif gg == "n":
                    continue
                salvar_endereço = input('Você deseja salvar seu endereço para compras futuras? ("s" ou "n"): ').lower()
                if salvar_endereço == "s":
                    pass
                elif salvar_endereço == "n":
                    break
                else:
                    print('Opção inválida, seu endereço não será salvo!!')
                    break
                cursor.execute(f'INSERT INTO endereço (cep, rua, bairro, cidade, uf, numero, complemento) VALUES ("{self.cep}", "{self.rua}", "{self.bairro}", "{self.cidade}", "{self.uf}", "{self.numero}", "{self.complemento}")')
                cursor.execute('SELECT * FROM endereço')
                conexao.commit()
                break

            while True:
                self.nome2 = str(input('\n\033[;1mNome do titular do cartão:\033[m\nNome completo: ')).upper()
                print('\n\033[;1mNúmero do cartão:\033[m')
                cc = Cartao()
                self.num_cartao = cc.Validar()
                self.val_mes = int(input('\n\033[;1mValidade:\033[m\nMês: '))
                self.val_ano = int(input('\nAno: '))
                self.validade = '{}/{}'.format(self.val_mes, self.val_ano)
                self.cvv = input('\n\033[;1mCódigo de segurança:\033[m\nCVV: ')
                if not self.nome2 or not self.num_cartao or not self.val_ano or not self.val_mes or not self.cvv:
                    print('\nVocê não pode deixar nenhum campo em branco!\n')
                    continue
                if self.val_mes != 2 or self.val_ano != 4 or self.cvv < 3 or self.cvv > 4:
                    print('\nPor favor, digite corretamente!\n')
                    continue
                print(f'\n{self.nome2} \n{self.num_cartao} \n{self.validade} \n{self.cvv} \n')
                self.hh = int(input('Os dados acima estão corretos? ("s" ou "n"): ')).lower()
                if self.hh == "n":
                    print('Ok, digite novamente seus dados!')
                    continue
                elif self.hh == "s":
                    pass
                else:
                    print('Opção inválida, refaça novamente seus dados!')
                    continue
                break
            m = True
            while m == True:
                self.email_test = input('Para continuar, digite seu email novamente: ')
                cursor.execute('SELECT * FROM cartão_de_credito')
                for linha in cursor.fetchall():
                    if linha == self.email_test:
                        m = False
                        break
                print('Você digitou o email errado, digite novamente.')
            salvar_cartao = input('Você deseja salvar seu cartão para compras futuras? ("s" ou "n"): ').lower()
            if salvar_cartao == "s":
                pass
            elif salvar_cartao == "n":
                break
            else:
                print('Opção inválida, seu cartão não será salvo!!')
                break
            cursor.execute(f'UPDATE cartao_de_credito SET nome2 = ?, numero_do_cartao = ?, validade_cartao = ?, cvv = ? WHERE email = "{self.email_test}"', (self.nome2, self.num_cartao, self.validade, self.cvv))
            cursor.execute('SELECT * FROM cartao_de_credito')
            conexao.commit()
            break

class Carrinho(Pagamentos):
    def __init__(self) -> None:
        cursor.execute('SELECT * FROM carrinho')
        for linha in cursor.fetchall():
            id, email2, produto2, valor2 = linha
            print('\n',linha)
class Favoritos:
    def __init__(self, Produto3, Valor3, Email3) -> None:
        pass


print("\033[1;0m \033[1;106mOLÁ SEJA BEM VINDO A PEDRINHO ELETRONICOS!\033[m \033[m\n\n")
print("\033[;1mENTRE E APROVEITE A VARIEDADES DE PRODUTOS\033[m")
cad = int(input('1.Cadastrar \n2.Entrar na conta \n3.Entrar como convidado \n4.Sair \n\033[;1mDIGITE A OPÇÃO DESEJADA:\033[m\n'))
cadastro = Cadastro()
match cad:
    case 1:
        cadastro.Inserir_Dados()
        print("\nCADASTRO FEITO COM SUCESSO, APROVEITE A NOSSA LOJA.")
    case 2:
        cadastro.Entrar_na_Conta()
    case 3:
        print('Bem vindo a nossa loja!!!')
        pag = Pagamentos()
        pag.Formas_Pag()
    case 4:
        print('\033[1;46m\033[1m\nOBRIGADO POR SUA VISITA, VOLTE SEMPRE!!!\033[m')
        exit()

while True:
    cc = int(input('\n\033[1;31mCATEGORIAS DE PRODUTOS \033[m \n1.Eletrônicos \n2.Periféricos \n3.Jogos \n4.Sair \n\nDigite o número do departamento desejado: \n'))
    categorias = Categorias()
    match cc:
        case 1:
            categorias.Eletronicos()
        case 2:
            categorias.Perifericos()
        case 3:
            categorias.Jogos()
        case 4:
            print('\033[1;46m\033[1m\nOBRIGADO POR SUA VISITA, VOLTE SEMPRE!!!\033[m')
            exit()

    pg = int(input('1.Ver produtos \n2.Ir a Carrinho de compras \n3.Lista de desejos \n4.Departamentos \n5.Sair \n\033[;1mDIGITE A OPÇÃO DESEJADA:\033[m\n'))
    match pg:
        case 1:
            int(input('Digite o número do produto: \n'))
        case 2:
            pass
        case 3:
            pass
        case 4:
            continue
        case 5:
            print('\033[1;46m\033[1m\nOBRIGADO POR SUA VISITA, VOLTE SEMPRE!!!\033[m')
            exit()
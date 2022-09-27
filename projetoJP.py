import sqlite3


conexao = sqlite3.connect("projeto_pj_DB.db")
cursor = conexao.cursor()

class Cadastro:
    def __init__(self) -> None:
        pass
    def Inserir_Dados(self, nome, data_de_nascimento, cpf, email, senha, dados):
        self.dados = dados
        while True:
            try:
                nome = str(input("Digite seu nome completo: "))
                cpf = int(input("Digite seu cpf sem pontos: "))
                print('\n\033[;1mAbaixo digite a data de seu nascimento em partes, começando com o dia, o mês e o ano.(dd/mm/aaaa)\n\033[m')
                while True:
                    dia = int(input("Digite o dia de seu nascimento: "))
                    mes = int(input("Digite o mês de seu nascimento: "))
                    ano = int(input("E o ano de nascimento: "))
                    if dia < 1 or dia > 31 or mes < 1 or mes > 12:
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
                    senha = input("\nDigite o sua senha (A senha deve ter entre 6 a 12 dígitos): ")
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
                if not nome or not dia or not mes or not ano or not email or not senha:
                    print('Todos os campos são obrigatórios.')
                    continue
                self.dados = input(f'\n\033[;1mNome: {nome} \nCPF: {cpf} \nData de Nascimento: {data_de_nascimento} \nEmail: {email}\n \nOs dados acima estão corretos? ("s" ou "n")\033[m\n').lower()
                if self.dados == 's':
                    break
                if self.dados == 'n':
                    print('\n\033[1;91mPor favor, digite seus dados novamente.\033[m\n')
                    continue
            except:
                print('\n\n\033[1;31mDigite seus dados corretamente.\033[m\n')
        cursor.execute(f'INSERT INTO cadastro (nome, data_de_nascimento, cpf, email, senha) VALUES ("{nome}", {data_de_nascimento}, {cpf}, "{email}", "{senha}")')
        cursor.execute('SELECT * FROM cadastro')
        conexao.commit()

    def Entrar_na_Conta(self, email_confirm, senha_confirm):
        self.email_confirm = email_confirm
        self.senha_confirm = senha_confirm
        self.email_confirm = input('\nEmail: ')
        self.senha_confirm = input('Senha: ')
        cursor.execute('SELECT * FROM cadastro')
        for linha in cursor.fetchall():
            if linha[3] == self.email_confirm and linha[4] == self.senha_confirm:
                print('\033[32mConectado\033[m')
                self.senha_confirm = input('Confirme sua senha para ter acesso a sua conta: ')
                while self.senha_confirm != linha[4]:
                    print('\033[1;31mEmail incorreto.\033[m')
                    self.senha_confirm = input('Confirme sua senha para ter acesso a sua conta: ')
                a = False
            else:
                continue
            if a == True:
                print('\033[1;31m\nSenha incorreta, tente novamente.\033[m')
                continue
class Categorias:
    def __init__(self, Produto, Valor) -> None:
        self.produto = Produto
        self.valor = Valor
    def Eletronicos(self, Produto, Valor):
        pass
    def Perifericos(self, Produto, Valor):
        pass
    def Jogos(self, Produto, Valor):
        pass
class Produtos:
    def __init__(self, Produto, Valor) -> None:
        self.produto = Produto
        self.valor = Valor
class Pagamentos:
    def __init__(self, Nome2, CPF2, Numero_do_Cartão, Validade_cartão, CVV, Email5) -> None:
        self.nome2 = Nome2
        self.cpf2 = CPF2
        self.num_cartao = Numero_do_Cartão
        self.validade = Validade_cartão
        self.cvv = CVV
        self.email = Email5
class Carrinho:
    def __init__(self, Produto2, Valor2, Email2) -> None:
        pass
class Favoritos:
    def __init__(self, Produto3, Valor3, Email3) -> None:
        pass


print("\033[1;0m \033[1;106mOLÁ SEJA BEM VINDO A PEDRINHO ELETRONICOS!\033[m \033[m\n\n")
print("\033[;1mENTRE EM SUA CONTA OU CRIE UMA AGORA A APROVEITE A VARIEDADES DE PRODUTOS\033[m")
cad = int(input('1.Cadastrar \n2.Entrar na conta \n\033[;1mDIGITE A OPÇÃO DESEJADA:\033[m\n'))
cadastro = Cadastro()
match cad:
    case 1:
        cadastro.Inserir_Dados('','','','','','')
        print("\nCADASTRO FEITO COM SUCESSO, APROVEITE A NOSSA LOJA.")
    case 2:
        cadastro.Entrar_na_Conta('','')
        print("")
        print("\nCONTA LOGADA COM SUCESSO, BEM-VINDO A NOSSA LOJA.")
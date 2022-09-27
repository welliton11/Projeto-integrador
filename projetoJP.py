import sqlite3


conexao = sqlite3.connect("projeto_pj_DB.db")
cursor = conexao.cursor()

class Cadastro:
    def __init__(self) -> None:
        pass
    def Inserir_Dados(self, nome, data_de_nascimento, cpf, email, senha):
        while True:
            nome = str(input("Digite seu nome completo: "))
            cpf = int(input("Digite seu cpf sem pontos: "))
            print('\n\033[;1mAbaixo digite a data de seu nascimento em partes, começando com o dia, o mês e o ano.(dd/mm/aaaa)\n\033[m')
            dia = int(input("Digite o dia de seu nascimento: "))
            mes = int(input("Digite o mês de seu nascimento: "))
            ano = int(input("E o ano de nascimento: "))
            data_de_nascimento = '{}/{}/{}'.format(dia, mes, ano)
            email = input("Digite o seu email: ")
            senha = input("Digite o sua senha: ")
            if not nome or not dia or not mes or not ano or not email or not senha:
                print('Todos os campos são obrigatórios.')
                continue
            break  
        cursor.execute(f'INSERT INTO cadastro (nome, data_de_nascimento, cpf, email, senha) VALUES ("{nome}", {data_de_nascimento}, {cpf}, "{email}", "{senha}")')
        cursor.execute('SELECT * FROM cadastro')
        conexao.commit()
    def Entrar_na_Conta(self):
        email = input('\nEmail: ')
        senha = input('Senha: ')
        cursor.execute('SELECT * FROM conta')
        for linha in cursor.fetchall():
            if linha[1] == email and linha[2] == senha:
                print('\033[32mConectado\033[m')
                email2 = input('Confirme seu email para ter acesso ao menu netflix: ')
                while email2 != email:
                    print('\033[1;31mEmail incorreto.\033[m')
                    email2 = input('Confirme seu email para criar um perfil.')
                a = False
            else:
                continue
            if a == True:
                print('\033[1;31m\nEmail incorreto, tente novamente.\033[m')
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
cad = int(input('1.Entrar na conta \n2.Cadastrar \n\033[;1mDIGITE A OPÇÃO DESEJADA:\033[m\n'))
cadastro = Cadastro()
match cad:
    case 1:
        cadastro.Inserir_Dados('','','','','')
        print("\nCADASTRO FEITO COM SUCESSO, APROVEITE A NOSSA LOJA.")
    case 2:
        cadastro.Entrar_na_Conta()
        print("")
        print("\nCONTA LOGADA COM SUCESSO, BEM-VINDO A NOSSA LOJA.")
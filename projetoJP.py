import sqlite3
conexao = sqlite3.connect("projeto_pj_DB.db")
cursor = conexao.cursor()

class Cadastro:
    def __init__(self) -> None:
        pass
    def Inserir_Dados(self, nome, data_de_nascimento, cpf, email, senha):
        data_de_nascimento = []
        nome = input("Digite seu nome completo: ")
        data_de_nascimento.append(input("Digite o dia de seu nascimento: "))
        data_de_nascimento.append(input("Digite o mês de seu nascimento: "))
        data_de_nascimento.append(input("E o ano de nascimento: "))
        email = input("Digite o seu email: ")
        senha = input("Digite o sua senha: ")
        
        cursor.execute('INSERT INTO cadastro (nome, data_de_nascimento, cpf, email, senha) VALUES (?,?,?)',(nome, data_de_nascimento, cpf, email, senha))
        cursor.execute('SELECT * FROM cadastro')
        conexao.commit()
    def Entrar_na_Conta(self):
        pass
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

match cad:
    case 1:
        login1.inserirCadastramento()
        print("")
        print("CADASTRO FEITO COM SUCESSO, APROVEITE A NOSSA LOJA.")
    case 2:
        cadastro = Cadastro()
        login1.entrarLogin()
        print("")
        print("\nCONTA LOGADA COM SUCESSO, BEM-VINDO A NOSSA LOJA.")
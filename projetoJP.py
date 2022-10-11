from Val_Cartao import Cartao
from datetime import date
import pycep_correios
import sqlite3
import time


conexao = sqlite3.connect("projeto_pj_DB.db")
cursor = conexao.cursor()

email_global = []
total_pagar = []
class Cadastro():
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
                    pass
                elif self.dados == 'n':
                    print('\n\033[1;31mPor favor, digite seus dados novamente.\033[m')
                    continue
                else:
                    print('\n\033[1;31mOpção inválida! Por favor, digite corretamente.\033[m\n')
            except:
                print('\n\n\033[1;31mDigite seus dados corretamente.\033[m\n')
                continue
            try:
                cursor.execute(f'INSERT INTO cadastro (nome, sobrenome, data_de_nascimento, cpf, email, senha) VALUES ("{nome}", "{sobrenome}", "{data_de_nascimento}", {cpf}, "{email}", "{senha}")')
                cursor.execute('SELECT * FROM cadastro')
                conexao.commit()
                break
            except:
                print('\n\033[1;31mEmail já existente.\n\033[m')
                continue
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
                    print(f"\n\033[1mBem vindo de volta, {linha[0]}.\033[m")
                    email_global.append(self.email_confirm)
                else:
                    continue
            if a == True:
                print('\033[1;31m\nEmail ou senha incorretos, tente novamente.\033[m')
                continue
            break
        
class Categorias():
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
            case __:
                print('\n\033[1;31mOpção inválida!\033[m\n')
    def Eletronicos(self):
        cursor.execute('SELECT * FROM eletronicos')
        for linha in cursor.fetchall():
            n_id, prod, rs = linha
            print(f'\033[;1m{n_id}-\033[m{prod}, R${rs}\n')
    def Perifericos(self):
        cursor.execute('SELECT * FROM perifericos')
        for linha in cursor.fetchall():
            n_id, prod, rs = linha
            print(f'\033[;1m{n_id}-\033[m{prod}, R${rs}\n')
    def Jogos(self):
        cursor.execute('SELECT * FROM jogos')
        for linha in cursor.fetchall():
            n_id, prod, rs = linha
            print(f'\033[;1m{n_id}-\033[m{prod}, R${rs}\n')

class Produtos():
    def __init__(self) -> None:
        pass
    def Inserir_no_Carrinho(self):
        t = True
        selecionar = int(input('Digite o número do produto: \n'))
        cursor.execute(f'SELECT * FROM {cc} WHERE id = {selecionar}')
        for linha in cursor.fetchall():
            num_id, produto, valor = linha
            print(f'\n\033[;1m{num_id}-\033[m {produto} \nR${valor}\n')
        esc = int(input('1.Adicionar ao carrinho \n2.Voltar \n\n\033[1mESCOLHA A OPÇÃO DESEJADA: \n\033[m\n'))
        match esc:
            case 1:
                cursor.execute('SELECT * FROM carrinho')
                cursor.execute(f'INSERT INTO carrinho (email2, produto2, valor2) VALUES ("{email_global[0]}", "{produto}", "{valor}")')
                conexao.commit()
                print('\n\033[1mSeu produto foi adicionado ao carrinho!!\n\033[m')
            case 2:
                pass
            case __:
                print('\n\033[1;31mOpção inválida!\033[m\n')
    def Compras_feitas(self):
        t = True
        cursor.execute(f'SELECT * FROM compras_realizadas WHERE email6 = "{email_global[0]}"')
        for linha in cursor.fetchall():
            if linha[3] == email_global[0]:
                produto6, valor6, data_compra, email6 = linha
                print(f'\n\033[1m{data_compra}\033[m \n"{produto6}", R${valor6}\n')
                t = False
            continue
        if t == True:
            print('\n\033[1mVocê não fez nenhuma compra!\n\033[m')

class Carrinho():
    def __init__(self) -> None:
        pass
    def Carrinho_compras(self):
        carrinho_sair = True
        contador = 0
        self.total = 0
        cursor.execute(f'SELECT * FROM carrinho WHERE email2 = "{email_global[0]}"')
        for linha in cursor.fetchall():
            n_id7, emmail7, jogo7, valors7 = linha
            self.total += linha[3]
            contador += 1
        if contador == 0:
            print('\nSeu carrinho está vazio!!\n')
            carrinho_sair = False
        while carrinho_sair == True:
            options = input(f'\n\033[;1mTOTAL: R$ {float(self.total)}\033[m \n\n1.Comprar \n2.Remover do carrinho \n3.Voltar \n\n\033[1mDIGITE A OPÇÃO DESEJADA:\033[m\n')
            match int(options):
                case 1:
                    total_pagar.append(str(self.total))
                    pagg = Pagamentos()
                    pagg.Formas_Pag()

                    break
                case 2:
                    ttt = True
                    num_id = int(input('\nDigite o id do produto que deseja excluir: '))
                    cursor.execute(f'SELECT * FROM carrinho WHERE email2 = "{email_global[0]}"')
                    for linha in cursor.fetchall():
                        if linha[0] == num_id:
                            ttt = False
                            break
                    if ttt == True:
                        print('\nVocê não tem este produto no seu carrinho!!\n')
                        carr.Carrinho_compras()
                    cursor.execute(f'SELECT * FROM carrinho WHERE email2 = "{email_global[0]}"')
                    cursor.execute('DELETE FROM carrinho WHERE id = ?', (num_id,))
                    conexao.commit()
                    print('\n\033[0;32mProduto removido!!\n\033[m')
                case 3:
                    break
                case __:
                    print('\n\033[1;31mOpção inválida!\033[m\n')

class Pagamentos():
    def __init__(self) -> None:
        pass
    def Formas_Pag(self):
        aaa = True
        bbb = True
        m = True
        self.total = float(total_pagar[0])
        contador = 0
        cursor.execute('SELECT * FROM cartao_de_credito')
        for linha in cursor.fetchall():
            if linha[5] == email_global[0]:
                utilizar_cartão = input('\nVocê ja tem cartão de crédito salvo, deseja utilizá-lo? ("s" ou "n"): \n').lower()
                if utilizar_cartão == "s":
                    bbb = False
                    cursor.execute(f'SELECT * FROM cartao_de_credito WHERE email5 = "{email_global[0]}"')
                    for linha in cursor.fetchall():
                        num_id2, nome, numero_do_cartao, validade_cartao, cvv, email5 = linha
                        print(f'\n{num_id2}. {nome}, {numero_do_cartao}, {validade_cartao}\n')
                        contador += 1
                    if contador >= 2:
                        while True:
                            cartao_salvo = int(input(f'Escolha o cartão que deseja utilizar (1 ao {contador}): '))
                            if cartao_salvo > contador or cartao_salvo < 1:
                                print('\033[1;31mOpção inválida, por favor digite corretamente.\033[m')
                                continue
                            break
                        cursor.execute(f'SELECT * FROM cartao_de_credito WHERE email = "{email_global[0]}", id = {contador}')
                        for linha in cursor.fetchall():
                            num_id2, nome, numero_do_cartao, validade_cartao, cvv = linha
                            print(f'{num_id2}. {nome}, {numero_do_cartao}, {validade_cartao}')
                    contador = 0
                    while True:
                        confirm_cvv = input('\nDigite o cvv do cartão para continuar: \n')
                        if int(confirm_cvv) == cvv:
                            print('\n\033[1mSELECIONADO!\n\033[m')
                            break
                        contador += 1
                        if contador == 3:
                            print('\n\033[1mLimite de tentativas excedidos, tente novamente mais tarde!\033[m\n')
                            carr.Carrinho_compras()
                            break
                        if int(confirm_cvv) != cvv:
                            print('\n\033[1;31mCódigo cvv incorreto!!\n\033[m')
                            continue
                elif utilizar_cartão == "n":
                    pass
                else:
                    print('\n\033[1;31mOpção inválida!!\n\033[m')
                    continue

        cursor.execute('SELECT * FROM endereço')
        for linha in cursor.fetchall():
            if linha[8] == email_global[0]:
                contador = 0
                utilizar_endereco = input('Você ja tem endereço salvo, deseja utilizá-lo? ("s" ou "n"): \n').lower()
                if utilizar_endereco == "s":
                    aaa = False
                    cursor.execute(f'SELECT * FROM endereço WHERE email4 = "{email_global[0]}"')
                    for linha in cursor.fetchall():
                        num_id3, cep, rua, bairro, cidade, uf, numero, complemento, email4 = linha
                        print(f'\n\033[;1m{num_id3}:\033[m \n{cep} \n{rua}, {numero} \n{complemento} \n{bairro} \n{cidade} \n{uf} \n')
                        contador += 1
                    if contador >= 2:
                        while m == True:
                            endereco_salvo = int(input(f'\nDigite o número do endereço: '))
                            cursor.execute(f'SELECT * FROM endereço WHERE email4 = "{email_global[0]}" or id = {endereco_salvo}')
                            for linha in cursor.fetchall():
                                if endereco_salvo == linha[0]:
                                    num_id3, cep, rua, bairro, cidade, uf, numero, complemento, email4 = linha
                                    print(f'\n{cep} \n{rua}, {numero} \n{complemento} \n{bairro} \n{cidade} \n{uf} \n')
                                    m = False
                                    break
                            if m == True:
                                print('\nOpção inválida, por favor digite corretamente.\n')
                                continue
                    self.cep = cep
                    self.rua = rua
                    self.bairro = bairro
                    self.cidade = cidade
                    self.uf = uf
                    self.numero = numero
                    self.complemento = complemento
                elif utilizar_endereco == "n":
                    m = False
                    pass
            if m == True:
                if linha[8] != email_global[0]:
                    continue
            break

        while aaa == True:
            endereco = pycep_correios.get_address_from_cep(input('\n\033[;1mENDEREÇO DE ENTREGA:\033[m \n\nDigite seu cep: '))
            self.numero = input('Digite o número da casa: ')
            self.complemento = input('Digite o complemento (casa, apartamento ou comercial): ').capitalize()
            if not self.numero or not self.complemento:
                print('Todos os campos são obrigatórios.')
                continue
            BOLD    = "\033[;1m"
            print('')
            print(BOLD +endereco['logradouro'].capitalize())
            print(endereco['bairro'].capitalize())
            print(endereco['cidade'].capitalize())
            print(endereco['uf'].upper())
            print(endereco['cep'])
            print(f'{self.numero} \n{self.complemento}\033[m'.capitalize())
            gg = input('\nOs dados acima estão corretos? ("s" ou "n"): \n').lower()
            if str(gg) == "s":
                self.rua = (endereco['logradouro'].capitalize())
                self.bairro = (endereco['bairro'].capitalize())
                self.cidade = (endereco['cidade'].capitalize())
                self.uf = (endereco['uf'].upper())
                self.cep = (endereco['cep'])
            elif str(gg) == "n":
                continue
            salvar_endereço = input('\nVocê deseja salvar seu endereço para compras futuras? ("s" ou "n"): \n').lower()
            if salvar_endereço == "s":
                pass
            elif salvar_endereço == "n":
                break
            else:
                print('\n\033[1;31mOpção inválida, seu endereço não será salvo!!\033[m\n')
                break
            cursor.execute(f'INSERT INTO endereço (cep, rua, bairro, cidade, uf, numero, complemento, email4) VALUES ("{self.cep}", "{self.rua}", "{self.bairro}", "{self.cidade}", "{self.uf}", "{self.numero}", "{self.complemento}", "{email_global[0]}")')
            cursor.execute('SELECT * FROM endereço')
            conexao.commit()
            break

        while bbb == True:
            self.nome2 = str(input('\n\033[;1mCartão de Crédito:\033[m \n\nNome completo: ')).upper()
            print('\n\033[;1mNúmero do cartão:\033[m')
            cc = Cartao()
            self.num_cartao = cc.Validar()
            self.val_mes = str(input('\n\033[;1mValidade:\033[m\nMês: ')).zfill(2)
            self.val_ano = int(input('\nAno: '))
            self.validade = '{}/{}'.format(self.val_mes, self.val_ano)
            self.cvv = input('\n\033[;1mCódigo de segurança:\033[m\nCVV: ')
            if not self.nome2 or not self.num_cartao or not self.val_ano or not self.val_mes or not self.cvv:
                print('\nVocê não pode deixar nenhum campo em branco!\n')
                continue
            if self.val_ano < 2022:
                print('\033[1;31m\nSeu cartão esta vencido, por favor use um cartão válido!\n\033[m')
                continue
            if (len(self.val_mes) != 2) or int(self.val_mes) > 12 or int(self.val_mes) < 1 or len(str(self.val_ano)) != 4:
                print('\n\033[1;31mPor favor, digite corretamente!\033[m\n')
                continue
            if int(self.cvv) < 3 and int(self.cvv) > 4:
                print('\n\033[1;31mCódigo CVV inválido!\n\033[m')
                continue
            print(f'\n{self.nome2} \n{self.num_cartao} \n{self.validade} \n{self.cvv} \n')
            self.hh = input('\nOs dados acima estão corretos? ("s" ou "n"): \n').lower()
            if self.hh == "n":
                print('\n\033[1mOk, digite novamente seus dados!\033[m')
                continue
            elif self.hh == "s":
                break
            else:
                print('\n\033[1;31mOpção inválida, refaça novamente seus dados!\033[m\n')
                continue

        while True:
            self.parcelas = input('\033[1m\nVocê pode parcelar em até 8x sem juros ou em até 12x com juros de 3,5% no cartão. Digite de 1 à 12 de acordo com o número de parcelas desejadas: \033[m\n')
            if int(self.parcelas) >= 1 and int(self.parcelas) <= 8:
                calculo = self.total / int(self.parcelas)
                print(f'\nParcelas: {self.parcelas}x de {calculo} \nTotal: {self.total}\n')
                break
            elif int(self.parcelas) >= 9 and int(self.parcelas) <= 12:
                calculo = self.total / int(self.parcelas)
                calculo_juros = calculo + (calculo*(3.5/100))
                novo_total = calculo_juros * int(self.parcelas)
                print(f'\nParcelas: {self.parcelas}x de {calculo_juros:.2f} \nTotal: {novo_total}\n')
                break
            else:
                print('\033[1;31m\nOpção inválida, você só pode digitar de 1 à 12!\033[m\n')
                continue

        salvar_cartao = input('\n\033[1mVocê deseja salvar seu cartão para compras futuras? ("s" ou "n"): \033[m\n').lower()
        m = True
        if salvar_cartao == "s":
            m = False
        elif salvar_cartao == "n":
            pass
        else:
            print('\033[1;31m\nOpção inválida, seu cartão não será salvo!!\033[m\n')

        if m == False:
            cursor.execute(f'INSERT INTO cartao_de_credito (nome2, numero_do_cartao, validade_cartao, cvv, email5) VALUES ("{self.nome2}", "{self.num_cartao}", "{self.validade}", "{self.cvv}", "{email_global[0]}")')
            cursor.execute('SELECT * FROM cartao_de_credito')
            conexao.commit()
            print('\n\033[0;32mCartão salvo !!\033[m\n')

while True:
    try:
        print("\n\n\033[1;46m\033[1m BEM VINDO A PEDRINHO ELETRÔNICOS!\033[m")
        cad = input('\n1.Cadastrar \n2.Entrar na conta \n3.Entrar como convidado \n4.Sair \n\n\033[;1mDIGITE A OPÇÃO DESEJADA:\033[m\n')
        cadastro = Cadastro()
        convidado1 = True
        match int(cad):
            case 1:
                cadastro.Inserir_Dados()
                print("\n\033[1mCADASTRO FEITO COM SUCESSO, APROVEITE A NOSSA LOJA.\033[m")
                continue
            case 2:
                cadastro.Entrar_na_Conta()
                
                break
            case 3:
                print('\n\033[1mBEM VINDO A NOSSA LOJA!!!\n\033[m')
                convidado1 = False
                break
            case 4:
                print('\033[1;46m\033[1m\nOBRIGADO POR SUA VISITA, VOLTE SEMPRE!!!\033[m')
                exit()
            case __:
                print('\n\033[1;31mOpção inválida!\033[m\n')
    except:
        print('\n\033[1;31mFormato inválido!\n\033[m')

while True:
    dd = input('\n\033[1;0m\033[1;106m PEDRINHO ELETRÔNICOS \033[m \n\n1.Departamentos \n2.Carrinho de compras \n3.Sair \n\n\033[;1mDIGITE A OPÇÃO DESEJADA:\033[m\n')
    match int(dd):
        case 1:
            pass
        case 2:
            if convidado1 == True:
                carrinho_sair = True
                contador = 0
                total = 0
                cursor.execute(f'SELECT * FROM carrinho WHERE email2 = "{email_global[0]}"')
                for linha in cursor.fetchall():
                    n_id7, emmail7, jogo7, valors7 = linha
                    print(f'\n\033[1m{n_id7}-\033[m {jogo7}, R${valors7}')
                    total += linha[3]
                    contador += 1
                if contador == 0:
                    print('\n\033[0;32mSeu carrinho está vazio!!\n\033[m\n')
                    carrinho_sair = False
                    continue
                if carrinho_sair == True:
                    carr = Carrinho()
                    carr.Carrinho_compras()

                    def progresso(a):
                        print("\r\033[1m\nCarregando: [{0:50s}] {1:.1f}%".format('#' * int(a * 50), a * 100),end='')
                    def test():
                        for n in range(101):
                            progresso(n/100)
                            time.sleep(0.01)
                    test()
                    print('\n\n\033[0;32m\033[1mOBRIGADO PELA COMPRA!!!\n\033[m\033[m\033[m')
                    data = str(date.today().day).zfill(2), str(date.today().month).zfill(2), date.today().year
                    x_data = ''.join(str(v) for v in data)
                    data_compra = '{}/{}/{}'.format(x_data[:2], x_data[2:4], x_data[4:8])

                    cursor.execute(f'SELECT * FROM carrinho WHERE email2 = "{email_global[0]}"')
                    for linha in cursor.fetchall():
                        n_id8, emmail8, produto8, valors8 = linha
                    cursor.execute(f'INSERT INTO compras_realizadas (produto7, valor, data_compra, email6) VALUES ("{produto8}", "{valors8}", "{data_compra}", "{email_global[0]}")')
                    conexao.commit()
                    cursor.execute(f'DELETE FROM carrinho WHERE email2 = "{email_global[0]}"')
                    conexao.commit()
                    continue

            elif convidado1 == False:
                print('\n\033[1mPara prosseguir, crie uma conta!\033[m')
                cdd = input('1.Criar conta \n2.Voltar \n\033[;1mDIGITE A OPÇÃO DESEJADA:\033[m\n')
                match int(cdd):
                    case 1:
                        cadastro.Inserir_Dados()
                        print("\nCADASTRO FEITO COM SUCESSO, APROVEITE A NOSSA LOJA.")
                        continue
                    case 2:
                        continue
                    case __:
                        print('\n\033[1;31mOpção inválida!\033[m\n')
        case 3:
            print('\033[1;46m\033[1m\nOBRIGADO POR SUA VISITA, VOLTE SEMPRE!!!\033[m')
            exit()
        case __:
            print('\n\033[1;31mOpção inválida!\033[m\n')

    while True:
        cc = input('\n\033[1;31mCATEGORIAS DE PRODUTOS \033[m \n1.Eletrônicos \n2.Periféricos \n3.Jogos \n4.Sair \n\n\033[;1mDIGITE O NÚMERO DO DEPARTAMENTO DESEJADO:\033[m\n')
        categorias = Categorias()
        match int(cc):
            case 1:
                categorias.Eletronicos()
                cc = "eletronicos"
            case 2:
                categorias.Perifericos()
                cc = 'perifericos'
            case 3:
                categorias.Jogos()
                cc = 'jogos'
            case 4:
                print('\033[1;46m\033[1m\nOBRIGADO POR SUA VISITA, VOLTE SEMPRE!!!\033[m')
                exit()
            case __:
                print('\n\033[1;31mOpção inválida!\033[m\n')

        pg = input('\n1.Selecione produto \n2.Ir a Carrinho de compras \n3.Início \n4.Sair \n\n\033[;1mDIGITE A OPÇÃO DESEJADA:\033[m\n')
        match int(pg):
            case 1:
                if convidado1 == True:
                    pp = Produtos()
                    pp.Inserir_no_Carrinho()
                    break
                elif convidado1 == False:
                    print('\n\033[1mPara prosseguir, crie uma conta!\033[m')
                    cdd = int(input('1.Criar conta \n2.Voltar \n\033[;1mDIGITE A OPÇÃO DESEJADA:\033[m\n'))
                    match cdd:
                        case 1:
                            cadastro.Inserir_Dados()
                            print("\nCADASTRO FEITO COM SUCESSO, APROVEITE A NOSSA LOJA.")
                            break
                        case 2:
                            break
                        case __:
                            print('\n\033[1;31mOpção inválida!\033[m\n')
            case 2:
                if convidado1 == True:
                    carrinho_sair = True
                    contador = 0
                    total = 0
                    cursor.execute(f'SELECT * FROM carrinho WHERE email2 = "{email_global[0]}"')
                    for linha in cursor.fetchall():
                        n_id7, emmail7, jogo7, valors7 = linha
                        print(f'\n\033[1m{n_id7}-\033[m {jogo7}, R${valors7}')
                        total += linha[3]
                        contador += 1
                    if contador == 0:
                        print('\n\033[1m\nSeu carrinho está vazio!!\n\033[m')
                        carrinho_sair = False
                        continue
                    if carrinho_sair == True:
                        carr = Carrinho()
                        carr.Carrinho_compras()

                        def progress(a):
                            print("\r\033[1m\nCarregando: [{0:50s}] {1:.1f}%".format('#' * int(a * 50), a * 100),end='')
                        def teste():
                            for n in range(101):
                                progress(n/100)
                                time.sleep(0.01)
                        teste()
                        print('\n\n\033[0;32m\033[1mOBRIGADO PELA COMPRA!!!\n\033[m\033[m\033[m')

                        data = str(date.today().day).zfill(2), str(date.today().month).zfill(2), date.today().year
                        x_data = ''.join(str(v) for v in data)
                        data_compra = '{}/{}/{}'.format(x_data[:2], x_data[2:4], x_data[4:8])

                        cursor.execute(f'SELECT * FROM carrinho WHERE email2 = "{email_global[0]}"')
                        for linha in cursor.fetchall():
                            n_id8, emmail8, produto8, valors8 = linha
                        cursor.execute(f'INSERT INTO compras_realizadas (produto7, valor, data_compra, email6) VALUES ("{produto8}", "{valors8}", "{data_compra}", "{email_global[0]}")')
                        conexao.commit()
                        cursor.execute(f'DELETE FROM carrinho WHERE email2 = "{email_global[0]}"')
                        conexao.commit()
                        break
                elif convidado1 == False:
                    print('\n\033[1mPara prosseguir, crie uma conta!\033[m')
                    cdd = input('1.Criar conta \n2.Voltar \n\033[;1mDIGITE A OPÇÃO DESEJADA:\033[m\n')
                    match int(cdd):
                        case 1:
                            cadastro.Inserir_Dados()
                            print("\nCADASTRO FEITO COM SUCESSO, APROVEITE A NOSSA LOJA.")
                            break
                        case 2:
                            break
                        case __:
                            print('\n\033[1;31mOpção inválida!\n\033[m')
            case 3:
                break
            case 4:
                print('\033[1;46m\033[1m\nOBRIGADO POR SUA VISITA, VOLTE SEMPRE!!!\033[m')
                exit()
            case __:
                print('\n\033[1;31mOpção inválida!\n\033[m')
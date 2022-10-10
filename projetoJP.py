from Val_Cartao import Cartao
import pycep_correios
import sqlite3
import time


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
                elif self.dados == 'n':
                    print('\n\033[1;91mPor favor, digite seus dados novamente.\033[m\n')
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
                cursor.execute(f'INSERT INTO compras_realizadas (email6) VALUES ("{email}")')
                cursor.execute('SELECT * FROM compras_realizadas')
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

class Produtos:
    def __init__(self) -> None:
        pass
    def Prodd(self):
        t = True
        selecionar = int(input('Digite o número do produto: \n'))                
        cursor.execute(f'SELECT * FROM {cc} WHERE id = {selecionar}')
        for linha in cursor.fetchall():
            num_id, produto, valor = linha
            print(f'\n\033[;1m{num_id}-\033[m {produto} \nR${valor}\n')
        esc = int(input('1.Adicionar ao carrinho \n2.Adicionar à Lista de Desejos \n3.Voltar \n\nEscolha a opção desejada: '))
        while t == True:
            email_test = input('Para continuar, digite seu email: ')
            cursor.execute('SELECT * FROM cadastro')
            for linha in cursor.fetchall():
                if linha[4] == email_test:
                    t = False
                    break
            if t == True:
                print('Você digitou o email errado, digite novamente.')
        match esc:
            case 1:
                cursor.execute('SELECT * FROM carrinho')
                cursor.execute(f'INSERT INTO carrinho (email2, produto2, valor2) VALUES ("{email_test}", "{produto}", "{valor}"')
                conexao.commit()
                print('Adicionado ao carrinho!!')
            case 2:
                cursor.execute(f'INSERT INTO favoritos (email3, produto3, valor3) VALUES ("{email_test}", "{produto}", "{valor}"')
                conexao.commit()
                print('Adicionado à Lista de Desejos!!')
            case 3:
                pass

class Carrinho(Produtos):
    def __init__(self) -> None:
        pass
    def Carrinho_compras(self):
        self.email_test = input('\nPara continuar, digite seu email: ')
        self.total = 0
        m = True
        while m == True:
                cursor.execute('SELECT * FROM carrinho')
                for linha in cursor.fetchall():
                    if linha[1] == self.email_test:
                        m = False                        
                        break
                if m == True:
                    print('Você digitou o email errado, digite novamente.')
        cursor.execute(f'SELECT * FROM carrinho WHERE email = "{self.email_test}"')
        for linha in cursor.fetchall():
            print('\n',linha)
            self.total += linha[3]
        options = int(input(f'\n\033[;1mTOTAL: {float(self.total)}\033[m \n1.Comprar \n2.Remover do carrinho \n3.Aumentar/diminuir quantidade de produto(s) \n4.Voltar \n\nDigite a opção desejada: '))
        tttt = True
        while tttt == True:
            cursor.execute('SELECT * FROM cadastro')
            for linha in cursor.fetchall():
                if self.email_test == linha:
                    tttt = False
                    break
            if tttt == True:
                print('\nVocê digitou o email errado, digite novamente.\n')
        match options:
            case 1:
                pagg = Pagamentos()
                pagg.Formas_Pag()
            case 2:
                ttt = True
                num_id = int(input('\nDigite o id do produto que deseja excluir: '))
                cursor.execute(f'SELECT * FROM carrinho WHERE email = "{self.email_test}"')
                for linha in cursor.fetchall():
                    if linha[0] == num_id:
                        ttt = False
                        break
                if ttt == True:
                    print('\nVocê não tem este produto no seu carrinho!!\n')
                    carr.Carrinho_compras()
                    
                cursor.execute('DELETE FROM carrinho WHERE id = ?, email = ?', (num_id, self.email_test))
                conexao.commit()
                print('Produto removido!!')
            case 3:
                pass
            case 4:
                pass

class Pagamentos(Carrinho):
    def __init__(self) -> None:
        super().__init__()
    def Formas_Pag(self):
        aaa = True
        bbb = True
        m = True
        contador = 0
        cursor.execute('SELECT * FROM cartao_de_credito')
        for linha in cursor.fetchall():
            if linha[5] == self.email_test:
                utilizar_cartão = ('Você ja tem cartão de crédito salvo, deseja utilizá-lo? ("s" ou "n"): ').lower()
                if utilizar_cartão == "s":
                    bbb = False
                    cursor.execute(f'SELECT * FROM cartao_de_credito WHERE email = "{self.email_test}"')
                    for linha in cursor.fetchall():
                        num_id2, nome, numero_do_cartao, validade_cartao, cvv = linha
                        print(f'\n{num_id2}. {nome}, {numero_do_cartao}, {validade_cartao}\n')
                        contador += 1
                    if contador >= 2:
                        while True:
                            cartao_salvo = int(input(f'Escolha o cartão que deseja utilizar (1 ao {contador}): '))
                            if cartao_salvo > contador or cartao_salvo < 1:
                                print('Opção inválida, por favor digite corretamente.')
                                continue
                            break
                        cursor.execute(f'SELECT * FROM cartao_de_credito WHERE email = "{self.email_test}", id = {contador}')
                        for linha in cursor.fetchall():
                            num_id2, nome, numero_do_cartao, validade_cartao, cvv = linha
                            print(f'{num_id2}. {nome}, {numero_do_cartao}, {validade_cartao}')
                    contador = 0
                    while True:
                        confirm_cvv = int(input('Digite o cvv do cartão para continuar: '))
                        if confirm_cvv == cvv:
                            break
                        contador += 1
                        if contador == 3:
                            print('Limite de tentativas excedidos, tente novamente mais tarde!')
                            carr.Carrinho_compras()
                            break
                        if confirm_cvv != cvv:
                            print('Código cvv incorreto!!')
                            continue
                elif utilizar_cartão == "n":
                    pass
                else:
                    print('Opção inválida!')
                    carr.Carrinho_compras()

        cursor.execute('SELECT * FROM endereço')
        for linha in cursor.fetchall():
            if linha[8] == self.email_test:
                contador = 0
                utilizar_endereco = ('Você ja tem esse endereço salvo, deseja utilizá-lo? ("s" ou "n"): ').lower()
                if utilizar_endereco == "s":
                    aaa = False
                    cursor.execute(f'SELECT * FROM endereço WHERE email = "{self.email_test}"')
                    for linha in cursor.fetchall():
                        num_id3, cep, rua, bairro, cidade, uf, numero, complemento = linha
                        print(f'\n\033[;1m{num_id3}:\033[m \n{cep} \n{rua}, {numero} \n{complemento} \n{bairro} \n{cidade} \n{uf} \n')
                        contador += 1
                    if contador >= 2:
                        while True:
                            endereco_salvo = int(input(f'Escolha o endereço que deseja utilizar (1 ao {contador}): '))
                            if endereco_salvo > contador or endereco_salvo < 1:
                                print('\nOpção inválida, por favor digite corretamente.\n')
                                continue
                            break
                        cursor.execute(f'SELECT * FROM endereço WHERE email = "{self.email_test}", id = {contador}')
                        for linha in cursor.fetchall():
                            num_id3, cep, rua, bairro, cidade, uf, numero, complemento = linha
                            print(f'\n{cep} \n{rua}, {numero} \n{complemento} \n{bairro} \n{cidade} \n{uf} \n')
                    self.cep = cep
                    self.rua = rua
                    self.bairro = bairro
                    self.cidade = cidade
                    self.uf = uf
                    self.numero = numero
                    self.complemento = complemento
                elif utilizar_endereco == "n":
                    pass
                else:
                    print('Opção inválida, seu endereço não será salvo!!')
                    carr.Carrinho_compras()

        while aaa == True:
            endereco = pycep_correios.get_address_from_cep(input('\n\033[;1mENDEREÇO DE ENTREGA:\033[m \nDigite seu cep: '))
            self.numero = input('Digite o número da casa: ')
            self.complemento = input('Digite o complemento (casa, apartamento ou comercial): ').capitalize()
            if not self.numero or not self.complemento:
                print('Todos os campos são obrigatórios.')
                continue
            self.rua = print(endereco['\033[;1mlogradouro'].capitalize())
            self.bairro = print(endereco['bairro'].capitalize())
            self.cidade = print(endereco['cidade'].capitalize())
            self.uf = print(endereco['uf'].upper())
            self.cep = print(endereco['cep'])
            print(f'{self.numero} \n{self.complemento}\033[m'.capitalize())
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
            cursor.execute(f'INSERT INTO endereço (cep, rua, bairro, cidade, uf, numero, complemento, email4) VALUES ("{self.cep}", "{self.rua}", "{self.bairro}", "{self.cidade}", "{self.uf}", "{self.numero}", "{self.complemento}", "{self.email_test}")')
            cursor.execute('SELECT * FROM endereço')
            conexao.commit()
            break

        while bbb == True:
            self.nome2 = str(input('\n\033[;1mNome do titular do cartão:\033[m \nNome completo: ')).upper()
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
            self.hh = int(input('Os dados acima estão corretos? ("s" ou "n"): ').lower())
            if self.hh == "n":
                print('Ok, digite novamente seus dados!')
                continue
            elif self.hh == "s":
                break
            else:
                print('Opção inválida, refaça novamente seus dados!')
                continue

        while True:
            self.parcelas = int(input('Você pode parcelar em até 8x sem juros ou em até 12x com juros de 3,5% no cartão. Digite de 1 à 12 de acordo com o número de parcelas desejadas: '))
            if self.parcelas >= 1 and self.parcelas <= 8:
                calculo = self.total / self.parcelas
                print(f'\nParcelas: {self.parcelas}x de {calculo} \nTotal: {self.total}\n')
                break
            elif self.parcelas >= 9 and self.parcelas <= 12:
                calculo = self.total / self.parcelas
                calculo_juros = calculo + (calculo*(3,5/100))
                novo_total = calculo_juros * self.parcelas
                print(f'\nParcelas: {self.parcelas}x de {calculo_juros} \nTotal: {novo_total}\n')
            else:
                print('Opção inválida, você só pode digitar de 1 à 12!')
                continue

        salvar_cartao = input('Você deseja salvar seu cartão para compras futuras? ("s" ou "n"): ').lower()
        m = True
        if salvar_cartao == "s":
            m = False
        elif salvar_cartao == "n":
            pass
        else:
            print('Opção inválida, seu cartão não será salvo!!')

        if m == False:
            cursor.execute(f'INSERT INTO endereço (nome2, num_cartao, validade, cvv, email5) VALUES ("{self.nome2}", "{self.num_cartao}", "{self.validade}", "{self.cvv}", "{self.email_test}")')
            cursor.execute('SELECT * FROM cartao_de_credito')
            conexao.commit()
            print('\nCartão salvo !!\n')

class Favoritos(Carrinho, Produtos):
    def __init__(self) -> None:
        super().__init__()
    def Lista_desejos(self):
        if self.email_test == None:
            self.email_test = input('\nPara continuar, digite seu email: ')
        m = True
        while m == True:
                cursor.execute('SELECT * FROM favoritos')
                for linha in cursor.fetchall():
                    if linha[1] == self.email_test:
                        m = False
                        break
                if m == True:
                    print('Você digitou o email errado, digite novamente.')
        cursor.execute(f'SELECT * FROM favoritos WHERE email = "{self.email_test}"')
        for linha in cursor.fetchall():
            num_id, produto, valor = linha
            print(f'{num_id}.{produto} R${valor}')
        esc2 = int(input('1.Adicionar ao carrinho \n2.Remover da Lista de Desejos \n3.Voltar \n\nEscolha a opção desejada: '))
        match esc2:
                case 1:
                    cursor.execute(f'INSERT INTO carrinho (id, email2, produto2, valor2) VALUES ("{num_id}", "{email_test}", "{produto}", "{valor}"')
                    conexao.commit()
                    print('Adicionado ao carrinho!!')
                case 2:
                    ttt = True
                    num_id = int(input('\nDigite o id do produto que deseja excluir: '))
                    cursor.execute(f'SELECT * FROM favoritos WHERE email = "{self.email_test}"')
                    for linha in cursor.fetchall():
                        if linha[0] == num_id:
                            ttt = False
                            break
                    if ttt == True:
                        print('\nVocê não tem este produto na sua lista de desejos!!\n')
                        favoritos.Lista_desejos()
                        
                    cursor.execute('DELETE FROM favoritos WHERE id = ?, email = ?', (num_id, self.email_test))
                    conexao.commit()
                    print('Produto removido!!')
                case 3:
                    pass

print("\033[1;0m\033[1;106m Olá, Bem vindo à PEDRINHO ELETRONICOS! \033[m \033[m\n\n")
print("\033[;1mENTRE E APROVEITE A VARIEDADES DE PRODUTOS\033[m")
cad = int(input('1.Cadastrar \n2.Entrar na conta \n3.Entrar como convidado \n4.Sair \n\033[;1mDIGITE A OPÇÃO DESEJADA:\033[m\n'))
cadastro = Cadastro()
convidado1 = True
match cad:
    case 1:
        cadastro.Inserir_Dados()
        print("\nCADASTRO FEITO COM SUCESSO, APROVEITE A NOSSA LOJA.")
    case 2:
        cadastro.Entrar_na_Conta()
    case 3:
        print('Bem vindo a nossa loja!!!')
        convidado1 = False
    case 4:
        print('\033[1;46m\033[1m\nOBRIGADO POR SUA VISITA, VOLTE SEMPRE!!!\033[m')
        exit()

while True:
    dd = int(input('\n\033[1;0m\033[1;106m PEDRINHO ELETRÔNICOS \033[m \033[m \n1.Departamentos \n2.Carrinho de compras \n3.Lista de desejos \n4.Sair \n\nDigite a opção desejada: \n'))
    match dd:
        case 1:
            pass
        case 2:
            if convidado1 == True:
                carr = Carrinho()
                carr.Carrinho_compras()

                def progresso(a):
                    print("\rProgress: [{0:50s}] {1:.1f}%".format('#' * int(a * 50), a * 100),end='')
                def test():
                    for n in range(101):
                        progresso(n/100)
                        time.sleep(0.01)
                test()
                print('\n\033[0;32m\033[1mOBRIGADO PELA COMPRA!!!\n\033[m\033[m')

            elif convidado1 == False:
                print('\n\033[1mPara prosseguir, crie uma conta!\033[m')
                cdd = int(input('1.Criar conta \n2.Voltar \n\033[1mDigite a opção desejada: \033[m'))
                match cdd:
                    case 1:
                        cadastro.Inserir_Dados()
                        print("\nCADASTRO FEITO COM SUCESSO, APROVEITE A NOSSA LOJA.")
                        continue
                    case 2:
                        continue
        case 3:
            if convidado1 == True:
                favoritos = Favoritos()
                favoritos.Lista_desejos()

                continue
            elif convidado1 == False:
                print('\n\033[1mPara prosseguir, crie uma conta!\033[m')
                cdd = int(input('1.Criar conta \n2.Voltar \n\033[1mDigite a opção desejada: \033[m'))
                match cdd:
                    case 1:
                        cadastro.Inserir_Dados()
                        print("\nCADASTRO FEITO COM SUCESSO, APROVEITE A NOSSA LOJA.")
                        continue
                    case 2:
                        continue
        case 4:
            print('\033[1;46m\033[1m\nOBRIGADO POR SUA VISITA, VOLTE SEMPRE!!!\033[m')
            exit()

    while True:
        cc = int(input('\n\033[1;31mCATEGORIAS DE PRODUTOS \033[m \n1.Eletrônicos \n2.Periféricos \n3.Jogos \n4.Sair \n\nDigite o número do departamento desejado: \n'))
        categorias = Categorias()
        match cc:
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

        pg = int(input('1.Selecione produto \n2.Ir a Carrinho de compras \n3.Lista de desejos \n4.Início \n5.Sair \n\033[;1mDIGITE A OPÇÃO DESEJADA:\033[m\n'))
        match pg:
            case 1:
                if convidado1 == True:
                    pp = Produtos()
                    pp.Prodd()
                elif convidado1 == False:
                    print('\n\033[1mPara prosseguir, crie uma conta!\033[m')
                    cdd = int(input('1.Criar conta \n2.Voltar \n\033[1mDigite a opção desejada: \033[m'))
                    match cdd:
                        case 1:
                            cadastro.Inserir_Dados()
                            print("\nCADASTRO FEITO COM SUCESSO, APROVEITE A NOSSA LOJA.")
                            break
                        case 2:
                            break
            case 2:
                if convidado1 == True:
                    carr = Carrinho()
                    carr.Carrinho_compras()

                    def progresso(a):
                        print("\rProgress: [{0:50s}] {1:.1f}%".format('#' * int(a * 50), a * 100),end='')
                    def test():
                        for n in range(101):
                            progresso(n/100)
                            time.sleep(0.01)
                    test()
                    print('\n\033[0;32m\033[1mOBRIGADO PELA COMPRA!!!\n\033[m\033[m')
                elif convidado1 == False:
                    print('\n\033[1mPara prosseguir, crie uma conta!\033[m')
                    cdd = int(input('1.Criar conta \n2.Voltar \n\033[1mDigite a opção desejada: \033[m'))
                    match cdd:
                        case 1:
                            cadastro.Inserir_Dados()
                            print("\nCADASTRO FEITO COM SUCESSO, APROVEITE A NOSSA LOJA.")
                            break
                        case 2:
                            break
            case 3:
                if convidado1 == True:
                    favoritos = Favoritos()
                    favoritos.Lista_desejos()
                elif convidado1 == False:
                    print('\n\033[1mPara prosseguir, crie uma conta!\033[m')
                    cdd = int(input('1.Criar conta \n2.Voltar \n\033[1mDigite a opção desejada: \033[m'))
                    match cdd:
                        case 1:
                            cadastro.Inserir_Dados()
                            print("\nCADASTRO FEITO COM SUCESSO, APROVEITE A NOSSA LOJA.")
                            break
                        case 2:
                            break
            case 4:
                break
            case 5:
                print('\033[1;46m\033[1m\nOBRIGADO POR SUA VISITA, VOLTE SEMPRE!!!\033[m')
                exit()
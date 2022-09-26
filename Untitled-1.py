
import sqlite3
conexao = sqlite3.connect("loja1.db")
cursor = conexao.cursor()

class Login():
    def __init__(self) -> None:
        pass
    def inserirCadastramento(self):
        nome = str(input("Digite seu nome: "))
        idade = int(input("Digite sua idade: "))
        email = input("Digite o seu email: ")
        senha = input("Digite o sua senha: ")
        cursor.execute("INSERT INTO Login (nome,idade,email,senha) VALUES (?,?,?,?)",(nome,idade,email,senha))
        conexao.commit()
    def entrarLogin(self):
        email = input("Digite o seu email: ")
        senha = input("Digite o sua senha: ")
        cursor.execute("INSERT INTO Login (email,senha) VALUES (?,?)",(email,senha))
        conexao.commit()


print("\033[1;0m \033[1;106mOLÁ SEJA BEM VINDO A PEDRINHO ELETRONICOS!\033[m \033[m")
print("")
print("VOCE DESEJA REALIZAR SEU CADASTRO OU ENTRAR EM UMA CONTA JÁ CRIADA?")
cad = int(input("""1-CADASTRO
2-LOGIN
DIGITE SUA OPÇÃO: """))
print("")
login1 = Login()
match cad:
    case 1:
        login1.inserirCadastramento()
        print("")
        print("CADASTRO FEITO COM SUCESSO, APROVEITE A NOSSA LOJA.")
    case 2:
        login1.entrarLogin()
        print("")
        print("CONTA LOGADA COM SUCESSO, BEM-VINDO A NOSSA LOJA.")
print("")
print("SEJA MUITO BEM-VINDO A NOSSA LOJA E FIQUE A VONTADE!")
print("")
print("\033[1;31mCATEGORIAS DE PRODUTOS \033[m")
cat = int(input("""1-ELETRÔNICOS
2-PERIFERICOS
3-JOGOS
QUAL OPÇÃO VOCÊ DESEJA ACESSAR?: """))
print("")
match cat:
    case 1:
        print("1- IPHONE 11 | VALOR: R$4000")
        print("2- IPHONE 12 PRO | VALOR: R$5690")
        print("3- IPHONE 13 PRO MAX | VALOR: R$7230")
        print("4- MACBOOK | VALOR: R$27000")
        print("5- TV SAMSUNG SMART 55 POLEGADAS | VALOR: R$6790")
        print("6- TV LG SMART 70 POLEGADAS | VALOR: R$9390")
        print("")
        eletronicos = int(input("""QUAL OPÇÃO VOCÊ DESEJA COMPRAR? DIGITE O NUMERO DO ITEM: """))
        print("")
        if eletronicos == 1:
            pagamento = int(input("""QUAL SERÁ A FORMA DE PAGAMENTO?: 
1- CARTÃO DE CRÉDITO PARCELADO ATÉ 10X S/JUROS
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
            if pagamento == 1:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$400 10X MENSAL")
                nomecartao = str(input("NOME DO CARTÃO: "))
                numerocartao = int(input("NUMERO DO CARTÃO: "))
                cvv = int(input("NUMERO CVV: "))
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 2:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$4,000 A VISTA")
                nomecartao = str(input("NOME DO CARTÃO: "))
                numerocartao = int(input("NUMERO DO CARTÃO: "))
                cvv = int(input("NUMERO CVV: "))
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 3:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$4,000 E PARA SER APROVADO LEVA EM TORNO DE 3 A 5 DIAS ÚTEIS!")
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 4:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$4,000 E É APROVADO EM SEGUIDA APÓS O PIX!")
                print("CÓDIGO DO PIX COPIA E COLA: 0ada2d1a05150db6181dfh320da916030ada310hj02")
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
        if eletronicos == 2:              
            pagamento = int(input("""QUAL SERÁ A FORMA DE PAGAMENTO?: 
1- CARTÃO DE CRÉDITO PARCELADO ATÉ 10X S/JUROS
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
            if pagamento == 1:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$569 10X MENSAL")
                nomecartao = str(input("NOME DO CARTÃO: "))
                numerocartao = int(input("NUMERO DO CARTÃO: "))
                cvv = int(input("NUMERO CVV: "))
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 2:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$5,690 A VISTA")
                nomecartao = str(input("NOME DO CARTÃO: "))
                numerocartao = int(input("NUMERO DO CARTÃO: "))
                cvv = int(input("NUMERO CVV: "))
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 3:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$5,690 E PARA SER APROVADO LEVA EM TORNO DE 3 A 5 DIAS ÚTEIS!")
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 4:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$5,690 E É APROVADO EM SEGUIDA APÓS O PIX!")
                print("CÓDIGO DO PIX COPIA E COLA: 0ada2d1a05150db6181dfh320da916030ada310hj02")
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
        if eletronicos == 3:              
            pagamento = int(input("""QUAL SERÁ A FORMA DE PAGAMENTO?: 
1- CARTÃO DE CRÉDITO PARCELADO ATÉ 10X S/JUROS
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
            if pagamento == 1:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$723 10X MENSAL")
                nomecartao = str(input("NOME DO CARTÃO: "))
                numerocartao = int(input("NUMERO DO CARTÃO: "))
                cvv = int(input("NUMERO CVV: "))
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 2:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$7,230 A VISTA")
                nomecartao = str(input("NOME DO CARTÃO: "))
                numerocartao = int(input("NUMERO DO CARTÃO: "))
                cvv = int(input("NUMERO CVV: "))
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 3:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$7,230 E PARA SER APROVADO LEVA EM TORNO DE 3 A 5 DIAS ÚTEIS!")
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 4:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$7,230 E É APROVADO EM SEGUIDA APÓS O PIX!")
                print("CÓDIGO DO PIX COPIA E COLA: 0ada2d1a05150db6181dfh320da916030ada310hj02")
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
        if eletronicos == 4:              
            pagamento = int(input("""QUAL SERÁ A FORMA DE PAGAMENTO?: 
1- CARTÃO DE CRÉDITO PARCELADO ATÉ 10X S/JUROS
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
            if pagamento == 1:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$2,700 10X MENSAL")
                nomecartao = str(input("NOME DO CARTÃO: "))
                numerocartao = int(input("NUMERO DO CARTÃO: "))
                cvv = int(input("NUMERO CVV: "))
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 2:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$27,000 A VISTA")
                nomecartao = str(input("NOME DO CARTÃO: "))
                numerocartao = int(input("NUMERO DO CARTÃO: "))
                cvv = int(input("NUMERO CVV: "))
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 3:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$27,000 E PARA SER APROVADO LEVA EM TORNO DE 3 A 5 DIAS ÚTEIS!")
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 4:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$27,000 E É APROVADO EM SEGUIDA APÓS O PIX!")
                print("CÓDIGO DO PIX COPIA E COLA: 0ada2d1a05150db6181dfh320da916030ada310hj02")
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
        if eletronicos == 5:              
            pagamento = int(input("""QUAL SERÁ A FORMA DE PAGAMENTO?: 
1- CARTÃO DE CRÉDITO PARCELADO ATÉ 10X S/JUROS
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
            if pagamento == 1:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$679 10X MENSAL")
                nomecartao = str(input("NOME DO CARTÃO: "))
                numerocartao = int(input("NUMERO DO CARTÃO: "))
                cvv = int(input("NUMERO CVV: "))
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 2:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$6,790 A VISTA")
                nomecartao = str(input("NOME DO CARTÃO: "))
                numerocartao = int(input("NUMERO DO CARTÃO: "))
                cvv = int(input("NUMERO CVV: "))
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 3:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$6,790 E PARA SER APROVADO LEVA EM TORNO DE 3 A 5 DIAS ÚTEIS!")
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 4:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$6,790 E É APROVADO EM SEGUIDA APÓS O PIX!")
                print("CÓDIGO DO PIX COPIA E COLA: 0ada2d1a05150db6181dfh320da916030ada310hj02")
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
        if eletronicos == 6:              
            pagamento = int(input("""QUAL SERÁ A FORMA DE PAGAMENTO?: 
1- CARTÃO DE CRÉDITO PARCELADO ATÉ 10X S/JUROS
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
            if pagamento == 1:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$939 10X MENSAL")
                nomecartao = str(input("NOME DO CARTÃO: "))
                numerocartao = int(input("NUMERO DO CARTÃO: "))
                cvv = int(input("NUMERO CVV: "))
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 2:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$9,390 A VISTA")
                nomecartao = str(input("NOME DO CARTÃO: "))
                numerocartao = int(input("NUMERO DO CARTÃO: "))
                cvv = int(input("NUMERO CVV: "))
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 3:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$9,390 E PARA SER APROVADO LEVA EM TORNO DE 3 A 5 DIAS ÚTEIS!")
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 4:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$9,390 E É APROVADO EM SEGUIDA APÓS O PIX!")
                print("CÓDIGO DO PIX COPIA E COLA: 0ada2d1a05150db6181dfh320da916030ada310hj02")
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
    case 2:           
        print("1- TECLADO GAMER HYPERX | VALOR: R$980")
        print("2- MOUSE SCORPION GAMER | VALOR: R$390")
        print("3- HEADSET FALLEN | VALOR: R$1030")
        print("4- CADEIRA GAMER THUNDERX3 TGC12, BLACK | VALOR: R$1790")
        print("5- MOUSEPAD 60CM | VALOR: R$300")
        print("6- MONITOR 144HZ ULTRALED 2K|4K | VALOR: R$3299")
        print("")
        perifericos = int(input("""QUAL OPÇÃO VOCÊ DESEJA COMPRAR? DIGITE O NUMERO DO ITEM: """))
        print("")
        if perifericos == 1:
            pagamento = int(input("""QUAL SERÁ A FORMA DE PAGAMENTO?: 
1- CARTÃO DE CRÉDITO PARCELADO ATÉ 10X S/JUROS
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
            if pagamento == 1:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$98 10X MENSAL")
                nomecartao = str(input("NOME DO CARTÃO: "))
                numerocartao = int(input("NUMERO DO CARTÃO: "))
                cvv = int(input("NUMERO CVV: "))
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 2:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$980 A VISTA")
                nomecartao = str(input("NOME DO CARTÃO: "))
                numerocartao = int(input("NUMERO DO CARTÃO: "))
                cvv = int(input("NUMERO CVV: "))
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 3:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$980 E PARA SER APROVADO LEVA EM TORNO DE 3 A 5 DIAS ÚTEIS!")
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 4:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$980 E É APROVADO EM SEGUIDA APÓS O PIX!")
                print("CÓDIGO DO PIX COPIA E COLA: 0ada2d1a05150db6181dfh320da916030ada310hj02")
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
        if perifericos == 2:              
            pagamento = int(input("""QUAL SERÁ A FORMA DE PAGAMENTO?: 
1- CARTÃO DE CRÉDITO PARCELADO ATÉ 10X S/JUROS
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
            if pagamento == 1:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$39 10X MENSAL")
                nomecartao = str(input("NOME DO CARTÃO: "))
                numerocartao = int(input("NUMERO DO CARTÃO: "))
                cvv = int(input("NUMERO CVV: "))
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 2:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$390 A VISTA")
                nomecartao = str(input("NOME DO CARTÃO: "))
                numerocartao = int(input("NUMERO DO CARTÃO: "))
                cvv = int(input("NUMERO CVV: "))
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 3:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$390 E PARA SER APROVADO LEVA EM TORNO DE 3 A 5 DIAS ÚTEIS!")
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 4:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$390 E É APROVADO EM SEGUIDA APÓS O PIX!")
                print("CÓDIGO DO PIX COPIA E COLA: 0ada2d1a05150db6181dfh320da916030ada310hj02")
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
        if perifericos == 3:              
            pagamento = int(input("""QUAL SERÁ A FORMA DE PAGAMENTO?: 
1- CARTÃO DE CRÉDITO PARCELADO ATÉ 10X S/JUROS
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
            if pagamento == 1:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$103 10X MENSAL")
                nomecartao = str(input("NOME DO CARTÃO: "))
                numerocartao = int(input("NUMERO DO CARTÃO: "))
                cvv = int(input("NUMERO CVV: "))
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 2:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$1030 A VISTA")
                nomecartao = str(input("NOME DO CARTÃO: "))
                numerocartao = int(input("NUMERO DO CARTÃO: "))
                cvv = int(input("NUMERO CVV: "))
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 3:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$1030 E PARA SER APROVADO LEVA EM TORNO DE 3 A 5 DIAS ÚTEIS!")
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 4:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$1030 E É APROVADO EM SEGUIDA APÓS O PIX!")
                print("CÓDIGO DO PIX COPIA E COLA: 0ada2d1a05150db6181dfh320da916030ada310hj02")
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
        if perifericos == 4:             
            pagamento = int(input("""QUAL SERÁ A FORMA DE PAGAMENTO?: 
1- CARTÃO DE CRÉDITO PARCELADO ATÉ 10X S/JUROS
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
            if pagamento == 1:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$179 10X MENSAL")
                nomecartao = str(input("NOME DO CARTÃO: "))
                numerocartao = int(input("NUMERO DO CARTÃO: "))
                cvv = int(input("NUMERO CVV: "))
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 2:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$1790 A VISTA")
                nomecartao = str(input("NOME DO CARTÃO: "))
                numerocartao = int(input("NUMERO DO CARTÃO: "))
                cvv = int(input("NUMERO CVV: "))
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 3:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$1790 E PARA SER APROVADO LEVA EM TORNO DE 3 A 5 DIAS ÚTEIS!")
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 4:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$1790 E É APROVADO EM SEGUIDA APÓS O PIX!")
                print("CÓDIGO DO PIX COPIA E COLA: 0ada2d1a05150db6181dfh320da916030ada310hj02")
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
        if perifericos == 5:              
            pagamento = int(input("""QUAL SERÁ A FORMA DE PAGAMENTO?: 
1- CARTÃO DE CRÉDITO PARCELADO ATÉ 10X S/JUROS
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
            if pagamento == 1:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$30 10X MENSAL")
                nomecartao = str(input("NOME DO CARTÃO: "))
                numerocartao = int(input("NUMERO DO CARTÃO: "))
                cvv = int(input("NUMERO CVV: "))
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 2:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$300 A VISTA")
                nomecartao = str(input("NOME DO CARTÃO: "))
                numerocartao = int(input("NUMERO DO CARTÃO: "))
                cvv = int(input("NUMERO CVV: "))
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 3:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$300 E PARA SER APROVADO LEVA EM TORNO DE 3 A 5 DIAS ÚTEIS!")
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 4:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$300 E É APROVADO EM SEGUIDA APÓS O PIX!")
                print("CÓDIGO DO PIX COPIA E COLA: 0ada2d1a05150db6181dfh320da916030ada310hj02")
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
        if perifericos == 6:              
            pagamento = int(input("""QUAL SERÁ A FORMA DE PAGAMENTO?: 
1- CARTÃO DE CRÉDITO PARCELADO ATÉ 10X S/JUROS
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
            if pagamento == 1:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$329,99 10X MENSAL")
                nomecartao = str(input("NOME DO CARTÃO: "))
                numerocartao = int(input("NUMERO DO CARTÃO: "))
                cvv = int(input("NUMERO CVV: "))
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 2:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$3299 A VISTA")
                nomecartao = str(input("NOME DO CARTÃO: "))
                numerocartao = int(input("NUMERO DO CARTÃO: "))
                cvv = int(input("NUMERO CVV: "))
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 3:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$3299 E PARA SER APROVADO LEVA EM TORNO DE 3 A 5 DIAS ÚTEIS!")
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
            if pagamento == 4:
                cep = int(input("DIGITE SEU CEP: "))
                nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                print("CEP: ",cep)
                print("NOME DO RECEBIDOR: ",nome1)
                print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                print("O VALOR É DE R$3299 E É APROVADO EM SEGUIDA APÓS O PIX!")
                print("CÓDIGO DO PIX COPIA E COLA: 0ada2d1a05150db6181dfh320da916030ada310hj02")
                while True:
                    conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                    if conf == 1:
                        print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                        break
                    elif conf == 2:
                        print("\033[1;35mCOMPRA CANCELADA!\033[m")
                        break
                    else:
                        print(
                            "\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")
cursor.close()
conexao.close()
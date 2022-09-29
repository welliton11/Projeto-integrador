import sys
import sqlite3
conexao = sqlite3.connect("loja1.db")
cursor = conexao.cursor()

class Cadastro():
    def __init__(self) -> None:
        pass
    def Cadastro2(self):
        nome = str(input("Digite seu nome: "))
        idade = int(input("Digite sua idade: "))
        email = input("Digite o seu email: ")
        senha = input("Digite o sua senha: ")
        cursor.execute("INSERT INTO Cadastro (nome,idade,email,senha) VALUES (?,?,?,?)",(nome,idade,email,senha))
        conexao.commit()
class Login():
    def __init__(self) -> None:
        pass
    def Login2(self):
        email = input("Digite o seu email: ")
        senha = input("Digite o sua senha: ")
        cursor.execute("INSERT INTO Login (email,senha) VALUES (?,?)",(email,senha))
        conexao.commit()
print("\033[1;0m \033[1;106mOLÁ SEJA BEM VINDO A WKB ELETRONICOS!\033[m \033[m")
print("")
print("VOCE DESEJA REALIZAR SEU CADASTRO OU ENTRAR EM UMA CONTA JÁ CRIADA?")
cad = int(input("""1-CADASTRO
2-LOGIN
DIGITE SUA OPÇÃO: """))
print("")
login1 = Login()
cadastro = Cadastro()
match cad:
    case 1:
        cadastro.Cadastro2()
        print("")
        print("CADASTRO FEITO COM SUCESSO, APROVEITE A NOSSA LOJA.")
    case 2:
        login1.Login2()
        print("")
        print("CONTA LOGADA COM SUCESSO, BEM-VINDO A NOSSA LOJA.")
print("")
print("SEJA MUITO BEM-VINDO A NOSSA LOJA E FIQUE A VONTADE!")
print("")
print("\033[1;31mCATEGORIAS DE PRODUTOS \033[m")
while True:
    cat = int(input("""1-ELETRÔNICOS
2-PERIFERICOS
3-JOGOS
QUAL OPÇÃO VOCÊ DESEJA ACESSAR?: """))
    if cat == 1 or cat == 2 or cat == 3:
        print()
    else:
        print("\033[1;31mTENTE NOVAMENTE OPÇÃO INVÁLIDA\033[m")
        print()
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
            if eletronicos == 1 or eletronicos == 2 or eletronicos == 3 or eletronicos == 4 or eletronicos == 5 or eletronicos == 6:
                print()
            else:
                print("\033[1;31mTENTE NOVAMENTE OPÇÃO INVALIDA\033[m")
            if eletronicos == 1:
                pagamento = int(input("""QUAL SERÁ A FORMA DE PAGAMENTO?: 
1- CARTÃO DE CRÉDITO PARCELADO
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
                if pagamento == 1 or pagamento == 2 or pagamento == 3 or pagamento == 4:
                    print()
                else:
                    print("\033[1;31mTENTE NOVAMENTE OPÇÃO INVALIDA\033[m")
                if pagamento == 1:
                    cep = int(input("DIGITE SEU CEP: "))

                    nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                    print("CEP: ",cep)
                    print("NOME DO RECEBIDOR: ",nome1)
                    print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                    while True:
                        vezes = int(input("DIGITE EM QUANTAS VEZES VOCÊ QUER PARCELAR: "))
                        if vezes > 15:
                            print("\033[1;91mNÃO PODEMOS FAZER MAIS QUE 15X\033[m")
                        if vezes < 2:
                            print("\033[1;91mNÃO PODEMOS FAZER EM MENOS QUE 2X\033[m")
                        if vezes >= 2 and vezes <= 15:
                            print("O VALOR FICARÁ DE R$",4000 // vezes,"MENSAL")
                        break
                    nomecartao = str(input("NOME DO CARTÃO: "))
                    while True:
                        total=0
                        s = input('DIGITE O NUMERO DO CARTÃO (SEM SINAIS "-->"): ')
                        if (len(s) != 16):
                            print ("NUMERO ERRADO. TENTE NOVAMENTE")
                            exit()
                        for i in range(0,16,2):
                            acum=int(s[i])*2
                        if (acum > 9):
                            acum=acum-9
                            total=total+acum
                        for i in range(1,17,2):
                            total=total+int(s[i])
                        if ((total%10) != 0 or total > 150):
                            print ("CARTÃO INVALIDO")
                            continue
                        print ("CARTÃO VALIDO: %s" % s)
                        break
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
1- CARTÃO DE CRÉDITO PARCELADO
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
                if pagamento == 1 or pagamento == 2 or pagamento == 3 or pagamento == 4:
                    print()
                else:
                    print("\033[1;31mTENTE NOVAMENTE OPÇÃO INVALIDA\033[m")
                if pagamento == 1:
                    cep = int(input("DIGITE SEU CEP: "))

                    nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                    print("CEP: ",cep)
                    print("NOME DO RECEBIDOR: ",nome1)
                    print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                    while True:
                        vezes = int(input("DIGITE EM QUANTAS VEZES VOCÊ QUER PARCELAR: "))
                        if vezes > 15:
                            print("\033[1;91mNÃO PODEMOS FAZER MAIS QUE 15X\033[m")
                        if vezes < 2:
                            print("\033[1;91mNÃO PODEMOS FAZER EM MENOS QUE 2X\033[m")
                        if vezes >= 2 and vezes <= 15:
                            print("O VALOR FICARÁ DE R$",5690 // vezes,"MENSAL")
                        break
                    nomecartao = str(input("NOME DO CARTÃO: "))
                    while True:
                        total=0
                        s = input('DIGITE O NUMERO DO CARTÃO (SEM SINAIS "-->"): ')
                        if (len(s) != 16):
                            print ("NUMERO ERRADO. TENTE NOVAMENTE")
                            exit()
                        for i in range(0,16,2):
                            acum=int(s[i])*2
                        if (acum > 9):
                            acum=acum-9
                            total=total+acum
                        for i in range(1,17,2):
                            total=total+int(s[i])
                        if ((total%10) != 0 or total > 150):
                            print ("CARTÃO INVALIDO")
                            continue
                        print ("CARTÃO VALIDO: %s" % s)
                        break
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
1- CARTÃO DE CRÉDITO PARCELADO
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
                if pagamento == 1 or pagamento == 2 or pagamento == 3 or pagamento == 4:
                    print()
                else:
                    print("\033[1;31mTENTE NOVAMENTE OPÇÃO INVALIDA\033[m")
                if pagamento == 1:
                    cep = int(input("DIGITE SEU CEP: "))

                    nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                    print("CEP: ",cep)
                    print("NOME DO RECEBIDOR: ",nome1)
                    print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                    while True:
                        vezes = int(input("DIGITE EM QUANTAS VEZES VOCÊ QUER PARCELAR: "))
                        if vezes > 15:
                            print("\033[1;91mNÃO PODEMOS FAZER MAIS QUE 15X\033[m")
                        if vezes < 2:
                            print("\033[1;91mNÃO PODEMOS FAZER EM MENOS QUE 2X\033[m")
                        if vezes >= 2 and vezes <= 15:
                            print("O VALOR FICARÁ DE R$",7230 // vezes,"MENSAL")
                        break
                    nomecartao = str(input("NOME DO CARTÃO: "))
                    while True:
                        total=0
                        s = input('DIGITE O NUMERO DO CARTÃO (SEM SINAIS "-->"): ')
                        if (len(s) != 16):
                            print ("NUMERO ERRADO. TENTE NOVAMENTE")
                            exit()
                        for i in range(0,16,2):
                            acum=int(s[i])*2
                        if (acum > 9):
                            acum=acum-9
                            total=total+acum
                        for i in range(1,17,2):
                            total=total+int(s[i])
                        if ((total%10) != 0 or total > 150):
                            print ("CARTÃO INVALIDO")
                            continue
                        print ("CARTÃO VALIDO: %s" % s)
                        break
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
1- CARTÃO DE CRÉDITO PARCELADO
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
                if pagamento == 1 or pagamento == 2 or pagamento == 3 or pagamento == 4:
                    print()
                else:
                    print("\033[1;31mTENTE NOVAMENTE OPÇÃO INVALIDA\033[m")
                if pagamento == 1:
                    cep = int(input("DIGITE SEU CEP: "))

                    nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                    print("CEP: ",cep)
                    print("NOME DO RECEBIDOR: ",nome1)
                    print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                    while True:
                        vezes = int(input("DIGITE EM QUANTAS VEZES VOCÊ QUER PARCELAR: "))
                        if vezes > 15:
                            print("\033[1;91mNÃO PODEMOS FAZER MAIS QUE 15X\033[m")
                        if vezes < 2:
                            print("\033[1;91mNÃO PODEMOS FAZER EM MENOS QUE 2X\033[m")
                        if vezes >= 2 and vezes <= 15:
                            print("O VALOR FICARÁ DE R$",27000 // vezes,"MENSAL")
                        break
                    nomecartao = str(input("NOME DO CARTÃO: "))
                    while True:
                        total=0
                        s = input('DIGITE O NUMERO DO CARTÃO (SEM SINAIS "-->"): ')
                        if (len(s) != 16):
                            print ("NUMERO ERRADO. TENTE NOVAMENTE")
                            exit()
                        for i in range(0,16,2):
                            acum=int(s[i])*2
                        if (acum > 9):
                            acum=acum-9
                            total=total+acum
                        for i in range(1,17,2):
                            total=total+int(s[i])
                        if ((total%10) != 0 or total > 150):
                            print ("CARTÃO INVALIDO")
                            continue
                        print ("CARTÃO VALIDO: %s" % s)
                        break
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
1- CARTÃO DE CRÉDITO PARCELADO
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
                if pagamento == 1 or pagamento == 2 or pagamento == 3 or pagamento == 4:
                    print()
                else:
                    print("\033[1;31mTENTE NOVAMENTE OPÇÃO INVALIDA\033[m")
                if pagamento == 1:
                    cep = int(input("DIGITE SEU CEP: "))

                    nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                    print("CEP: ",cep)
                    print("NOME DO RECEBIDOR: ",nome1)
                    print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                    while True:
                        vezes = int(input("DIGITE EM QUANTAS VEZES VOCÊ QUER PARCELAR: "))
                        if vezes > 15:
                            print("\033[1;91mNÃO PODEMOS FAZER MAIS QUE 15X\033[m")
                        if vezes < 2:
                            print("\033[1;91mNÃO PODEMOS FAZER EM MENOS QUE 2X\033[m")
                        if vezes >= 2 and vezes <= 15:
                            print("O VALOR FICARÁ DE R$",6790 // vezes,"MENSAL")
                        break
                    nomecartao = str(input("NOME DO CARTÃO: "))
                    while True:
                        total=0
                        s = input('DIGITE O NUMERO DO CARTÃO (SEM SINAIS "-->"): ')
                        if (len(s) != 16):
                            print ("NUMERO ERRADO. TENTE NOVAMENTE")
                            exit()
                        for i in range(0,16,2):
                            acum=int(s[i])*2
                        if (acum > 9):
                            acum=acum-9
                            total=total+acum
                        for i in range(1,17,2):
                            total=total+int(s[i])
                        if ((total%10) != 0 or total > 150):
                            print ("CARTÃO INVALIDO")
                            continue
                        print ("CARTÃO VALIDO: %s" % s)
                        break
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
1- CARTÃO DE CRÉDITO PARCELADO
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
                if pagamento == 1 or pagamento == 2 or pagamento == 3 or pagamento == 4:
                    print()
                else:
                    print("\033[1;31mTENTE NOVAMENTE OPÇÃO INVALIDA\033[m")
                if pagamento == 1:
                    cep = int(input("DIGITE SEU CEP: "))

                    nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                    print("CEP: ",cep)
                    print("NOME DO RECEBIDOR: ",nome1)
                    print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                    while True:
                        vezes = int(input("DIGITE EM QUANTAS VEZES VOCÊ QUER PARCELAR: "))
                        if vezes > 15:
                            print("\033[1;91mNÃO PODEMOS FAZER MAIS QUE 15X\033[m")
                        if vezes < 2:
                            print("\033[1;91mNÃO PODEMOS FAZER EM MENOS QUE 2X\033[m")
                        if vezes >= 2 and vezes <= 15:
                            print("O VALOR FICARÁ DE R$",9390 // vezes,"MENSAL")
                        break
                    nomecartao = str(input("NOME DO CARTÃO: "))
                    while True:
                        total=0
                        s = input('DIGITE O NUMERO DO CARTÃO (SEM SINAIS "-->"): ')
                        if (len(s) != 16):
                            print ("NUMERO ERRADO. TENTE NOVAMENTE")
                            exit()
                        for i in range(0,16,2):
                            acum=int(s[i])*2
                        if (acum > 9):
                            acum=acum-9
                            total=total+acum
                        for i in range(1,17,2):
                            total=total+int(s[i])
                        if ((total%10) != 0 or total > 150):
                            print ("CARTÃO INVALIDO")
                            continue
                        print ("CARTÃO VALIDO: %s" % s)
                        break
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
            if perifericos == 1 or perifericos == 2 or perifericos == 3 or perifericos == 4 or perifericos == 5 or perifericos == 6:
                print()
            else:
                print("\033[1;31mTENTE NOVAMENTE OPÇÃO INVALIDA\033[m")
            if perifericos == 1:
                pagamento = int(input("""QUAL SERÁ A FORMA DE PAGAMENTO?: 
1- CARTÃO DE CRÉDITO PARCELADO
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
                if pagamento == 1 or pagamento == 2 or pagamento == 3 or pagamento == 4:
                    print()
                else:
                    print("\033[1;31mTENTE NOVAMENTE OPÇÃO INVALIDA\033[m")
                if pagamento == 1:
                    cep = int(input("DIGITE SEU CEP: "))

                    nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                    print("CEP: ",cep)
                    print("NOME DO RECEBIDOR: ",nome1)
                    print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                    while True:
                        vezes = int(input("DIGITE EM QUANTAS VEZES VOCÊ QUER PARCELAR: "))
                        if vezes > 15:
                            print("\033[1;91mNÃO PODEMOS FAZER MAIS QUE 15X\033[m")
                        if vezes < 2:
                            print("\033[1;91mNÃO PODEMOS FAZER EM MENOS QUE 2X\033[m")
                        if vezes >= 2 and vezes <= 15:
                            print("O VALOR FICARÁ DE R$",980 // vezes,"MENSAL")
                        break
                    nomecartao = str(input("NOME DO CARTÃO: "))
                    while True:
                        total=0
                        s = input('DIGITE O NUMERO DO CARTÃO (SEM SINAIS "-->"): ')
                        if (len(s) != 16):
                            print ("NUMERO ERRADO. TENTE NOVAMENTE")
                            exit()
                        for i in range(0,16,2):
                            acum=int(s[i])*2
                        if (acum > 9):
                            acum=acum-9
                            total=total+acum
                        for i in range(1,17,2):
                            total=total+int(s[i])
                        if ((total%10) != 0 or total > 150):
                            print ("CARTÃO INVALIDO")
                            continue
                        print ("CARTÃO VALIDO: %s" % s)
                        break
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
1- CARTÃO DE CRÉDITO PARCELADO
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
                if pagamento == 1 or pagamento == 2 or pagamento == 3 or pagamento == 4:
                    print()
                else:
                    print("\033[1;31mTENTE NOVAMENTE OPÇÃO INVALIDA\033[m")
                if pagamento == 1:
                    cep = int(input("DIGITE SEU CEP: "))

                    nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                    print("CEP: ",cep)
                    print("NOME DO RECEBIDOR: ",nome1)
                    print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                    while True:
                        vezes = int(input("DIGITE EM QUANTAS VEZES VOCÊ QUER PARCELAR: "))
                        if vezes > 15:
                            print("\033[1;91mNÃO PODEMOS FAZER MAIS QUE 15X\033[m")
                        if vezes < 2:
                            print("\033[1;91mNÃO PODEMOS FAZER EM MENOS QUE 2X\033[m")
                        if vezes >= 2 and vezes <= 15:
                            print("O VALOR FICARÁ DE R$",390 // vezes,"MENSAL")
                        break
                    nomecartao = str(input("NOME DO CARTÃO: "))
                    while True:
                        total=0
                        s = input('DIGITE O NUMERO DO CARTÃO (SEM SINAIS "-->"): ')
                        if (len(s) != 16):
                            print ("NUMERO ERRADO. TENTE NOVAMENTE")
                            exit()
                        for i in range(0,16,2):
                            acum=int(s[i])*2
                        if (acum > 9):
                            acum=acum-9
                            total=total+acum
                        for i in range(1,17,2):
                            total=total+int(s[i])
                        if ((total%10) != 0 or total > 150):
                            print ("CARTÃO INVALIDO")
                            continue
                        print ("CARTÃO VALIDO: %s" % s)
                        break
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
1- CARTÃO DE CRÉDITO PARCELADO
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
                if pagamento == 1 or pagamento == 2 or pagamento == 3 or pagamento == 4:
                    print()
                else:
                    print("\033[1;31mTENTE NOVAMENTE OPÇÃO INVALIDA\033[m")
                if pagamento == 1:
                    cep = int(input("DIGITE SEU CEP: "))

                    nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                    print("CEP: ",cep)
                    print("NOME DO RECEBIDOR: ",nome1)
                    print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                    while True:
                        vezes = int(input("DIGITE EM QUANTAS VEZES VOCÊ QUER PARCELAR: "))
                        if vezes > 15:
                            print("\033[1;91mNÃO PODEMOS FAZER MAIS QUE 15X\033[m")
                        if vezes < 2:
                            print("\033[1;91mNÃO PODEMOS FAZER EM MENOS QUE 2X\033[m")
                        if vezes >= 2 and vezes <= 15:
                            print("O VALOR FICARÁ DE R$",1030 // vezes,"MENSAL")
                        break
                    nomecartao = str(input("NOME DO CARTÃO: "))
                    while True:
                        total=0
                        s = input('DIGITE O NUMERO DO CARTÃO (SEM SINAIS "-->"): ')
                        if (len(s) != 16):
                            print ("NUMERO ERRADO. TENTE NOVAMENTE")
                            exit()
                        for i in range(0,16,2):
                            acum=int(s[i])*2
                        if (acum > 9):
                            acum=acum-9
                            total=total+acum
                        for i in range(1,17,2):
                            total=total+int(s[i])
                        if ((total%10) != 0 or total > 150):
                            print ("CARTÃO INVALIDO")
                            continue
                        print ("CARTÃO VALIDO: %s" % s)
                        break
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
1- CARTÃO DE CRÉDITO PARCELADO
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
                if pagamento == 1 or pagamento == 2 or pagamento == 3 or pagamento == 4:
                    print()
                else:
                    print("\033[1;31mTENTE NOVAMENTE OPÇÃO INVALIDA\033[m")
                if pagamento == 1:
                    cep = int(input("DIGITE SEU CEP: "))

                    nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                    print("CEP: ",cep)
                    print("NOME DO RECEBIDOR: ",nome1)
                    print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                    while True:
                        vezes = int(input("DIGITE EM QUANTAS VEZES VOCÊ QUER PARCELAR: "))
                        if vezes > 15:
                            print("\033[1;91mNÃO PODEMOS FAZER MAIS QUE 15X\033[m")
                        if vezes < 2:
                            print("\033[1;91mNÃO PODEMOS FAZER EM MENOS QUE 2X\033[m")
                        if vezes >= 2 and vezes <= 15:
                            print("O VALOR FICARÁ DE R$",1790 // vezes,"MENSAL")
                        break
                    nomecartao = str(input("NOME DO CARTÃO: "))
                    while True:
                        total=0
                        s = input('DIGITE O NUMERO DO CARTÃO (SEM SINAIS "-->"): ')
                        if (len(s) != 16):
                            print ("NUMERO ERRADO. TENTE NOVAMENTE")
                            exit()
                        for i in range(0,16,2):
                            acum=int(s[i])*2
                        if (acum > 9):
                            acum=acum-9
                            total=total+acum
                        for i in range(1,17,2):
                            total=total+int(s[i])
                        if ((total%10) != 0 or total > 150):
                            print ("CARTÃO INVALIDO")
                            continue
                        print ("CARTÃO VALIDO: %s" % s)
                        break
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
1- CARTÃO DE CRÉDITO PARCELADO
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
                if pagamento == 1 or pagamento == 2 or pagamento == 3 or pagamento == 4:
                    print()
                else:
                    print("\033[1;31mTENTE NOVAMENTE OPÇÃO INVALIDA\033[m")
                if pagamento == 1:
                    cep = int(input("DIGITE SEU CEP: "))

                    nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                    print("CEP: ",cep)
                    print("NOME DO RECEBIDOR: ",nome1)
                    print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                    while True:
                        vezes = int(input("DIGITE EM QUANTAS VEZES VOCÊ QUER PARCELAR: "))
                        if vezes > 15:
                            print("\033[1;91mNÃO PODEMOS FAZER MAIS QUE 15X\033[m")
                        if vezes < 2:
                            print("\033[1;91mNÃO PODEMOS FAZER EM MENOS QUE 2X\033[m")
                        if vezes >= 2 and vezes <= 15:
                            print("O VALOR FICARÁ DE R$",300 // vezes,"MENSAL")
                        break
                    nomecartao = str(input("NOME DO CARTÃO: "))
                    while True:
                        total=0
                        s = input('DIGITE O NUMERO DO CARTÃO (SEM SINAIS "-->"): ')
                        if (len(s) != 16):
                            print ("NUMERO ERRADO. TENTE NOVAMENTE")
                            exit()
                        for i in range(0,16,2):
                            acum=int(s[i])*2
                        if (acum > 9):
                            acum=acum-9
                            total=total+acum
                        for i in range(1,17,2):
                            total=total+int(s[i])
                        if ((total%10) != 0 or total > 150):
                            print ("CARTÃO INVALIDO")
                            continue
                        print ("CARTÃO VALIDO: %s" % s)
                        break
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
1- CARTÃO DE CRÉDITO PARCELADO
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
                if pagamento == 1 or pagamento == 2 or pagamento == 3 or pagamento == 4:
                    print()
                else:
                    print("\033[1;31mTENTE NOVAMENTE OPÇÃO INVALIDA\033[m")
                if pagamento == 1:
                    cep = int(input("DIGITE SEU CEP: "))

                    nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                    print("CEP: ",cep)
                    print("NOME DO RECEBIDOR: ",nome1)
                    print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                    while True:
                        vezes = int(input("DIGITE EM QUANTAS VEZES VOCÊ QUER PARCELAR: "))
                        if vezes > 15:
                            print("\033[1;91mNÃO PODEMOS FAZER MAIS QUE 15X\033[m")
                        if vezes < 2:
                            print("\033[1;91mNÃO PODEMOS FAZER EM MENOS QUE 2X\033[m")
                        if vezes >= 2 and vezes <= 15:
                            print("O VALOR FICARÁ DE R$",3299 // vezes,"MENSAL")
                        break
                    nomecartao = str(input("NOME DO CARTÃO: "))
                    while True:
                        total=0
                        s = input('DIGITE O NUMERO DO CARTÃO (SEM SINAIS "-->"): ')
                        if (len(s) != 16):
                            print ("NUMERO ERRADO. TENTE NOVAMENTE")
                            exit()
                        for i in range(0,16,2):
                            acum=int(s[i])*2
                        if (acum > 9):
                            acum=acum-9
                            total=total+acum
                        for i in range(1,17,2):
                            total=total+int(s[i])
                        if ((total%10) != 0 or total > 150):
                            print ("CARTÃO INVALIDO")
                            continue
                        print ("CARTÃO VALIDO: %s" % s)
                        break
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
        case 3:           
            print("1- FARCRY 6 | VALOR: R$380")
            print("2- FIFA 23 | VALOR: R$350")
            print("3- CALL OF DUTY MW2 | VALOR: R$530")
            print("4- FREE FIRE | VALOR: R$200")
            print("5- FORZA HORIZON 5 | VALOR: R$400")
            print("6- eFOOTBALL 2023 | VALOR: R$320")
            print("")
            jogos = int(input("""QUAL OPÇÃO VOCÊ DESEJA COMPRAR? DIGITE O NUMERO DO ITEM: """))
            if jogos == 1 or jogos == 2 or jogos == 3 or jogos == 4 or jogos == 5 or jogos == 6:
                print()
            else:
                print("\033[1;31mTENTE NOVAMENTE OPÇÃO INVALIDA\033[m")
            print("")
            if jogos == 1:
                pagamento = int(input("""QUAL SERÁ A FORMA DE PAGAMENTO?: 
1- CARTÃO DE CRÉDITO PARCELADO
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
                if pagamento == 1 or pagamento == 2 or pagamento == 3 or pagamento == 4:
                    print()
                else:
                    print("\033[1;31mTENTE NOVAMENTE OPÇÃO INVALIDA\033[m")
                if pagamento == 1:
                    cep = int(input("DIGITE SEU CEP: "))

                    nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                    print("CEP: ",cep)
                    print("NOME DO RECEBIDOR: ",nome1)
                    print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                    while True:
                        vezes = int(input("DIGITE EM QUANTAS VEZES VOCÊ QUER PARCELAR: "))
                        if vezes > 15:
                            print("\033[1;91mNÃO PODEMOS FAZER MAIS QUE 15X\033[m")
                        if vezes < 2:
                            print("\033[1;91mNÃO PODEMOS FAZER EM MENOS QUE 2X\033[m")
                        if vezes >= 2 and vezes <= 15:
                            print("O VALOR FICARÁ DE R$",380 // vezes,"MENSAL")
                        break
                    nomecartao = str(input("NOME DO CARTÃO: "))
                    while True:
                        total=0
                        s = input('DIGITE O NUMERO DO CARTÃO (SEM SINAIS "-->"): ')
                        if (len(s) != 16):
                            print ("NUMERO ERRADO. TENTE NOVAMENTE")
                            exit()
                        for i in range(0,16,2):
                            acum=int(s[i])*2
                        if (acum > 9):
                            acum=acum-9
                            total=total+acum
                        for i in range(1,17,2):
                            total=total+int(s[i])
                        if ((total%10) != 0 or total > 150):
                            print ("CARTÃO INVALIDO")
                            continue
                        print ("CARTÃO VALIDO: %s" % s)
                        break
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
                    print("O VALOR É DE R$380 A VISTA")
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
                    print("O VALOR É DE R$380 E PARA SER APROVADO LEVA EM TORNO DE 3 A 5 DIAS ÚTEIS!")
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
                    print("O VALOR É DE R$380 E É APROVADO EM SEGUIDA APÓS O PIX!")
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
            if jogos == 2:              
                pagamento = int(input("""QUAL SERÁ A FORMA DE PAGAMENTO?: 
1- CARTÃO DE CRÉDITO PARCELADO
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
                if pagamento == 1 or pagamento == 2 or pagamento == 3 or pagamento == 4:
                    print()
                else:
                    print("\033[1;31mTENTE NOVAMENTE OPÇÃO INVALIDA\033[m")
                if pagamento == 1:
                    cep = int(input("DIGITE SEU CEP: "))

                    nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                    print("CEP: ",cep)
                    print("NOME DO RECEBIDOR: ",nome1)
                    print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                    while True:
                        vezes = int(input("DIGITE EM QUANTAS VEZES VOCÊ QUER PARCELAR: "))
                        if vezes > 15:
                            print("\033[1;91mNÃO PODEMOS FAZER MAIS QUE 15X\033[m")
                        if vezes < 2:
                            print("\033[1;91mNÃO PODEMOS FAZER EM MENOS QUE 2X\033[m")
                        if vezes >= 2 and vezes <= 15:
                            print("O VALOR FICARÁ DE R$",350 // vezes,"MENSAL")
                        break
                    nomecartao = str(input("NOME DO CARTÃO: "))
                    while True:
                        total=0
                        s = input('DIGITE O NUMERO DO CARTÃO (SEM SINAIS "-->"): ')
                        if (len(s) != 16):
                            print ("NUMERO ERRADO. TENTE NOVAMENTE")
                            exit()
                        for i in range(0,16,2):
                            acum=int(s[i])*2
                        if (acum > 9):
                            acum=acum-9
                            total=total+acum
                        for i in range(1,17,2):
                            total=total+int(s[i])
                        if ((total%10) != 0 or total > 150):
                            print ("CARTÃO INVALIDO")
                            continue
                        print ("CARTÃO VALIDO: %s" % s)
                        break
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
                    print("O VALOR É DE R$350 A VISTA")
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
                    print("O VALOR É DE R$350 E PARA SER APROVADO LEVA EM TORNO DE 3 A 5 DIAS ÚTEIS!")
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
                    print("O VALOR É DE R$350 E É APROVADO EM SEGUIDA APÓS O PIX!")
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
            if jogos == 3:              
                pagamento = int(input("""QUAL SERÁ A FORMA DE PAGAMENTO?: 
1- CARTÃO DE CRÉDITO PARCELADO
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
                if pagamento == 1 or pagamento == 2 or pagamento == 3 or pagamento == 4:
                    print()
                else:
                    print("\033[1;31mTENTE NOVAMENTE OPÇÃO INVALIDA\033[m")
                if pagamento == 1:
                    cep = int(input("DIGITE SEU CEP: "))

                    nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                    print("CEP: ",cep)
                    print("NOME DO RECEBIDOR: ",nome1)
                    print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                    while True:
                        vezes = int(input("DIGITE EM QUANTAS VEZES VOCÊ QUER PARCELAR: "))
                        if vezes > 15:
                            print("\033[1;91mNÃO PODEMOS FAZER MAIS QUE 15X\033[m")
                        if vezes < 2:
                            print("\033[1;91mNÃO PODEMOS FAZER EM MENOS QUE 2X\033[m")
                        if vezes >= 2 and vezes <= 15:
                            print("O VALOR FICARÁ DE R$",530 // vezes,"MENSAL")
                        break
                    nomecartao = str(input("NOME DO CARTÃO: "))
                    while True:
                        total=0
                        s = input('DIGITE O NUMERO DO CARTÃO (SEM SINAIS "-->"): ')
                        if (len(s) != 16):
                            print ("NUMERO ERRADO. TENTE NOVAMENTE")
                            exit()
                        for i in range(0,16,2):
                            acum=int(s[i])*2
                        if (acum > 9):
                            acum=acum-9
                            total=total+acum
                        for i in range(1,17,2):
                            total=total+int(s[i])
                        if ((total%10) != 0 or total > 150):
                            print ("CARTÃO INVALIDO")
                            continue
                        print ("CARTÃO VALIDO: %s" % s)
                        break
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
                    print("O VALOR É DE R$530 A VISTA")
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
                    print("O VALOR É DE R$530 E PARA SER APROVADO LEVA EM TORNO DE 3 A 5 DIAS ÚTEIS!")
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
                    print("O VALOR É DE R$530 E É APROVADO EM SEGUIDA APÓS O PIX!")
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
            if jogos == 4:             
                pagamento = int(input("""QUAL SERÁ A FORMA DE PAGAMENTO?: 
1- CARTÃO DE CRÉDITO PARCELADO
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
                if pagamento == 1 or pagamento == 2 or pagamento == 3 or pagamento == 4:
                    print()
                else:
                    print("\033[1;31mTENTE NOVAMENTE OPÇÃO INVALIDA\033[m")
                if pagamento == 1:
                    cep = int(input("DIGITE SEU CEP: "))

                    nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                    print("CEP: ",cep)
                    print("NOME DO RECEBIDOR: ",nome1)
                    print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                    while True:
                            vezes = int(input("DIGITE EM QUANTAS VEZES VOCÊ QUER PARCELAR: "))
                            if vezes > 15:
                                print("\033[1;91mNÃO PODEMOS FAZER MAIS QUE 15X\033[m")
                            if vezes < 2:
                                print("\033[1;91mNÃO PODEMOS FAZER EM MENOS QUE 2X\033[m")
                            if vezes >= 2 and vezes <= 15:
                                print("O VALOR FICARÁ DE R$",200 // vezes,"MENSAL")
                            break
                    nomecartao = str(input("NOME DO CARTÃO: "))
                    while True:
                        total=0
                        s = input('DIGITE O NUMERO DO CARTÃO (SEM SINAIS "-->"): ')
                        if (len(s) != 16):
                            print ("NUMERO ERRADO. TENTE NOVAMENTE")
                            exit()
                        for i in range(0,16,2):
                            acum=int(s[i])*2
                        if (acum > 9):
                            acum=acum-9
                            total=total+acum
                        for i in range(1,17,2):
                            total=total+int(s[i])
                        if ((total%10) != 0 or total > 150):
                            print ("CARTÃO INVALIDO")
                            continue
                        print ("CARTÃO VALIDO: %s" % s)
                        break                 
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
                    print("O VALOR É DE R$200 A VISTA")
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
                    print("O VALOR É DE R$200 E PARA SER APROVADO LEVA EM TORNO DE 3 A 5 DIAS ÚTEIS!")
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
                    print("O VALOR É DE R$200 E É APROVADO EM SEGUIDA APÓS O PIX!")
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
            if jogos == 5:              
                pagamento = int(input("""QUAL SERÁ A FORMA DE PAGAMENTO?: 
1- CARTÃO DE CRÉDITO PARCELADO
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
                if pagamento == 1 or pagamento == 2 or pagamento == 3 or pagamento == 4:
                    print()
                else:
                    print("\033[1;31mTENTE NOVAMENTE OPÇÃO INVALIDA\033[m")
                if pagamento == 1:
                    cep = int(input("DIGITE SEU CEP: "))

                    nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                    print("CEP: ",cep)
                    print("NOME DO RECEBIDOR: ",nome1)
                    print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                    while True:
                        vezes = int(input("DIGITE EM QUANTAS VEZES VOCÊ QUER PARCELAR: "))
                        if vezes > 15:
                            print("\033[1;91mNÃO PODEMOS FAZER MAIS QUE 15X\033[m")
                        if vezes < 2:
                            print("\033[1;91mNÃO PODEMOS FAZER EM MENOS QUE 2X\033[m")
                        if vezes >= 2 and vezes <= 15:
                            print("O VALOR FICARÁ DE R$",400 // vezes,"MENSAL")
                        break
                    nomecartao = str(input("NOME DO CARTÃO: "))
                    while True:
                        total=0
                        s = input('DIGITE O NUMERO DO CARTÃO (SEM SINAIS "-->"): ')
                        if (len(s) != 16):
                            print ("NUMERO ERRADO. TENTE NOVAMENTE")
                            exit()
                        for i in range(0,16,2):
                            acum=int(s[i])*2
                        if (acum > 9):
                            acum=acum-9
                            total=total+acum
                        for i in range(1,17,2):
                            total=total+int(s[i])
                        if ((total%10) != 0 or total > 150):
                            print ("CARTÃO INVALIDO")
                            continue
                        print ("CARTÃO VALIDO: %s" % s)
                        break
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
                    print("O VALOR É DE R$400 A VISTA")
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
                    print("O VALOR É DE R$400 E PARA SER APROVADO LEVA EM TORNO DE 3 A 5 DIAS ÚTEIS!")
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
                    print("O VALOR É DE R$400 E É APROVADO EM SEGUIDA APÓS O PIX!")
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
            if jogos == 6:              
                pagamento = int(input("""QUAL SERÁ A FORMA DE PAGAMENTO?: 
1- CARTÃO DE CRÉDITO PARCELADO
2- A VISTA
3- BOLETO
4- PIX
DIGITE A OPÇÃO: """))
                if pagamento == 1 or pagamento == 2 or pagamento == 3 or pagamento == 4:
                    print()
                else:
                    print("\033[1;91mTENTE NOVAMENTE OPÇÃO INVALIDA\033[m")
                while True:
                    if pagamento == 1:
                        cep = int(input("DIGITE SEU CEP: "))
                        nome1 = str(input("DIGITE O NOME COMPLETO DO RECEBIDOR: "))
                        print("CEP: ",cep)
                        print("NOME DO RECEBIDOR: ",nome1)
                        print("PRAZO ESTIMADO DE ENTREGA É DE 15 DIAS")
                        while True:
                            vezes = int(input("DIGITE EM QUANTAS VEZES VOCÊ QUER PARCELAR: "))
                            if vezes > 15:
                                print("\033[1;91mNÃO PODEMOS FAZER MAIS QUE 15X\033[m")
                            if vezes < 2:
                                print("\033[1;91mNÃO PODEMOS FAZER EM MENOS QUE 2X\033[m")
                            if vezes >= 2 and vezes <= 15:
                                print("O VALOR FICARÁ DE R$",320 // vezes,"MENSAL")
                            break    
                        nomecartao = str(input("NOME DO CARTÃO: "))
                        while True:
                            total=0
                            s = input('DIGITE O NUMERO DO CARTÃO (SEM SINAIS "-->"): ')
                            if (len(s) != 16):
                                print ("NUMERO ERRADO. TENTE NOVAMENTE")
                                exit()
                            for i in range(0,16,2):
                                acum=int(s[i])*2
                            if (acum > 9):
                                acum=acum-9
                                total=total+acum
                            for i in range(1,17,2):
                                total=total+int(s[i])
                            if ((total%10) != 0 or total > 150):
                                print ("CARTÃO INVALIDO")
                                continue
                            print ("CARTÃO VALIDO: %s" % s)  
                            break
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
                        print("O VALOR É DE R$320 A VISTA")
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
                        print("O VALOR É DE R$320 E PARA SER APROVADO LEVA EM TORNO DE 3 A 5 DIAS ÚTEIS!")
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
                        print("O VALOR É DE R$320 E É APROVADO EM SEGUIDA APÓS O PIX!")
                        print("CÓDIGO DO PIX COPIA E COLA: 0ada2d1a05150db6181dfh320da916030ada310hj02")
                        while True:
                            conf = int(input("DIGITE \033[1;96m1\033[m PARA CONFIRMAR COMPRA: "))                
                            if conf == 1:
                                print("\033[1;92mCOMPRA EFETUADA COM SUCESSO!\033[m")
                                break
                            elif conf == 2:
                                print("\033[1;35mCOMPRA CANCELADA!\033[m")
                            else:
                                print("\033[1;31mCOMPRA NÃO CONFIRMADA! TENTE NOVAMENTE\033[m")

                            cursor.close()
                            conexao.close()
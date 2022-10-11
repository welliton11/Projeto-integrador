import sys
class Cartao:
    def __init__(self) -> None:
        pass
    def Validar(self):
        while True:
            total=0
            num_cartao = str(input('Numero do cartao (sem espaços): '))
            if (len(num_cartao) != 16):
                print("\nSó pode ter 16 dígitos!\n")
                continue
            for i in range(0,16,2):
                acum=int(num_cartao[i])*2
                if (acum > 9):
                    acum=acum-9
                    total=total+acum
            for i in range(1,17,2):
                total=total+int(num_cartao[i])
            if ((total%10) != 0 or total > 150):
                print("\n\033[1;32mCartão inválido!\n\033[m")
                continue
            print("\033[0;32m\nCartao valido!\033[m\n")
            return num_cartao
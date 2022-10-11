import time

def progresso(a):
    print("\r\033[1mCarregando: [{0:50s}] {1:.1f}%".format('#' * int(a * 50), a * 100),end='')

def test():
    for n in range(101):
        progresso(n/100)
        time.sleep(0.01)
test()
print('\n\033[0;32m\033[1mOBRIGADO PELA COMPRA!!!\n\033[m\033[m')
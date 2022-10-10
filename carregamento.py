import time

def progresso(a):
    print("\rProgress: [{0:50s}] {1:.1f}%".format('#' * int(a * 50), a * 100),end='')

def test():
    for n in range(101):
        progresso(n/100)
        time.sleep(0.01)
test()
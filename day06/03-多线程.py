from time import sleep
from threading import Thread


def sing(name):
    for i in range(5):
        print("我在唱%s" % name)
        sleep(1)

def dance(name):
    for i in range(5):
        print("我在跳%s" % name)
        sleep(1)

t1 = Thread(target=sing, args=("喜洋洋",))
t2 = Thread(target=dance, args=("rap",))

t1.start()
t2.start()
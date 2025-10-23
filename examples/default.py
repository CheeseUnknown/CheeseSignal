import __init__
from CheeseSignal import Signal

signal = Signal()

def handle_1():
    print('Handler 1 executed')
signal.connect(handle_1)

@signal.connect()
def handle_2():
    print('Handler 2 executed')

if __name__ == '__main__':
    signal.send()

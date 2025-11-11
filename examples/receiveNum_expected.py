import __init__
from CheeseSignal import Signal

signal = Signal()

@signal.connect(receive_num_expected = 3)
def handle_1():
    print('Handler 1 executed')

@signal.connect(receive_num_expected = 3, auto_remove = True)
def handle_2():
    print('Handler 2 executed')

if __name__ == '__main__':
    for i in range(5):
        signal.send()
        print(list(signal.receivers.keys()))

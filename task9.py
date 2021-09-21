import threading
import time

def stream1(interval):
    i = 10
    while i > 0:
        print(f'Время: {time.ctime()} Поток: {t1.getName()}', i, end='\r\n')
        time.sleep(interval)
        i -= 1


def stream2(interval):
    i = 10
    while i > 0:
        print(f'Время: {time.ctime()} Поток: {t2.getName()}', i, end='\r\n')
        time.sleep(interval)
        i -= 1


t1 = threading.Thread(target=stream1, args=(1,))
t1.daemon = True
t1.start()

t2 = threading.Thread(target=stream2, args=(1,))
t2.daemon = True
t2.start()

t1.join()
t2.join()
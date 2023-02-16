from time import sleep
h = m = s = 0

while True:
    sleep(1)
    if s != 60:
        s += 1
    else:
        s = 0
        m += 1
    if m == 60:
        m = 0
        h += 1
        
    print(f'{h}:{m}:{s}')

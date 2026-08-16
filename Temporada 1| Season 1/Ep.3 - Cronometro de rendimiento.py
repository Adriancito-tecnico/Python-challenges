import time, threading

def contador():
    t_s = 0
    t_milis = 0
    while True:
        time.sleep(0.05)
        t_milis += 50

        if t_milis == 1000:
            t_milis = 0
            t_s += 1
        print(f"\r Time: {t_s}.{"0"*(3 - len(list(str(t_milis))))}{t_milis}S", end=" ")

threading.Thread(target=contador, daemon=True).start()

#operación simultane
result = 0
for i in range(99999999):
    result += i

print(f"\n {result}")
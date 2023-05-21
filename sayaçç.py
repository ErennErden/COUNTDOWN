import time
from plyer import notification
def countdown(n): 
    while n != 0:
        n -= 1
        time.sleep(1) 
        print(n) 
    notification.notify(
        title = "sayacın geri bildirimi", 
        message = "ZAMAN DOLDU ASKER!! ", 
        timeout=2,) 
    time.sleep(5)


sayac = int(input("geri sayım için zaman dilimi giriniz:  "))
countdown(sayac)
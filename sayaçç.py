import time
from plyer import notification
def countdown(n): # sonsuz döngü içinde n değişkeni 0 a eşit değilse n değişkeninden 1 çıkar ve 1 saniye bekle
    while n != 0:
        n -= 1
        time.sleep(1) #bir saniyeliğine programı durdur/uyut/kapat
        print(n) #her n değişkeni azalınca ve 1 saniye geçince n-1 i yani geri sayım süresini göster
    notification.notify(
        title = "sayacın geri bildirimi", #geri bildirimin başlık kısmı
        message = "ZAMAN DOLDU ASKER!! ", #geri bildirim mesajı
        timeout=2,) #2 saniye olunca while döngüsü ile beraber bitir programı
    time.sleep(5) #eğer yazmazsanız mesaj otomatik olarak değil manuel olarak kapatılır ve parantezin dışına yazılmalı


sayac = int(input("geri sayım için zaman dilimi giriniz:  "))
countdown(sayac)
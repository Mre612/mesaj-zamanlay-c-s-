import schedule
import time
from datetime import datetime, timedelta

def send_mesaj(mesaj):
    print(f"Mesaj gönderildi: {mesaj}")

def schedule_mesaj():
    mesaj = input("Göndermek istediğiniz mesajı girin: ")
    schedule_time = input("Mesajın gönderileceği saati (SS:DD formatında) girin: ")

    try:
        hour, minute = map(int, schedule_time.split(':'))
        assert 0 <= hour < 24 and 0 <= minute < 60
    except (ValueError, AssertionError):
        print("Geçersiz zaman formatı! Lütfen SS:DD formatında doğru bir zaman girin.")
        return

    now = datetime.now()
    scheduled_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

    if scheduled_time < now:
        scheduled_time += timedelta(days=1)

    schedule.every().day.at(scheduled_time.strftime("%H:%M")).do(send_mesaj, mesaj)

    time_diff = (scheduled_time - now).total_seconds()

    if time_diff < 60:
        print(f"Mesajınız {int(time_diff)} saniye sonra gönderilecek.")
    elif time_diff < 3600:
        minutes = time_diff // 60
        seconds = int(time_diff % 60)
        print(f"Mesajınız {int(minutes)} dakika {seconds} saniye sonra gönderilecek.")
    else:
        hours = time_diff // 3600
        minutes = (time_diff % 3600) // 60
        print(f"Mesajınız {int(hours)} saat {int(minutes)} dakika sonra gönderilecek.")

    another_time = input("Başka bir saatte de göndermek istiyor musunuz? (e/h): ").strip().lower()
    if another_time == 'e':
        schedule_mesaj()

if __name__ == "__main__":
    schedule_mesaj()
    while True:
        schedule.run_pending()
        time.sleep(1)
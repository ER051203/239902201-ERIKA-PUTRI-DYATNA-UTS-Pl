print("--MEMBUAT PROGRAM YANG MEMBACA & MENCETAK TANGGAL DARI JUMLAH HARI--")

from datetime import datetime, timedelta

num_days = int(input("Silahkan Masukan Jumlah Hari: "))  #input jumlah hari 

today = datetime.now()
future_date = today + timedelta(days=num_days)

day_of_week = future_date.strftime('%A')                #hari dalam 1 minggu

date_string = future_date.strftime("on %d %B %Y")       #Format tanggal

print(f"{day_of_week} {date_string}")                   #output yang mencetak tanggal

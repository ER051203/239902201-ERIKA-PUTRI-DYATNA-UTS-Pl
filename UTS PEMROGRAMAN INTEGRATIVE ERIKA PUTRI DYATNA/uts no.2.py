print("--MEMBUAT PROGRAM YANG MEMBACA & MENCETAK TANGGAL UJIAN HARI INI & SEMUA NILAI DARI 1 SAMPAI ANGKA TERSEBUT--")

import sys
from datetime import date

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    try:
        today = date.today()
        day = today.day
        product = factorial(day)
        print(f'Semua produk dari angka 1 sampai {day} is: {product}')
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
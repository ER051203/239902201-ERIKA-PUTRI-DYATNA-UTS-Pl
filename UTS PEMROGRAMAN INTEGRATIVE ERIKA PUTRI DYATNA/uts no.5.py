print ("--PROGRAM YANG MEMBACA BLANGAN BULAT--")

# Inisialisasi total sebagai 0
total = 0

with open('input.txt', 'r') as file:   # Buka file indata.txt di direktori yang sama dengan program
    for line in file:                   # Baca setiap baris dari file
        try:
            number = int(line.strip())  # Coba untuk mengonversi baris menjadi bilangan bulat
            total += number             # Tambahkan bilangan bulat ke total
        except ValueError:
            print(f"Error: '{line.strip()}' is not a valid integer.")   # Tangani kesalahan jika baris tidak dapat diubah menjadi bilangan bulat

# Format total dengan pemisah koma dan dua digit desimal
formatted_total = '{:,.3f}'.format(total)

# Cetak total yang diformat
print(formatted_total)


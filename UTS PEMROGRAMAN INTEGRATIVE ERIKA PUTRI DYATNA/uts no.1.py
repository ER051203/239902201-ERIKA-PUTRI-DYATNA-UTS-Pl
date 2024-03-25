print("--MEMBUAT PROGRAM YANG MEMBACA BIL.BULAT & DIBAGI JUMLAH HARI TAHUN INI--")

def read_numbers_from_file(file_name):
    numbers = []
    with open(file_name, 'r') as file:
        for line in file:
            number = int(line.strip())
            numbers.append(number)
    return numbers

def divide_by_number_of_days(numbers, jumlah_hari_dalam_1_tahun):
    result = []
    for number in numbers:
        result.append(number / jumlah_hari_dalam_1_tahun)
    return result

def main():
    file_name = 'indata.txt'
    numbers = read_numbers_from_file(file_name)

    jumlah_hari_dalam_1_tahun = 366

    divided_numbers = divide_by_number_of_days(numbers, jumlah_hari_dalam_1_tahun)

    for num in divided_numbers:
        print(f'{num :.11f}')

if __name__ == '__main__':
    main()
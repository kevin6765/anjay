#MEMANGGIL MODUL
import math

#INPUT
print('\n----- Selamat datang di program menghitung banyaknya kata yang dapat disusun -----')
n = int(input('\nMasukan jumlah huruf dalam kata SISTEM INFORMASI\n*JUMLAH TIDAK MENYERTAKAN HURUF DOUBLE = '))
r = int(input('\nMasukan jumlah huruf yang ingin dibentuk dari kata tersebut = '))

#PROSES
c = math.factorial(n)
d = math.factorial(n-r)
i = math.factorial(r)
o = c/(d*i)

#OUTPUT
print('\n------------------ MOHON DITUNGGU, SISTEM SEDANG MEMPROSES DATA ------------------\n')
print('Banyak kata yang dapat disusun', o)
print()
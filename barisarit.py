print('------- Selamat datang di program menghitung suku ke N -------')

#INPUT
suku_n = int(input("\nMasukan urutan bilangan yang ingin di ketahui = "))
urutan_3 = int(input('\nMasukan urutan bilangan pertama yang sudah diketahui = ')) 
suku_3 = int(input('Masukan besar bilangan pertama yang sudah diketahui = ')) 
urutan_7 = int(input('Masukan urutan bilangan kedua yang sudah diketahui = '))
suku_7 = int(input('Masukan besar bilangan kedua yang sudah diketahui = '))

#PROSES
b = (suku_7 - suku_3) // (urutan_7 - urutan_3)
a = suku_3 - (urutan_3 - 1) * b
Un = a + (suku_n - 1) * b
sn = (suku_n / 2) * (a + Un)

#OUTPUT
print('\n-------- MOHON DITUNGGU, SISTEM SEDANG MEMPROSES DATA --------\n')
print("Hasil dari Nilai A yaitu = ", a) 
print("Hasil dari Nilai B yaitu = ", b)
print("Hasil dari Suku ke -", suku_n, "yaitu = " , Un)
print("Hasil dari Banyak suku yaitu = " , suku_n)
print("Hasil dari Jumlah suku ke -", suku_n, "yaitu = ", sn, "\n")
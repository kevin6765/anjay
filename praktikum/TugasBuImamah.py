matriks1 = []
matriks2 = []

matrikstambah = []
matrikskurang = []
matrikskali = []
matriksbagi = []

print('==========================================================')
print('Halo Kevin! Selamat datang kembali di program pencetak NIM\n')

for i in range(0, 2):
    for j in range (0, 2):
        matriks1[i][j] = int(input('Silahkan masukan angka = '))


for i in range(0, 2):
    for j in range (0, 2):
        matriks2[i][j] = int(input('Silahkan masukan angka = '))
        
print(matriks1)
print(matriks2)

for i in matriks1:
  for j in matriks2:
    matrikstambah.append(i+j)
print('matriks penjumlahan = ', matrikstambah)

for i in matriks1:
  for j in matriks2:
    matrikskurang.append(i-j)
print('matriks pengurangan = ', matrikskurang)

for i in matriks1:
  for j in matriks2:
    matrikskali.append(i*j)
print('matriks perkalian = ', matrikskali)

for i in matriks1:
  for j in matriks2:
    matriksbagi.append(i/j)
print('matriks pembagian = ', matriksbagi)

print("Operasi Pembagian, Perkalian, Penjumlahan, dan pengKurangan Pada Matriks")
m = int(input('Jumlah Baris Kedua Matriks = '))
n = int(input('Jumlah Kolom kedua Matriks = '))
matriks1 = []
matriks2 = []
print("Masukkan Elemen Matriks 1 :")

for i in range(0,m):
    matriks1 += [0]
for i in range (0,m):
    matriks1[i] = [0]*n
for i in range (0,m):
    for j in range (0,n):
        print ('Masukkan baris ke-',i+1,' kolom ke-',j+1)
        matriks1[i][j] = int(input())

print("Masukkan Elemen Matriks 2 :")
for i in range(0,m):
    matriks2 += [0]
for i in range (0,m):
    matriks2[i] = [0]*n
for i in range (0,m):
    for j in range (0,n):
        print ('Masukkan baris ke-',i+1,' kolom ke-',j+1)
        matriks2[i][j] = int(input())

print ("Matriks ke 1 : ", matriks1)
print ("Matriks ke 2 : ", matriks2)

if(n == m):

    pembagian = [[0 for x in range(m)] for y in range(n)]
    for i in range(len(matriks1)):
        for j in range(len(matriks2[0])):
                pembagian[i][j] += matriks1[i][j] / matriks2[i][j]
    print("Pembagian Matriks 1 dan 2 : ", pembagian)

    
    perkalian = [[0 for x in range(m)] for y in range(n)]
    for i in range(len(matriks1)):
        for j in range(len(matriks2[0])):
            for k in range(len(matriks2)):
                perkalian[i][j] += matriks1[i][k] * matriks2[k][j]
    print("Perkalian Matriks 1 dan 2 : ", perkalian)


    penjumlahan = [[0 for x in range(m)] for y in range(n)]
    for i in range(len(matriks1)):
        for j in range(len(matriks2[0])):
                penjumlahan[i][j] += matriks1[i][j] + matriks2[i][j]
    print("Penjumlahan Matriks 1 dan 2 : ", penjumlahan)

    pengurangan = [[0 for x in range(m)] for y in range(n)]
    for i in range(len(matriks1)):
        for j in range(len(matriks2[0])):
                pengurangan[i][j] += matriks1[i][j] - matriks2[i][j]
    print("Pengurangan Matriks 1 dan 2 : ", pengurangan)

else:
    print("Untuk dapat melakukan Perkalian, Penjumlahan, dan Pengurangan Baris dan Kolom Matriks harus sama")

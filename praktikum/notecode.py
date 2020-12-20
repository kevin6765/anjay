durasi = int(input('DURASI (jam) = '))
kendaraan = int(input('Jenis kendaraan 1. Motor | 2. Mobil = '))
biaya1 = 3000
biaya2_motor = 2000
biaya2_mobil = 4000
biaya3 = 100000

print('sedang proses ---\n')
if durasi <= 2:
    biaya_akhir1 = biaya1 * durasi
    print('biaya anda adalah', biaya_akhir1)
elif 2 <= durasi <= 24 and kendaraan == 1:
    biaya_akhir2 = 6000 + (biaya2_motor * (durasi-2))
    print('biaya anda adalah', biaya_akhir2)
elif 2 <= durasi <= 24 and kendaraan == 2:
    biaya_akhir3 = 6000 + (biaya2_mobil * (durasi-2))
    print('biaya anda adalah', biaya_akhir3)
elif durasi >= 24 and kendaraan == 1:
    biaya_akhir2 = 6000 + (biaya2_motor * (durasi-2))
    biaya_akhir4 = biaya_akhir2 + (biaya3 * (durasi//24))
    print('biaya anda adalah', biaya_akhir4)
elif durasi >= 24 and kendaraan == 2:
    biaya_akhir3 = 6000 + (biaya2_mobil * (durasi-2))
    biaya_akhir5 = biaya_akhir3 + (biaya3 * (durasi//24))
    print('biaya anda adalah', biaya_akhir5)
else:
    print('perintah yang anda masukan error')

if choice == '1':
   print(num1,"+",num2,"=", penjumlahan(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", pengurangan(num1,num2))
elif choice == '3':
   print(num1,"x",num2,"=", perkalian(num1,num2))
elif choice == '4':
   print(num1,":",num2,"=", pembagian(num1,num2))
else:
   print("Input salah")

def kurang(angka1, angka2):
    kurang1 = print(angka1,"-",angka2,"=", angka1 - angka2)
    return kurang1
def tambah(angka1, angka2):
    tambah1 = angka1,"+",angka2,"=", angka1 + angka2
    return tambah1
def bagi(angka1, angka2):    
    bagi1 = angka1,":",angka2,"=", angka1 / angka2
    return bagi1
def kali(angka1, angka2):
    kali1 = angka1,"x",angka2,"=", angka1 * angka2
    return kali1

i = 0
while i == 0:
    pilihan2 = int(input("Masukkan pilihan(1/2/3/4): "))
    angka1 = int(input("Masukkan bilangan pertama: "))
    angka2 = int(input("Masukkan bilangan kedua: "))
    print(pilihan(pilihan2, angka1, angka2))
    print('Program telah selesai, ingin ulang?')
    y = 0
    while y == 0:
        ulang = int(input('Ketik 0 untuk YA dan 1 untuk TIDAK = '))
        if ulang == 0:
            y += 1
            break
        elif ulang == 1:
            y += 2
            break
        else:
            print('\nPerintah yang anda masukan error, silahkan coba lagi')
            continue
    if y == 1:
        continue
    else:
        break

    if pilihan2 == 1:
        pilihan3 = print(angka1, "-", angka2, "=", angka1 - angka2)
    elif pilihan2 == 2:
        pilihan3 = print(angka1, "+", angka2, "=", angka1 + angka2)
    elif pilihan2 == 3:
        pilihan3 = print(angka1, ":", angka2, "=", angka1 / angka2)
    elif pilihan2 == 4:
        pilihan3 = print(angka1, "x", angka2, "=", angka1 * angka2)
    else:
        pilihan3 = print('Pilihan error,silahkan coba lagi')
    return pilihan3

def faktorial(bil):
  hasil_faktorial = 1
  for x in range(2,bil+1):
    hasil_faktorial = hasil_faktorial * x
  return hasil_faktorial

print('Menghitung bilangan faktorial menggunakan for loop')
angka = int(input('Masukkan sebuah bilangan untuk dihitung nilai faktorialnya '))
faktorial_bil = faktorial(angka)
print('Bilangan faktorial dari {} adalah {}'.format(angka,faktorial_bil))

def faktorial(x):
  if x <= 1: # base scenario
    return 1
  else:
    f = x * faktorial(x-1)
    print(faktorial(x-1))
  return f

print('Menghitung bilangan faktorial menggunakan fungsi rekursif')
angka = int(input('Masukkan sebuah bilangan untuk dihitung nilai faktorialnya '))
faktorial_bil = faktorial(angka)
print('Bilangan faktorial dari {} adalah {}'.format(angka,faktorial_bil))

def faktorial():
    print('Menghitung bilangan faktorial menggunakan for loop')
    angka = int(input('Masukan angka = '))
    hasil_faktorial = 1
    for x in range(2,angka+1):
        print(x)
        hasil_faktorial = hasil_faktorial * x
    print('faktorial dari', angka, 'adalah', hasil_faktorial)

faktorial()
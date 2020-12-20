print('------- Selamat datang di program mengubah nilai angka kedalam nilai Abjad -------\n')

#INPUT
nama_kalian = input('Masukan Nama      : ')
nim_kalian = int(input('Masukan NIM       : '))
nilai_uts = float(input('Masukan Nilai UTS : '))
nilai_uas = float(input('Masukan nilai UAS : '))
print('\n--------------- MOHON DITUNGGU, SISTEM SEDANG MEMPROSES DATA ---------------------\n')

#PROSES + OUTPUT
nilai_total = (nilai_uts + nilai_uas) / 2
print('Nama anda adalah             :', nama_kalian)
print('NIM anda adalah              :', nim_kalian)

if nilai_uts > 100 or nilai_uas > 100:
    print('Nilai UTS atau UAS yang anda masukan salah, silahkan coba lagi!')
elif nilai_uts < 0 or nilai_uas < 0:
    print("Nilai UTS atau UAS yang anda masukan salah, silahkan coba lagi!")
else:
    print('Nilai rata-rata kamu adalah  :', nilai_total)

if nilai_uts > 100 or nilai_uas > 100:
    print("Nilai UTS atau UAS yang anda masukan salah, silahkan coba lagi!")
elif nilai_total < 0:
    print("Nilai Rata-rata anda error karena nilai UTS atau UAS yang anda input tidak benar")
elif 0 <= nilai_total <= 40:
    print('Anda mendapatkan nilai E')
elif 41 <= nilai_total <= 60:
    print('Anda mendapatkan nilai D')    
elif 61 <= nilai_total <= 70:
    print('Anda mendapatkan nilai C')
elif 71 <= nilai_total <= 80:
    print('Anda mendapatkan nilai B')
elif 81 <= nilai_total <= 100:
    print('Anda mendapatkan nilai A\n')
else :
    print()
print('\n--------------> Program telah selesai, ingin mencobanya lagi?\n')
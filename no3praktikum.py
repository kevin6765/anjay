print('Selamat datang di program validasi beasiswa\n')

#INPUT
nama = input('Silahkan masukan namamu = ')
skor_kamu = int(input('Silahkan masukan skormu = '))
ipk_kamu = float(input('Silahkan masukan ipkmu = '))

#PROSES + OUTPUT
if skor_kamu >= 1100 and ipk_kamu >= 3.0:
    print('Selamat', nama, ', kamu dinyatakan lolos')
else:
    print('Maaf', nama, ', kamu dinyatakan tidak lolos') 
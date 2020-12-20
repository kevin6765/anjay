print('Selamat datang di mesin pembayaran parkir otomatis')

#INPUT
nama = input('Silahkan masukan nama anda = ')
plat = int(input('Silahkan masukan No. Plat Anda = '))
jam_parkir = int(input('Silahkan masukan durasi parkir anda = '))
parkir = 3000

#PROSES
if jam_parkir <= 5:
    harga_total = parkir * jam_parkir
elif 5 < jam_parkir < 10:
    harga_total = ((jam_parkir - 5) * 2000) + (5 * parkir)
else: 
    harga_total = ((jam_parkir - 10) * 1000) + (5 * 2000) + (5 * parkir)

#OUTPUT
print('Halo', nama, 'Dengan No. Plat', plat)
print('Biaya total parkir kamu adalah', harga_total)


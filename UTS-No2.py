#Input
total_pembelian = int(input('Silahkan masukan total pembelian kamu = '))

#Proses
if total_pembelian < 100000:
    total_diskon = total_pembelian * 0.05
elif total_pembelian <= 500000:
    total_diskon = total_pembelian * 0.10
else:
    total_diskon = total_pembelian * 0.15

#Output
print('Selamat kamu mendapatkan diskon sebesar', total_diskon, 'rupiah')
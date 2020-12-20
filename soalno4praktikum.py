print('---------- Selamat datang di program penghitung volume kerucut ----------\n')

#INPUT
luas_selimut = float(input('Silahkan masukan Luas Selimutnya = '))
garis_pelukis = int(input('Silahkan masukan Garis Pelukisnya = '))
tinggi_kerucut = int(input('Silahkan masukan Tinggi Kerucut = '))
phi = int(3.14)

#PROSES
rumus = luas_selimut / (phi * garis_pelukis)
volume = (1 / 3) * (phi * tinggi_kerucut) * (rumus ** 2)
volume = volume / 1000

#OUTPUT
print('\n--------------- MOHON DITUNGGU, SISTEM SEDANG MEMPROSES DATA ------------')
print('\nHasil dari jari - jarinya adalah', round(rumus, 2), 'cm')
print('Hasil dari volumenya adalah', round(volume, 2), 'liter\n')
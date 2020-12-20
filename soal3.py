import itertools

kalimat = input('SITEMNFORA = ')
kalimat2 = int(input('Masukan = '))
jumlah = itertools.permutations(kalimat, kalimat2)
banyak = []
for kata in jumlah:
    banyak.append(kata)
print('Banyak kata yaitu = ', len(banyak), 'kata')

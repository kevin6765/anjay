def faktorial(bil):
  hasil_faktorial = 1
  for x in range(2,bil+1):
    hasil_faktorial = hasil_faktorial * x
  return hasil_faktorial

print('Menghitung bilangan faktorial menggunakan for loop')
angka = int(input('Masukkan sebuah bilangan untuk dihitung nilai faktorialnya '))
faktorial_bil = faktorial(angka)
print('Bilangan faktorial dari {} adalah {}'.format(angka,faktorial_bil))

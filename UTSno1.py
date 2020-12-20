#INPUT
a = int(input('Masukan Nilai = '))
b = int(input('Masukan nilai = '))
c = int(input('Masukan nilai = '))

#OUTPUT
if a > b and a > c:
    print('Nilai A yaitu', a, 'Adalah nilai terbesar')
elif b > a and b > c:
    print('Nilai B yaitu', b, 'Adalah nilai terbesar')
else:
    print('Nilai C yaitu', c, 'Adalah nilai terbesar')
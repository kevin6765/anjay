def faktorial(i):
    fact = 1
    for i in range (i,1,-1):
        fact *= i
    return fact
a = input('masukan kata = ')
spasi = 0
for z in a :
    if z == " " :
        spasi -= 1
b = len(a) + spasi
print('Jadi banyak huruf adaa : ', b)
sama = int(input('Banyak huruf yang sama : '))
hasil_hrf = 1
for x in range(1, sama+1) :
    print('masukan banyak huruf yang sama ke-', x, end=" ")
    hrf = int(input("=> "))
    hrf_fact = faktorial(hrf)
    hasil_hrf *= hrf_fact

h_jmlh = int(input('Jumlah huruf yang mau disusun = '))
selisih = b - h_jmlh
permutasi = ((faktorial(b))/ (faktorial(selisih)*hasil_hrf))
print('Banyak cara = ', permutasi)
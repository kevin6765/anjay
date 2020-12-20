def faktorial():
    i  = 0
    while i == 0:
        angka2 = []
        print('\n\tSelamat Datang di Program Menghitung Bilangan Faktorial')
        angka = int(input('\nSilahkan Masukan angka yang ingin dihitung = '))
        if angka <= 0:
            print('Angka yang dimasukan harus bilangan asli, silahkan coba lagi')
            continue
        else:
            hasil_faktorial = 1
            for p in range(1, angka + 1):
                angka2.append(p)
                hasil_faktorial = hasil_faktorial * p
            print('Faktorial dari', angka, 'adalah', hasil_faktorial, '| Susunan Bilangan Faktorial', angka2)
            
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

faktorial()
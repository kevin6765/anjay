i = 0
while i == 0:
    a = 0
    b = 0
    print('\n============================================================')
    print('\tSelamat Datang di Program Tuple Dinamis Python')
    print('Terdapat 2 Mode yaitu 1. Mode langsung dan 2. Mode isi list')
    pilihan = int(input('Silahkan masukan pilihan Anda (1/2) = '))

    if pilihan == 1:
        j = 0
        while j == 0:
            T = []
            T2 = (10, 30, 45, 21, 12, 13, 31, 90)
            T3 = ('pRaktikum', 'praktikum', 'Praktikum', 'PraKtIkuM', 'PRAKTIKUM')
            print('============================================================')
            print('\tSelamat Datang di Mode langsung')
            print('Terdapat 2 pilihan yaitu 1. Output satu dan 2. Output dua')
            pilihan1 = int(input('Silahkan masukan pilihan Anda (1/2) = '))
            print('============================================================')
            if pilihan1 == 1:
                k = 0
                for l in range(0, 5):
                    T.append(str(input('masukan nama kendaraan hingga 5 buah = ')))
                print('============================================================')
                T1 = tuple(T)
                print('Output 1 adalah =', T3[1], T3[3], T3[4], T1[4], T1[2])

            elif pilihan1 == 2:
                print('Output 2 adalah =')
                for c in range(3):
                    print(T2[3], 'dan', T2[5])
            else:
                print('Perintah yang anda masukan salah, silahkan coba lagi')
                continue
            print('============================================================')
            print('Program telah selesai | 1. Ulang Program | 2. Selesai | 3. Balik Ke Menu Awal')
            y = 0
            while y == 0:
                ulang = int(input('Masukan pilihan Anda (1/2/3) = '))
                if ulang == 1:
                    y += 1
                    break
                elif ulang == 2:
                    y += 2
                    break
                elif ulang == 3:
                    y += 3
                    break
                else:
                    print('\nPerintah yang anda masukan error, silahkan coba lagi')
                    continue
            if y == 1:
                continue
            elif y == 2:
                a += 1
                break
            else:
                a += 2
                break 
    
    elif pilihan == 2:
        m = 0
        while m == 0:
            T = []
            T2 = (10, 30, 45, 21, 12, 13, 31, 90)
            T3 = ('pRaktikum', 'praktikum', 'Praktikum', 'PraKtIkuM', 'PRAKTIKUM')
            print('============================================================')
            print('\tSelamat Datang di Mode isi list')
            print('============================================================')
            for k in range(0, 5):
                T.append(str(input('masukan nama kendaraan hingga 5 buah = ')))
            T1 = tuple(T)
            print('Silahkan pilih 1. Output satu | 2. Output dua')
            pilihan3 = int(input('Masukan pilihan Anda (1/2) = '))

            if pilihan3 == 1:
                print('Output 1 adalah =', T3[1], T3[3], T3[4], T1[4], T1[2])
            elif pilihan3 == 2:
                print('Output 2 adalah =')
                for c in range(3):
                    print(T2[3], 'dan', T2[5])
            
            print('============================================================')
            print('Program telah selesai | 1. Ulang Program | 2. Selesai | 3. Balik Ke Menu Awal')
            x = 0
            while x == 0:
                ulang2 = int(input('Masukan pilihan Anda (1/2/3) = '))
                if ulang2 == 1:
                    x += 1
                    break
                elif ulang2 == 2:
                    x += 2
                    break
                elif ulang2 == 3:
                    x += 3
                    break
                else:
                    print('\nPerintah yang anda masukan error, silahkan coba lagi')
                    continue
            if x == 1:
                continue
            elif x == 2:
                a += 1
                break
            else:
                a += 2
                break 

    else:
        print('Perintah yang anda masukan salah, silahkan coba lagi')
        continue
    
    e = 0
    while a < 3:
        if a == 1:
            e += 1
            break
        elif a == 2:
            e += 2
            break
    
    if e == 1:
        break
    else:
        continue


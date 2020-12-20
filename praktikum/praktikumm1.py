def Kalkulator():   
    i = 0
    while i == 0:
        print('\n\tSelamat Datang di Program Kalkulator Sederhana')
        print("\nSilahkan Pilih Operasi Yang Ada", "\n1. Kurang", "\n2. Tambah", "\n3. Bagi", "\n4. Kali")

        pilihan2 = int(input('Masukkan pilihan Anda (1/2/3/4): '))
        if pilihan2 == 1:
            angka1 = int(input('Masukkan Angka Pertama: '))
            angka2 = int(input('Masukkan Angka kedua: '))
            print(angka1, "-", angka2, "=", angka1 - angka2)
        elif pilihan2 == 2:
            angka1 = int(input('Masukkan Angka Pertama: '))
            angka2 = int(input('Masukkan Angka Kedua: '))
            print(angka1, "+", angka2, "=", angka1 + angka2)
        elif pilihan2 == 3:
            angka1 = int(input('Masukkan Angka Pertama: '))
            angka2 = int(input('Masukkan Angka Kedua: '))
            print(angka1, ":", angka2, "=", angka1 / angka2)
        elif pilihan2 == 4:
            angka1 = int(input('Masukkan Angka Pertama: '))
            angka2 = int(input('Masukkan Angka Kedua: '))
            print(angka1, "x", angka2, "=", angka1 * angka2)
        else:
            print('Pilihan error, silahkan coba lagi')
            continue
        
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
        
Kalkulator()

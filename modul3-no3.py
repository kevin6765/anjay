i = 0
while i == 0:
    #INPUT
    print("\n========================================================================================")
    print('Selamat datang di Perpustakaan Trunojoyo, silahkan masukan Data Diri anda\n')
    nama = str(input('NAMA = '))
    nim = str(input('NIM = '))
    banyak_buku = str(input('Banyak buku yang dipinjam = '))
    durasi_pinjam = int(input('Durasi pinjam Buku anda = '))
    denda1 = 2000
    denda2 = 5000
    
    #PROSES
    if durasi_pinjam <= 7:
        denda_total = 0
    else: 
        proses1 = ((durasi_pinjam // 7) - 1) * denda2
        proses2 = (durasi_pinjam - 7) * denda1
        denda_total = proses1 +  proses2

    #OUTPUT
    if denda_total == 0:
        print('\nHalo', nama, 'dengan NIM', nim, 'dan total buku dipinjam', banyak_buku, 'Buah')
        print('Selamat kamu terbebas dari denda karena tidak telat dalam mengembalikan Buku')
    else:
        print('\nHalo', nama, 'dengan NIM', nim, 'dan total buku dipinjam', banyak_buku, 'Buah') 
        print('Maaf kamu terkena denda RP.', denda_total)
        print('Yang terhitung denda harian sebesar RP.', proses2, 'dan Denda mingguan sebesar RP.', proses1)
        print('Karena telat dalam mengembalikan Buku selama', durasi_pinjam - 7, 'Hari')
    print('\nProgram perhitungan denda telah selesai\nApakah kamu ingin menghitung total denda lagi?')
    print("=======================================================================================\n")

    #LOOPING
    y = 0
    while y == 0:
        perintah = int(input('Ketik 0 untuk YA dan 1 untuk TIDAK = '))
        if perintah == 0:
            y += 1
            break
        elif perintah == 1:
            y += 2
            break
        else:
            print('\nPerintah yang anda masukan error, silahkan coba lagi')
            continue
    if y == 1:
        continue
    else:
        break
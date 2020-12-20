z = 0
while z == 0:
    print('Selamat datang di warung buah kami, silahkan pilih barang yang ingin dibeli')
    uang = int(input('Masukan uang yang anda miliki = '))
    barang = int(input('Pilih barang, 1. Semangka 2. Melon 3. Jambu 4. Pepaya 5. Mangga = '))
    if barang == 1:
        barang_belian = int(input('Harga semangka RP. 50000, Mau beli berapa? = '))
        barang_belian2 = barang_belian * 50000
    elif barang == 2:
        barang_belian = int(input('Harga melon RP. 30000, Mau beli berapa? = '))
        barang_belian2 = barang_belian * 30000
    elif barang == 3:
        barang_belian = int(input('Harga jambu RP. 20000, Mau beli berapa? = '))
        barang_belian2 = barang_belian * 20000
    elif barang == 4:
        barang_belian = int(input('Harga pepaya RP. 10000, Mau beli berapa? = '))
        barang_belian2 = barang_belian * 10000
    elif barang == 5:
        barang_belian = int(input('Harga Mangga RP. 60000, Mau beli berapa? = '))
        barang_belian2 = barang_belian * 60000
    else:
        print('Pilihan anda error, silahkan coba lagi')
        continue
    
    if barang_belian2 <= 200000:
        barang_belian1 = barang_belian2
        total_harga = uang - barang_belian2
        print('Total harga kamu adalah', barang_belian1)
        print('Uangmu yaitu', uang, 'dikurangi harga yaitu', barang_belian1, 'menjadi', total_harga)
    else:
        barang_belian1 = barang_belian2 * 5/100
        total_harga = barang_belian2 - barang_belian1
        total_harga2 = uang - total_harga
        print('Kamu mendapatkan diskon', barang_belian1, 'karena belanja di atas 200 Ribu')
        print('Total harga kamu adalah', total_harga)
        print('Uangmu yaitu', uang, 'dikurangi harga yaitu', total_harga, 'menjadi', total_harga2)
        print('programmu telah selesai')

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
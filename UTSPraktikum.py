z = 0
while z == 0:

    uang = int(input('Masukan uang yang anda punya = '))
    barang = {'Melon': 50000, 'Durian': 100000, 'Semangka': 40000, 'Nanas': 5000, 'Apel': 5000, 'Pisang': 5000}
    
    for nama_barang in barang:

        print('--------------------------------------------------')
        print('Anda memiliki RP', uang, 'di dompet Anda')
        print('Harga setiap', nama_barang, 'adalah RP', barang[nama_barang])
    
        input_count = input('Mau berapa ' + nama_barang + '?: ')
        print('Anda akan membeli', input_count, nama_barang)
    
        count = int(input_count)
        total_price = barang[nama_barang] * count

        if total_price <= 200000:
            total_price1 = total_price
        else:
            total_price1 = total_price * 0.05

        print('Harga total adalah RP', total_price)
    
        if uang >= total_price1:
            print('Anda telah membeli', input_count, nama_barang)
            uang -= total_price
        
            if uang == 0:
                print('Dompet Anda kosong')
                break

        else:
            print('Uang Anda tidak mencukupi')
            print('Anda tidak dapat membeli', nama_barang, 'sebanyak itu')

    print('Uang Anda tinggal', uang)

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
